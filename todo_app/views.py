from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView

from providers.models import Rating
from todo_app.models import ToDoList


class ToDoListListView(ListView):
    model = ToDoList
    template_name = "todo_app/list-of-todo.html"
    context_object_name = 'all_objects'


def user_checked(request):
    all_objects = ToDoList.objects.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            id_list = request.POST.getlist('boxes')
            all_objects.update(is_checked=False)
            for x in id_list:
                ToDoList.objects.filter(pk=int(x)).update(is_checked=True)
            messages.success(request,"Updated!")
            return redirect('list-of-todo')

        else:
            return render(request, 'todo_app/list-of-todo.html', {'all_objects': all_objects})


def budget(request):
    return render (request,'todo_app/budget.html')

