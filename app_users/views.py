from django.shortcuts import render
from .models import Department, Employee
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

# Create your views here.
def home(request):
    return render(request, 'app_users/home.html', {'title': 'Home Page'})

def get_filter(filter_query = None):
    if filter_query:
        print('==>FROM DATABASE')
        employee = Employee.objects.filter(name__contains=filter_query)
        cache.set(filter_query, employee)
        return employee
    else:
        return Employee.objects.all()

def cached(request):
    filter_query = request.GET.get('search')
    if cache.get(filter_query):
        print('==>FROM CACHE')
        employee = cache.get(filter_query)
    else:
        if filter_query:
            employee = get_filter(filter_query)
        else:
            employee = get_filter()

    return render(request, 'app_users/cached.html', {'employee' :employee})