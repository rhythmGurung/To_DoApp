from django.urls import path
from .views import home,update_todo, delete_todo



urlpatterns = [
    path('', home, name='home'),
    path('update/<int:todo_id>/', update_todo, name='update'),
    path('delete/<int:todo_id>/', delete_todo, name='delete'),
]