from common.views import index, RegisterView, CreateUserProfile
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.urls import path
from django.urls import include
  
app_name = 'common'  
urlpatterns = [  
	# path('', include('django.contrib.auth.urls')),
    path('', index, name='index'),
	path('login/', LoginView.as_view(template_name='common/login.html'), name='login'), 
	path('logout/', LogoutView.as_view(), name='logout'),
	path('register/', RegisterView.as_view(
		template_name='common/register.html',
		success_url=reverse_lazy('common:profile-create')
    ), name='register'),
	path('profile-create/', CreateUserProfile.as_view(template_name = 'common/profile-create.html'), name='profile-create'),
]