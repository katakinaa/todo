from django.urls import path
from todo_ import views

urlpatterns = [
    path('tasks/', views.task_list_create_api_view, name='task-list-create'),
    path('tasks/detail/<int:id>/', views.task_detail_api_view, name='task-detail'),
    path('tasks/update/<int:id>/', views.task_update_api_view, name='task-update'),
    path('tasks/delete/<int:id>/', views.task_delete_api_view, name='task-delete'),
]
