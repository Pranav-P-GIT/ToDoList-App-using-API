from creation import views
from django.urls import path
from .views import *

urlpatterns = [
    path('', ListTasks.as_view(),name='listtasks'),
    path('<int:pk>', SingleTask.as_view(),name='singletask'),
    path('create/', CreateTask.as_view(),name='createtask'),
    path('update/<int:pk>', UpdateTask.as_view(),name='updatetask'),
    path('delete/<int:pk>', DeleteTask.as_view(),name='deletetask'),
    path('show', views.showtasks,name='showtasks'),
    path('showone', views.showsingle,name='showone'),
    path('update', views.updatetask,name='update'),
    path('createtask', views.createtask,name='create'),
    path('delete', views.deletetask,name='delete'),
    
    
]