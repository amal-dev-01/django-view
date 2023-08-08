from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.index,name="name"),
    path('service/',views.service,name="service"),
    path('contact/',views.contact,name="contact"),
]
