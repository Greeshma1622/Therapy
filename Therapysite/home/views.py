from django.shortcuts import render,redirect
from .models import Plans, Counselors,Booking,Client,Contact,Room,Message
from .forms import BookingForm
from django.contrib import messages
from django.http import HttpResponse, JsonResponse

# Create your views here.

def Home(request):
    return render(request,'home.html')

def counselors(request):
    dict_counselors = {
        'counselordetails': Counselors.objects.all()
    }
    return render(request,'counselors.html',dict_counselors)

def plans(request):
    dict_plans = {
        'plansdetails':Plans.objects.all()
    }
    return render(request,'plans.html',dict_plans)

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)

def signup(request):
        if request.method == "POST":
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            phno = request.POST['phno']
            password2 = request.POST['password2']
            if password == password2 :
                if Client.objects.filter(email = email).exists():
                    messages.info(request,'email taken')
                    return redirect('signup')
                else:
                    customer = Client.objects.create(email = email,name = name,password = password,phno = phno)
                    customer.save()
                    messages.info(request,'user created')
                    return redirect('login')
            else:
                messages.info(request,'password is not match')
                return redirect('signup')
        else:
                return render(request,'signup.html')
 

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            check_user = Client.objects.get(email=email,password=password)
            request.session['email'] = check_user.email
            request.session['name'] = check_user.name
            request.session['phno'] = check_user.phno
            return redirect('newhome')
        except Client.DoesNotExist:
            messages.error(request,'Invalid username and password')
            return redirect('login')
    return render(request,'login.html')

def forgot(request):
    if request.method == "POST":
        email= request.POST['email']
        password = request.POST['password']
        if Client.objects.filter(email=email).exists():
            Client.objects.filter(email=email).update(password=password)
            return redirect('login')
        else:
            messages.error(request,'invalid data')
            return redirect('forgot')
    return render(request,'forgot.html')

def contact(request):
    if request.method=="POST":
        if request.POST['name'] is not None:
            enq=Contact.objects.create(name=request.POST['name'],email=request.POST['email'],phno=request.POST['phno'])
            enq.save()
            dicts={'out':1,'name':request.POST['name']}
        return render(request,'contact.html',dicts)
    return render(request,'contact.html')

def Chat(request):
    return render(request,'chat.html')

def rooms(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })
    
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})