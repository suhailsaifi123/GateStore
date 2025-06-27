from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Gate(models.Model):
    MATERIAL_CHOICES = [
        ('iron', 'Iron'),
        ('steel', 'Steel'),
        ('wood', 'Wood'),
        ('aluminum', 'Aluminum'),
        ('other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES)
    dimensions = models.CharField(max_length=100, help_text='e.g. 6ft x 4ft')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='gates/', help_text='Main/Featured image')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending Approval"),
        ("approved", "Approved"),
        ("completed", "Completed"),
        ("rejected", "Rejected"),
    ]
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    gate = models.ForeignKey(Gate, on_delete=models.CASCADE)
    weight_kg = models.PositiveIntegerField(help_text="Weight in Kg")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    advance_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_proof = models.FileField(upload_to="orders/payment_proofs/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} for {self.gate.name}"
