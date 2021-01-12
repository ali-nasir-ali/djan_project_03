from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.todolist, name='todolist'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('pricing/', views.pricing, name='pricing')

]

