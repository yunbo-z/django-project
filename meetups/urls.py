from django.urls import path
from . import views
# this variable must be called urlpatterns
# because django will look for this variable in urls.py file
urlpatterns = [
    path('meetups/', views.index),#ourdomain.com/meetups
    path('meetups/<slug:meetup_slug>',views.meetup_details),
]