from django.shortcuts import render
from .models import Task
from datetime import datetime, date
import re

def index(request):
    context = {'today': date.today().isoformat()}

    if request.method == 'POST':
        name = request.POST.get('task_name', '').strip()
        description = request.POST.get('description', '').strip()
        deadline_str = request.POST.get('deadline', '').strip()

        if not name or not description or not deadline_str:
            context['error'] = 'All fields are required.'
        elif re.fullmatch(r'\d+', name):
            context['error'] = 'Task name must not be all numbers.'
        else:
            try:
                deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date()
                if deadline < date.today():
                    context['error'] = 'Deadline cannot be in the past.'
                else:
                    Task.objects.create(name=name, description=description, deadline=deadline)
                    context['success'] = 'Task added successfully!'
            except ValueError:
                context['error'] = 'Invalid date format.'

    context['tasks'] = Task.objects.all()
    return render(request, 'index.html', context)
