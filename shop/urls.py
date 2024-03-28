from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('shop_detail/', views.shop_detail, name='shop_detail'),
    path('cart/', views.cart, name='cart'),
    path('chackout/', views.chackout, name='chackout'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('notpage/', views.notpage, name='notpage'),
    path('contact/', views.contact, name='contact'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]