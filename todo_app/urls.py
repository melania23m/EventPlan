from django.urls import path

from todo_app import views

urlpatterns =[
    path('list_of_todo/', views.ToDoListListView.as_view(), name='list-of-todo'),
    path('user_checked/', views.user_checked, name = 'user-checked'),
    path('budget/', views.budget, name = 'budget')
    #create_rating
]