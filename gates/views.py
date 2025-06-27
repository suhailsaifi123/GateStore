from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Gate, Order
from .forms import OrderForm
from django.conf import settings
import hashlib
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib.auth import get_user_model, authenticate, login
from django import forms
import os

# Create your views here.

def gate_list(request):
    gates = Gate.objects.all()
    material = request.GET.get('material')
    if material:
        gates = gates.filter(material=material)
    # Add more filters as needed
    return render(request, 'gates/gate_list.html', {'gates': gates})

def gate_detail(request, slug):
    gate = get_object_or_404(Gate, slug=slug)
    return render(request, 'gates/gate_detail.html', {'gate': gate})

def live_preview(request):
    gates = Gate.objects.all()
    return render(request, 'gates/live_preview.html', {'gates': gates})

@login_required
def place_order(request, slug):
    gate = get_object_or_404(Gate, slug=slug)
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.gate = gate
            weight = order.weight_kg
            if gate.material == 'iron':
                price_per_kg = 90
            else:
                price_per_kg = float(gate.price) / max(weight, 1)
            order.total_price = price_per_kg * weight
            order.advance_paid = order.total_price * 0.5
            order.status = 'pending'
            order.save()
            return render(request, 'gates/order_success.html', {'order': order})
    else:
        form = OrderForm()
    return render(request, 'gates/place_order.html', {'form': form, 'gate': gate})

@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        data = request.POST
        # Extract required fields
        posted_hash = data.get('hash')
        key = data.get('key')
        txnid = data.get('txnid')
        amount = data.get('amount')
        productinfo = data.get('productinfo')
        firstname = data.get('firstname')
        email = data.get('email')
        status = data.get('status')
        gate_name = productinfo
        # PayUMoney hash sequence for response:
        # salt|status|||||||||||email|firstname|productinfo|amount|txnid|key
        salt = settings.PAYUMONEY_MERCHANT_SALT
        try:
            hash_seq = f"{salt}|{status}|||||||||||{email}|{firstname}|{productinfo}|{amount}|{txnid}|{key}"
            calc_hash = hashlib.sha512(hash_seq.encode('utf-8')).hexdigest().lower()
        except Exception:
            return HttpResponse('Hash Error', status=400)
        if calc_hash != posted_hash:
            return HttpResponse('Invalid hash', status=400)
        # Find user and gate
        User = get_user_model()
        try:
            user = User.objects.get(username=firstname)
            gate = Gate.objects.get(name=gate_name)
        except Exception:
            return HttpResponse('User or Gate not found', status=400)
        # Calculate weight from amount (reverse calculation)
        # For iron: price_per_kg = 90, advance = total*0.5, total = price_per_kg*weight
        # So, weight = (amount*2)/price_per_kg
        if gate.material == 'iron':
            price_per_kg = 90
        else:
            price_per_kg = float(gate.price)
        try:
            weight = round((float(amount)*2)/price_per_kg)
        except Exception:
            weight = 1
        total_price = price_per_kg * weight
        advance_paid = float(amount)
        # Create order
        order = Order.objects.create(
            user=user,
            gate=gate,
            weight_kg=weight,
            total_price=total_price,
            advance_paid=advance_paid,
            status='approved',
        )
        return render(request, 'gates/order_success.html', {'order': order})
    return HttpResponse('Invalid request', status=400)

@csrf_exempt
def payment_failure(request):
    return HttpResponse('Payment Failed!')

class AdminImageUploadForm(forms.Form):
    image = forms.ImageField(label='Select an image to upload')

# Custom admin login view
def admin_login(request):
    error = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_upload_image')
        else:
            error = 'Invalid credentials or not an admin.'
    return render(request, 'gates/admin_login.html', {'error': error})

# Only staff can access
@user_passes_test(lambda u: u.is_staff)
def admin_upload_image(request):
    uploaded_url = None
    if request.method == 'POST':
        form = AdminImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            save_path = os.path.join(settings.MEDIA_ROOT, 'gates', image.name)
            with open(save_path, 'wb+') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            uploaded_url = settings.MEDIA_URL + 'gates/' + image.name
    else:
        form = AdminImageUploadForm()
    return render(request, 'gates/admin_upload_image.html', {'form': form, 'uploaded_url': uploaded_url})
