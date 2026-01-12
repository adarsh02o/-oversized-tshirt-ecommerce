from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from products.models import TShirt

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('products:home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Account created successfully!')
        return response

@login_required
def admin_dashboard(request):
    print(f"User: {request.user.username}, is_staff: {request.user.is_staff}, is_authenticated: {request.user.is_authenticated}")
    
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('products:home')
    
    tshirts = TShirt.objects.all()
    context = {
        'tshirts': tshirts,
        'total_products': tshirts.count(),
    }
    return render(request, 'accounts/admin_dashboard.html', context)
