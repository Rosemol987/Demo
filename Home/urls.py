from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='home'),
    path('about', views.about,name='about'),
    #path('show',views.show,name='show'),
    path('department',views.department, name='department'),
    path('doctor',views.doctor,name='doctor'),
    path('booking',views.booking),
]