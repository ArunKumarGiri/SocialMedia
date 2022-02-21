from django.conf import settings
from django.urls import path
from app import views
from .forms import LoginForm, MyPasswordChangeForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home', views.home,name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/<int:pk>', views.delete, name='delete'),
    path('accounts/profile/<str:username>', views.profile_view),
    
    

    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'), name='logout'),    
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    path('', views.RegistrationView.as_view(), name='customerregistration'),
]
