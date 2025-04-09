from django.shortcuts import render,redirect
from . models import student,History

# Create your views here.
def home(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        des=request.POST.get('des')
        print(name,des)
        student.objects.create(name=name,des=des)
        # print("successfully added the data to the database")
        return redirect("todo")

    return render(request,"home.html")


def todo(request):
    data=student.objects.all().order_by("-id")
    return render(request,"todolist.html",{'data':data})



def context(request):
    return render(request,"context.html")

def edit(request,pk):
     data2=student.objects.get(id=pk)
     if request.method=="POST":
        name=request.POST.get('name')
        des=request.POST.get('des')
        print(name,des)
        data2.name=name
        data2.des=des
        data2.save()
        # print("updated successfully")
        return redirect("todo") 
     return render(request,"edit.html",{'data':data2})


def delete(request,id):
    data=student.objects.get(id=id)
    History.objects.create(name=data.name,des=data.des)
    data.delete()
    return redirect("history")

def history(request):
    data4=History.objects.all()
    return render(request,"history.html",{'data':data4})
