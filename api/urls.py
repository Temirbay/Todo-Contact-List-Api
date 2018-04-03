from django.urls import path

from . import views

urlpatterns = [
    path('todos/', views.todo_list, name="todo_list"),
    path('todos/<int:todo_id>', views.todo_detail, name="todo_detail"),

    path('contacts/', views.contact_list, name="contact_list"),
    path('contacts/<int:contact_id>', views.contact_detail, name="contact_detail"),
]