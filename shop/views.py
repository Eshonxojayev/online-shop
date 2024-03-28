from django.shortcuts import render, redirect
from .models import Product, Category, Profile
from .forms import RegisterForm

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {'products': products, 'categories': categories})

def shop(request):
    return render(request, 'shop.html')

def shop_detail(request):
    return render(request, 'shop-detail.html')

def cart(request):
    return render(request, 'cart.html')

def chackout(request):
    return render(request, 'chackout.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def notpage(request):
    return render(request, '404.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form':form})
