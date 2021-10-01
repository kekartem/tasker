from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from tacker.models import Task


class MainView(View):
    def get(self, request):
        data = {}
        data['c1'] = []
        data['c2'] = []
        data['c3'] = []
        data['c4'] = []

        objects = Task.objects.all()
        for obj in objects:
            if obj.column == 1:
                data['c1'].append(obj)
            elif obj.column == 2:
                data['c2'].append(obj)
            elif obj.column == 3:
                data['c3'].append(obj)
            else:
                data['c4'].append(obj)


        return render(request, 'index.html', context=data)


class AddTask(View):
    def post(self, request):
        new = Task.objects.create(title=request.POST.get('title'), description=request.POST.get('description'),
                                  column=int(request.POST.get('col')))
        new.save()

        return redirect('/')


class ChangeStatus(View):
    def post(self, request):
        print(request.POST.get('id'))
        print(request.POST.get('col'))
        old = Task.objects.get(id=int(request.POST.get('id')))
        old.column = int(request.POST.get('col'))
        old.save()

        return redirect('/')

class Delete(View):
    def post(self, request):
        toDelete = Task.objects.get(id=int(request.POST.get('id')))
        toDelete.delete()

        return redirect('/')


class Test(View):
    def post(self, request):
        print(request.POST.get('test'))
        return redirect('/')