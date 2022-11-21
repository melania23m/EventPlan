from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView
from rest_framework.reverse import reverse_lazy

from todo_app.forms import BudgetForm
from todo_app.models import ToDoList, Budget


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



class BudgetCreateView(CreateView):
    template_name = "todo_app/create_budget.html"
    model = Budget
    form_class = BudgetForm

    success_url = reverse_lazy('budget')


class BudgetListView(ListView):
    template_name = "todo_app/budget.html"
    model = Budget
    context_object_name = 'all_budgets'
