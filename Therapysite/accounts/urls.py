from django.urls import path
from .import views

urlpatterns = [
    path('newhome',views.Newhome.as_view(),name="newhome"),
    path('logout/',views.Logout.as_view(),name="logout"),
    path('delete/',views.Delete.as_view(),name="delete"),
    path('profile/',views.Profile.as_view(),name="profile"),
    path('editprofile/',views.Editprofile.as_view(),name="editprofile"),
]