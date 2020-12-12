
from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Task
from django.contrib.auth.models import User , auth
from datetime import datetime
from datetime import date
import json
import time
# milliseconds = int(round(time.time() * 1000))
# print(milliseconds)
def index(request):
    tasks = reversed(Task.objects.all())
    point_t = Task.objects.all()
    c_task = reversed(Task.objects.all())
    total_point = 0
    total_c_task = 0
    total_r_task = 0
    
    for item in point_t:
        if item.is_completed:
            total_c_task+=1
            point = item.point
            total_point += point
        else:
            total_r_task += 1

    if total_r_task <= 2:
        condition = "okay"
    elif total_r_task <= 4:
        condition = "not okay"
    elif total_r_task <= 6:
        condition = "bad"
    else:
        condition = "poor"


    print(">>>>>>>>>>>>>>>>>>",total_point)
    return render(request,'index.html',{'tasks':tasks,'c_tasks':c_task,'total_point':total_point,'total_c_task':total_c_task,'total_r_task':total_r_task , 'condition':condition})

def create(request):
    if request.method == "POST":
        task_name = request.POST.get('task_name',False)
        task_note = request.POST.get('task_note',False)
        point = request.POST.get('point',False)
        point = int(point)
        print('>>>>>>>>>>>>>>>>>>>',task_name)
        print('>>>>>>>>>>>>>>>>>>>',task_note)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        is_completed = False
        start_on = current_date
        start_at = current_time
        note = f"--- {task_note} on {current_date} at {current_time} --- "
        task = Task.objects.create(task_name=task_name,task_note= note,start_at=start_at,start_on=start_on,is_completed=is_completed , point = point)
        task.save()
        return redirect('/')
    else:
        return render(request,'create.html')
def completed(request):
    if request.method == "POST":
        get_id = request.POST.get('get_id',False)
        print(">>>>>>>>>>>>",get_id)
        get_one = Task.objects.get(id = get_id)
        get_one.is_completed = True
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        get_one.end_on = current_date
        get_one.end_at = current_time
        get_one.save()
        return redirect('/')
    else:
        return render(request,'index.html')

def view(request):
    if request.method == "POST":
        get_id = request.POST.get('get_id',False)
        get_one = Task.objects.get(id = get_id)
        return render(request,'view.html',{'tasks':get_one})
    else:
        return render(request,'index.html')

def edit(request):
    if request.method == "POST":
        get_id = request.POST.get('get_id',False)
        get_one = Task.objects.get(id = get_id)
        return render(request,'edit.html',{'tasks':get_one})
    else:
        return render(request,'index.html')

def save_edit(request):
    if request.method == "POST":
        get_id = request.POST.get('get_id',False)
        note = request.POST.get('note',False)
        get_one = Task.objects.get(id = get_id)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        today = date.today()
        current_date = today.strftime("%Y-%m-%d")
        get_one.task_note = f"{note} on {current_date} at {current_time} --- "
        get_one.save() 
        return redirect('/')
    else:
        return render(request,'edit.html')

