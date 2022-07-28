from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('books', views.books , name='books'),
    path('update/<str:id>', views.update , name='update'),
    path('delete/<str:id>', views.delete , name='delete'),

]