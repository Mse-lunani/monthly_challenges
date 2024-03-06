from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# view is either a function or a class


def index(request):
    return HttpResponse("Hello, world. You're at the challenges index.")


def home(request):
    months2 = months()
    list_items = ''
    for month in months2:
        month_name = month['month']
        capitalized_month = month_name.capitalize()
        link = reverse('month-challenge', args=[month_name])
        list_items += f"<li><a href='{link}'>{capitalized_month}</a></li>"
    return HttpResponse(list_items)


def months():
    arr = [
        {'month': 'january', 'text': 'Eat no meat for the entire month!'},
        {'month': 'february', 'text': 'Walk for at least 20 minutes every day!'},
        {'month': 'march', 'text': 'Learn Django for at least 20 minutes every day!'},
        {'month': 'april', 'text': 'Eat no meat for the entire month!'},
        {'month': 'may', 'text': 'Walk for at least 20 minutes every day!'},
        {'month': 'june', 'text': 'Learn Django for at least 20 minutes every day!'},
        {'month': 'july', 'text': 'Eat no meat for the entire month!'},
        {'month': 'august', 'text': 'Walk for at least 20 minutes every day!'},
        {'month': 'september', 'text': 'Learn Django for at least 20 minutes every day!'},
        {'month': 'october', 'text': 'Eat no meat for the entire month!'},
        {'month': 'november', 'text': 'Walk for at least 20 minutes every day!'},
        {'month': 'december', 'text': 'Learn Django for at least 20 minutes every day!'}
    ]
    return arr


def monthly_challenge(request, month):
    text = None
    month_name = None
    arr = months()
    for i in arr:
        if i['month'] == month:
            text = i['text']
            month_name = i['month']
            break
    if not text:
        return HttpResponseNotFound('This month is not supported!')
    return render(request, "challenges/challenge.html", {
        "text": text,
        "month": month_name.capitalize()
    })


def monthly_challenge_by_number(request, month):
    arr = months()
    if month > len(arr):
        return HttpResponseNotFound('This month is not supported!')
    m = arr[month-1]['month']
    link = reverse('month-challenge', args=[m])
    return HttpResponseRedirect(link)
