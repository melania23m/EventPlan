from django.contrib import admin

from todo_app.models import ToDoList, Budget

admin.site.register(ToDoList)
admin.site.register(Budget)