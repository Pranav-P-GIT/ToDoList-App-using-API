from django.shortcuts import redirect, render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task
from .serializer import TaskSerializer
import requests
from django.shortcuts import get_object_or_404
from django.contrib import messages

#Constructing a custom API

class ListTasks(APIView):
    def get(self,request):
        Tasks=Task.objects.all()
        serializer=TaskSerializer(Tasks,many=True)
        return Response(serializer.data)
    
class SingleTask(APIView):
    def get(self,request,pk):
        Tasks=Task.objects.get(id=pk)
        serializer=TaskSerializer(Tasks,many=False)
        return Response(serializer.data)
    
class CreateTask(APIView):
    def post(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class UpdateTask(APIView):
    def post(self,request,pk):
        Tasks=Task.objects.get(id=pk)
        serializer=TaskSerializer(instance=Tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class DeleteTask(APIView):
    def delete(self,request,pk):
        Tasks=Task.objects.get(id=pk)
        Tasks.delete()
        return Response("Succesfully Deleted")
    
    
    
#Retrieving and manipulating data obtained from a custom-built API.
    
def showtasks(request):
    response=requests.get('http://127.0.0.1:8000/').json()
    return render(request, 'show.html', {'response':response})


def showsingle(request):
        a = request.GET['id']
        print(a)
        api=requests.get('http://127.0.0.1:8000/'+ a).json()
        context={'api':api}
        return render(request,"showone.html", context)
    
    
def updatetask(request):
    a = request.GET['id']
    if request.method == 'POST': 
        b = request.POST['task']
        c=  request.POST.get('user_choice') == 'on'
        task_data = {"id": a,"title": b,"completed": c}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url = "http://127.0.0.1:8000/update/"+a, json=task_data, headers=headers)
        print(res.text)
        messages.success(request, 'Task updated successfully')
        return redirect('/show')
    else:
        return render(request, 'update.html')
    
    
    
def createtask(request):
    if request.method == 'POST':
        a = request.POST['task']
        b=  request.POST.get('user_choice') == 'on'
        task_data = {"title": a,"completed": b,}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url = "http://127.0.0.1:8000/create/", json=task_data, headers=headers)
        print(res.text)
        messages.success(request, 'Task created successfully')
        return redirect('/show')
    else:
        return render(request, 'create.html')

    
    
def deletetask(request):
        a = request.GET['id']
        singletask = get_object_or_404(Task, id=a)
        singletask.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('/show')

    
    
    
