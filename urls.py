from sre_constants import SUCCESS
from django.conf import settings
from django.urls import path
from app import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MypasswordChangeForm
from django.contrib import admin

urlpatterns = [

  
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('cp seeds/', views.cpseeds, name='cp seeds'),
    path('eagle seeds/', views.eagleseeds, name='eagle seeds'),
    path('goodwill health/', views.goodwillhealth, name='goodwill health'),
    path('bayern seeds/', views.bayernseeds, name='bayern seeds'),
    path('naturals/', views.naturals, name='naturals'),
    path('maharashtra/', views.maharashtra, name='maharashtra'),
    path('kerala/', views.kerala, name='kerala'),
    path('uttarpradesh/', views.uttarpradesh, name='uttarpradesh'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),

    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MypasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
   
    path('registration/', views.CustomerRegistrationView.as_view(), name="customerregistration"),
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),
    path('analyze', views.analyze, name='analyze'),
   
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 