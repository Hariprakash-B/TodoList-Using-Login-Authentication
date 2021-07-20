from django.shortcuts import render,redirect
from testapp1.models import login
from testapp1.forms import *
# Create your views here.
def registration(request):
    if(request.method=='GET'):
        form = ContactForm()
        return render(request,'registration.html')
    elif(request.method=='POST'): 
        form = ContactForm(request.POST)
        if form.is_valid():
            l=login.objects.create(name=form.cleaned_data.get("name"),email=form.cleaned_data.get("email"),password=form.cleaned_data.get("password"))
            l.save()
            return redirect('/')
        return render(request, 'registration.html', {'form': form})
def home(request):
    return render(request,'home.html') 
def loginsite(request):
    if(request.method=='GET'):
        form =loginForm()
        print(form)
        return render(request,'login.html')
    elif(request.method=='POST'): 
        form =loginForm(request.POST)
        if form.is_valid():
            global getname
            getname=form.cleaned_data.get("name")
            print("login form validated",getname)
            return redirect('/home')
        return render(request, 'login.html', {'form': form})
def profile(request):
    print(getname)
    place =models.login.objects.get(name=str(getname))
    print(place.name,place.email,place.password)
    context={
        'name':place.name,
        'email':place.email,
        'password':place.password
    }
    return render(request,'profile.html',context)  
def index(request):
    tasks=taskmodel.objects.filter(name=getname).order_by('-id')
    form=taskform()
    print(form)
    print(getname)
    if request.method=='POST':
        form=taskform(request.POST)
        p=request.POST.get("complete")
        print("password:",p)
        if form.is_valid():
            print(form)
            form.save()
        return redirect('/home')
    context={'tasks':tasks,'form':form,'name':getname}
    return render(request,'index.html',context)


def update(request,pk):
    tasks=taskmodel.objects.filter(name=getname).order_by('-id')
    task=taskmodel.objects.get(id=pk)
    form=taskform(instance=task)
    if request.method=='POST':
        form=taskform(request.POST,instance=task)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/home')
    context={'tasks':tasks,'form':form,'name':getname}
    return render(request,'update.html',context)

def delete(request,pk):
    task=taskmodel.objects.get(id=pk)
    task.delete()
    return redirect('/home')
def main(request):
    return render(request,'main.html')