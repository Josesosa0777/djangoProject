from django.urls import path
from todolist_app import views

urlpatterns = [
    # set the name for the view and for the link:
    path('', views.todolist, name='todolist'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]
