from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from products.models import TShirt

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    authentication_form = CustomAuthenticationForm

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
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('products:home')
    
    tshirts = TShirt.objects.all()
    in_stock_count = tshirts.filter(stock__gt=10).count()
    low_stock_count = tshirts.filter(stock__gt=0, stock__lte=10).count()
    context = {
        'tshirts': tshirts,
        'total_products': tshirts.count(),
        'in_stock_count': in_stock_count,
        'low_stock_count': low_stock_count,
    }
    return render(request, 'accounts/admin_dashboard.html', context)
