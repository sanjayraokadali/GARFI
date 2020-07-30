from django.conf.urls import url
from GarfiApp import views

app_name = 'GarfiApp'

urlpatterns = [
    url(r'^$',views.AboutPage.as_view(),name='aboutpage'),
    url(r'^SignUp/$',views.SignUp,name='signup_page'),
    url(r'^SignUp/Success/$',views.SignUpSuccess,name='signup_success'),
    url(r'^Login/$',views.LoginPage,name='loginpage'),
    url(r'^Login/UserHome/$',views.UserHome,name='user_home'),
    url(r'^Login/UserHome/InputCode/$',views.InputCode,name='inputcode'),
    url(r'^Login/UserHome/InputCode/SavePoints',views.SavePoints,name='save_points'),
]
