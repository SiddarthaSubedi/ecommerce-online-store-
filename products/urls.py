from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('category/', views.category, name='all_categories'),
]