from django.shortcuts import render
#from django.template import loader
#from django.http import HttpResponse

from .models import People


def index(request, people_id):
    people = People.objects.get(pk=people_id)
    all_attributes = [
        people.person_gender,
        people.person_firstname,
        people.person_lastname,
        people.person_shortname,
        people.person_email_adress,
        people.person_phone_number,
        people.person_information,
        people.person_found,
        people.person_interests,
        people.person_photo,
    ]
    context = {
        'people': people,
        'all_attributes': all_attributes
    }
    return render(request, 'meetings/index.html', context)

