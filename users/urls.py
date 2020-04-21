from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='WDS-home'),
    path('about/',views.login,name='WDS-about'),
    path('customers/',views.signup,name='WDS-customer')
]