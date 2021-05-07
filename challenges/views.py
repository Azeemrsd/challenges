from django.shortcuts import render

from django.http import Http404,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenge = {
    "january":'Goto Gym',
    "febraury":'Eat no meat for entire month',
    "march":'Drink at least 3 liters of water.',
    "april":'Walk for at least 20 mintes',
    "may":'Talk to your friends daily',
    "june":'Go for swimming everyday',
    "july":'Play cricket on weekends',
    "august":'Do not sleep more than 8 hours',
    "september":'Learn a new course',
    "october":'Applu for job',
    "november":'Save at least 500 dollars',
    "december":'No challenge you have done a good job.'
}

def index(request):
    months = list(monthly_challenge.keys())
    return render(request,'challenges/index.html',{
        "months":months
    })

def monthly_challenges_by_number(request,month):
    months = list(monthly_challenge.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Month!')
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge',args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenges(request,month):
    # try:
         challenge_text = monthly_challenge[month]
         return render(request,'challenges/challenges.html', {"challengeText":challenge_text,"month":month})
    # except:
         raise Http404()