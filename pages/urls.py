from django.urls import path
from pages import views
app_name='pages'
urlpatterns=[
path('',views.home_page,name='home'),
path('about/',views.about_page,name='about'),
path('login/',views.login_page,name='login'),
path('logout/',views.logout_page,name='logout'),
path("signup/", views.signup_page, name='signup'),


] 