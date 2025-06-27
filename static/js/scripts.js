// Professional GateStore JavaScript

// Enhanced navbar scroll effect with smooth transitions
window.addEventListener('scroll', function() {
  const nav = document.querySelector('.navbar');
  const scrollY = window.scrollY;
  
  if (scrollY > 10) {
    nav.classList.add('scrolled');
  } else {
    nav.classList.remove('scrolled');
  }
  
  // Add parallax effect to hero section
  const hero = document.querySelector('.hero-section');
  if (hero) {
    hero.style.transform = `translateY(${scrollY * 0.5}px)`;
  }
});

// Enhanced active navigation highlighting with smooth transitions
document.addEventListener('DOMContentLoaded', function() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.nav-link');
  
  navLinks.forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
    
    // Add hover effects
    link.addEventListener('mouseenter', function() {
      this.style.transform = 'translateY(-2px)';
    });
    
    link.addEventListener('mouseleave', function() {
      this.style.transform = 'translateY(0)';
    });
  });
  
  // Initialize tooltips
  const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
  tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
  });
  
  // Add loading animations
  animateOnScroll();
  
  // Initialize back to top button
  createBackToTopButton();
});

// Enhanced smooth scrolling with easing
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const targetPosition = target.offsetTop - 80; // Account for fixed navbar
      window.scrollTo({
        top: targetPosition,
        behavior: 'smooth'
      });
    }
  });
});

// Enhanced form validation with real-time feedback
function validateForm(form) {
  const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
  let isValid = true;
  
  inputs.forEach(input => {
    if (!input.value.trim()) {
      showFieldError(input, 'This field is required');
      isValid = false;
    } else if (input.type === 'email' && !isValidEmail(input.value)) {
      showFieldError(input, 'Please enter a valid email address');
      isValid = false;
    } else if (input.type === 'tel' && !isValidPhone(input.value)) {
      showFieldError(input, 'Please enter a valid phone number');
      isValid = false;
    } else {
      clearFieldError(input);
    }
  });
  
  return isValid;
}

function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function isValidPhone(phone) {
  const phoneRegex = /^[\+]?[1-9][\d]{0,15}$/;
  return phoneRegex.test(phone.replace(/\s/g, ''));
}

function showFieldError(field, message) {
  clearFieldError(field);
  field.classList.add('is-invalid');
  field.style.borderColor = '#dc3545';
  
  const errorDiv = document.createElement('div');
  errorDiv.className = 'invalid-feedback';
  errorDiv.textContent = message;
  field.parentNode.appendChild(errorDiv);
  
  // Add shake animation
  field.style.animation = 'shake 0.5s ease-in-out';
  setTimeout(() => {
    field.style.animation = '';
  }, 500);
}

function clearFieldError(field) {
  field.classList.remove('is-invalid');
  field.style.borderColor = '';
  const errorDiv = field.parentNode.querySelector('.invalid-feedback');
  if (errorDiv) {
    errorDiv.remove();
  }
}

// Enhanced contact form handling with better UX
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    
    if (validateForm(this)) {
      showLoading(this);
      
      // Simulate form submission with realistic delay
      setTimeout(() => {
        hideLoading(this);
        showSuccessMessage('Thank you! Your message has been sent successfully. We\'ll get back to you soon.');
        this.reset();
        
        // Add success animation
        const formContainer = this.closest('.container');
        formContainer.style.animation = 'fadeInUp 0.6s ease-out';
      }, 2000);
    }
  });
  
  // Real-time validation
  const inputs = contactForm.querySelectorAll('input, textarea');
  inputs.forEach(input => {
    input.addEventListener('blur', function() {
      if (this.hasAttribute('required')) {
        if (!this.value.trim()) {
          showFieldError(this, 'This field is required');
        } else if (this.type === 'email' && !isValidEmail(this.value)) {
          showFieldError(this, 'Please enter a valid email address');
        } else {
          clearFieldError(this);
        }
      }
    });
  });
}

// Enhanced loading states with better visual feedback
function showLoading(form) {
  const submitBtn = form.querySelector('button[type="submit"]');
  const originalText = submitBtn.textContent;
  
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
  submitBtn.dataset.originalText = originalText;
  submitBtn.style.opacity = '0.7';
}

function hideLoading(form) {
  const submitBtn = form.querySelector('button[type="submit"]');
  submitBtn.disabled = false;
  submitBtn.textContent = submitBtn.dataset.originalText;
  submitBtn.style.opacity = '1';
}

// Enhanced success/error messages with animations
function showSuccessMessage(message) {
  const alertDiv = document.createElement('div');
  alertDiv.className = 'alert alert-success fade-in';
  alertDiv.innerHTML = `
    <div class="d-flex align-items-center">
      <i class="bi bi-check-circle-fill me-2"></i>
      <span>${message}</span>
    </div>
  `;
  
  const container = document.querySelector('.container');
  container.insertBefore(alertDiv, container.firstChild);
  
  // Auto-remove after 6 seconds
  setTimeout(() => {
    alertDiv.style.animation = 'fadeOut 0.5s ease-out';
    setTimeout(() => {
      alertDiv.remove();
    }, 500);
  }, 6000);
}

function showErrorMessage(message) {
  const alertDiv = document.createElement('div');
  alertDiv.className = 'alert alert-danger fade-in';
  alertDiv.innerHTML = `
    <div class="d-flex align-items-center">
      <i class="bi bi-exclamation-triangle-fill me-2"></i>
      <span>${message}</span>
    </div>
  `;
  
  const container = document.querySelector('.container');
  container.insertBefore(alertDiv, container.firstChild);
  
  setTimeout(() => {
    alertDiv.style.animation = 'fadeOut 0.5s ease-out';
    setTimeout(() => {
      alertDiv.remove();
    }, 500);
  }, 6000);
}

// Enhanced image lazy loading with fade-in effect
document.addEventListener('DOMContentLoaded', function() {
  const images = document.querySelectorAll('img[data-src]');
  
  const imageObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const img = entry.target;
        img.src = img.dataset.src;
        img.classList.add('fade-in');
        img.style.opacity = '0';
        
        img.onload = function() {
          img.style.transition = 'opacity 0.6s ease-in-out';
          img.style.opacity = '1';
        };
        
        imageObserver.unobserve(img);
      }
    });
  });
  
  images.forEach(img => imageObserver.observe(img));
});

// Enhanced webcam preview functionality with better error handling
function startWebcamPreview(gateUrl) {
  const video = document.getElementById('webcam');
  const canvas = document.getElementById('gateOverlay');
  const startBtn = document.querySelector('[onclick*="startWebcamPreview"]');
  
  if (!video || !canvas) {
    showErrorMessage('Preview elements not found. Please refresh the page.');
    return;
  }
  
  // Show loading state
  if (startBtn) {
    startBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Initializing...';
    startBtn.disabled = true;
  }
  
  navigator.mediaDevices.getUserMedia({ 
    video: { 
      width: { ideal: 1280 },
      height: { ideal: 720 },
      facingMode: 'environment'
    } 
  }).then(stream => {
    video.srcObject = stream;
    video.onloadedmetadata = () => {
      video.play();
      video.style.display = 'block';
      canvas.style.display = 'block';
      
      // Reset button
      if (startBtn) {
        startBtn.innerHTML = '<i class="bi bi-stop-circle me-2"></i>Stop Preview';
        startBtn.disabled = false;
        startBtn.onclick = () => stopWebcamPreview(stream);
      }
      
      drawOverlay();
      showSuccessMessage('Webcam preview started successfully!');
    };
  }).catch(error => {
    console.error('Error accessing webcam:', error);
    let errorMessage = 'Unable to access webcam. ';
    
    if (error.name === 'NotAllowedError') {
      errorMessage += 'Please allow camera permissions and try again.';
    } else if (error.name === 'NotFoundError') {
      errorMessage += 'No camera found on your device.';
    } else {
      errorMessage += 'Please check your camera settings and try again.';
    }
    
    showErrorMessage(errorMessage);
    
    if (startBtn) {
      startBtn.innerHTML = '<i class="bi bi-camera me-2"></i>Start Preview';
      startBtn.disabled = false;
    }
  });
}

// Enhanced overlay drawing with smooth animations
function drawOverlay() {
  const canvas = document.getElementById('gateOverlay');
  const video = document.getElementById('webcam');
  
  if (!canvas || !video) return;
  
  const ctx = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  
  // Draw video frame
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  
  // Add gate overlay with smooth positioning
  const gateImg = new Image();
  gateImg.onload = function() {
    const gateWidth = canvas.width * 0.4;
    const gateHeight = (gateImg.height / gateImg.width) * gateWidth;
    const x = (canvas.width - gateWidth) / 2;
    const y = canvas.height - gateHeight - 50;
    
    ctx.globalAlpha = 0.8;
    ctx.drawImage(gateImg, x, y, gateWidth, gateHeight);
    ctx.globalAlpha = 1.0;
  };
  gateImg.src = gateUrl;
  
  requestAnimationFrame(drawOverlay);
}

// Enhanced stop webcam function
function stopWebcamPreview(stream) {
  if (stream) {
    stream.getTracks().forEach(track => track.stop());
  }
  
  const video = document.getElementById('webcam');
  const canvas = document.getElementById('gateOverlay');
  const startBtn = document.querySelector('[onclick*="startWebcamPreview"]');
  
  if (video) video.style.display = 'none';
  if (canvas) canvas.style.display = 'none';
  
  if (startBtn) {
    startBtn.innerHTML = '<i class="bi bi-camera me-2"></i>Start Preview';
    startBtn.disabled = false;
    startBtn.onclick = () => startWebcamPreview();
  }
  
  showSuccessMessage('Webcam preview stopped.');
}

// Enhanced gate overlay on house image
function overlayGateOnHouse(gateUrl) {
  const canvas = document.getElementById('houseCanvas');
  const ctx = canvas.getContext('2d');
  const houseImg = document.getElementById('houseImage');
  
  if (!canvas || !houseImg) return;
  
  canvas.width = houseImg.naturalWidth;
  canvas.height = houseImg.naturalHeight;
  
  // Draw house image
  ctx.drawImage(houseImg, 0, 0, canvas.width, canvas.height);
  
  // Add gate overlay
  const gateImg = new Image();
  gateImg.onload = function() {
    const gateWidth = canvas.width * 0.3;
    const gateHeight = (gateImg.height / gateImg.width) * gateWidth;
    const x = (canvas.width - gateWidth) / 2;
    const y = canvas.height - gateHeight - 100;
    
    ctx.globalAlpha = 0.9;
    ctx.drawImage(gateImg, x, y, gateWidth, gateHeight);
    ctx.globalAlpha = 1.0;
  };
  gateImg.src = gateUrl;
}

// Enhanced gate position adjustment
function adjustGatePosition() {
  const canvas = document.getElementById('gateOverlay');
  if (!canvas) return;
  
  // Add smooth position adjustment logic here
  canvas.style.transition = 'all 0.3s ease-in-out';
}

// Enhanced gate filtering with smooth animations
function filterGates() {
  const materialFilter = document.getElementById('materialFilter');
  const gates = document.querySelectorAll('.gate-card');
  
  if (!materialFilter) return;
  
  const selectedMaterial = materialFilter.value;
  
  gates.forEach(gate => {
    const gateMaterial = gate.dataset.material;
    
    if (selectedMaterial === 'all' || gateMaterial === selectedMaterial) {
      gate.style.display = 'block';
      gate.style.animation = 'fadeInUp 0.5s ease-out';
    } else {
      gate.style.display = 'none';
    }
  });
  
  // Show/hide no results message
  const visibleGates = Array.from(gates).filter(gate => gate.style.display !== 'none');
  const noResults = document.getElementById('noResults');
  
  if (noResults) {
    if (visibleGates.length === 0) {
      noResults.style.display = 'block';
      noResults.style.animation = 'fadeIn 0.5s ease-out';
    } else {
      noResults.style.display = 'none';
    }
  }
}

// Enhanced price range update
function updatePriceRange() {
  const priceRange = document.getElementById('priceRange');
  const priceDisplay = document.getElementById('priceDisplay');
  
  if (!priceRange || !priceDisplay) return;
  
  const value = priceRange.value;
  const maxPrice = priceRange.max;
  const percentage = (value / maxPrice) * 100;
  
  priceDisplay.textContent = `$${value}`;
  priceRange.style.background = `linear-gradient(to right, #0d6efd 0%, #0d6efd ${percentage}%, #e9ecef ${percentage}%, #e9ecef 100%)`;
}

// Enhanced back to top button with smooth scroll
function createBackToTopButton() {
  const backToTopBtn = document.createElement('button');
  backToTopBtn.innerHTML = '<i class="bi bi-arrow-up"></i>';
  backToTopBtn.className = 'btn btn-primary position-fixed';
  backToTopBtn.style.cssText = `
    bottom: 20px;
    right: 20px;
    z-index: 1000;
    width: 50px;
    height: 50px;
    border-radius: 50%;
    display: none;
    box-shadow: 0 4px 15px rgba(13, 110, 253, 0.3);
  `;
  
  document.body.appendChild(backToTopBtn);
  
  // Show/hide button based on scroll position
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      backToTopBtn.style.display = 'block';
      backToTopBtn.style.animation = 'fadeIn 0.3s ease-out';
    } else {
      backToTopBtn.style.display = 'none';
    }
  });
  
  // Smooth scroll to top
  backToTopBtn.addEventListener('click', () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });
}

// Enhanced scroll animations
function animateOnScroll() {
  const elements = document.querySelectorAll('[data-aos]');
  
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.animation = 'fadeInUp 0.8s ease-out forwards';
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  
  elements.forEach(el => observer.observe(el));
}

// Enhanced debounce function for performance
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    25% { transform: translateX(-5px); }
    75% { transform: translateX(5px); }
  }
  
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(30px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  @keyframes fadeOut {
    from {
      opacity: 1;
      transform: translateY(0);
    }
    to {
      opacity: 0;
      transform: translateY(-10px);
    }
  }
  
  @keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
  }
`;
document.head.appendChild(style); 