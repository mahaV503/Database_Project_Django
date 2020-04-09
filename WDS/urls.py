
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homeview,name='WDS-home'),
    path('about/',views.aboutview,name='WDS-about'),
    path('customers/',views.customerview,name='WDS-customer')
]