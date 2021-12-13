from django.urls import path
from . import views
from .views import Home, Detail, Create, Contact

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/<int:pk>/',Detail.as_view(), name='detail'),
    path('new/',Create.as_view(), name='create'),
    path('about/', views.about, name='about'),
    path('contact/', Contact.as_view(), name='contact'),
    path('topics/', views.topics, name='topics')
]