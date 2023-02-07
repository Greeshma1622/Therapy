from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home,name='Home'),
    path('counselors', views.counselors,name='Counselor'),
    path('plans', views.plans,name='Plans'),
    path('booking', views.booking,name='Booking'),
    path('signup', views.signup,name='signup'),
    path('login', views.login,name='login'),
    path('forgot', views.forgot,name='forgot'),
    path('contact', views.contact,name='contact'),
    path('chat', views.Chat,name='Chat'),
    path('<str:room>/', views.rooms,name='room'),
    path('checkview', views.checkview,name='checkview'),
    path('send', views.send, name='send'),
       path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]