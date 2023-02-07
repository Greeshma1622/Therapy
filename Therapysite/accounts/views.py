from django.shortcuts import render,redirect
from django.views import View
from home.models import Client
from django.http import HttpResponse

class Newhome(View):
    def get(self,request):
        if request.session['email'] is not None:
            user=Client.objects.filter(email=request.session['email'])
        return render(request,'newhome.html',{'form':user})

class Profile(View):
    def get(self,request):
        if request.session['email'] is not None:
            user=Client.objects.filter(email=request.session['email'])
        return render(request,'profile.html',{'form':user})

class Editprofile(View):
    def get(self,request):
        edit1=request.session['email']
        edit=Client.objects.filter(email=edit1)
        return render(request,'editprofile.html',{'form':edit})
    def post(self,request):
        edit1=request.session['email']
        if request.method == 'POST':
            if Client.objects.filter(email=edit1).exists():
                if request.POST['password']:
                    Client.objects.filter(email=edit1).update(password=request.POST['password'])
                if request.POST['name']:
                    Client.objects.filter(email=edit1).update(name=request.POST['name'])
                if request.POST['email']:
                    if Client.objects.filter(email=edit1).exists():
                        edit=Client.objects.filter(email=edit1)
                        messages.error(request,"email already exists")
                        return render(request,'editprofile.html',{'form':edit})
                    else:
                         Client.objects.filter(email=edit1).update(email=request.POST['email'])
                         request.session['email']=request.POST['email']
                if request.POST['phno']:
                    Client.objects.filter(email=edit1).update(phno=request.POST['phno'])
                customer=Client.objects.filter(email=request.session['email'])
                return render(request,'profile.html',{'form':customer})

class Delete(View):
    def get(self,request):
        delete=request.GET['delete']
        Client.objects.filter(email=delete).delete()
        client=Client.objects.all()
        return render(request,'signup.html',{'form':client})

class Logout(View):
    def logout(self,request):
        request.session.pop('email',None)
        request.session.pop('name',None)
        request.session.pop('phno',None)

        return render(request,'home.html')
        




    