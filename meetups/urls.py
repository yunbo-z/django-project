from django.urls import path
from . import views
# this variable must be called urlpatterns
# because django will look for this variable in urls.py file
urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),#ourdomain.com/meetups
    path('meetups/<slug:meetup_slug>',views.meetup_details, name='meetup-detail'),
]
# The slug part indicates that this segment of the URL should match a slug (a URL-friendly string). 
# meetup_slug is a variable name that will be passed to the associated view function, 
# containing the value captured from the URL.