from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    meetups= [{
        'title': 'A First Meetup',
        'location': 'US',
        'slug': 'a-first_meetup'
        },
              {
                  'title':'A second Meetup',
                  'location':'Paris',
                  'slug':'a-second-meetup'
              }
              ]
    
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })