from django.shortcuts import render
from .models import HomeInfo,Social,PastEvent
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def Home(request):
    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()
    context = {'page': 'home', 'homeinfo': homeinfo,'social':social}
    
    return render(request, 'App/index.html', context)

def PastMeet(request):
    homeinfo = HomeInfo.objects.last()
    social = Social.objects.last()
    past = PastEvent.objects.all().order_by('-date')
    paginator = Paginator(past, 5)
    page = request.GET.get('page')
    try:
        past = paginator.page(page)
    except PageNotAnInteger:
        past = paginator.page(1)
    except EmptyPage:
        past = paginator.page(paginator.num_pages)
    
    # print(past)
    context = {'page': 'home', 'homeinfo': homeinfo,'social':social,'pastmeet':past}
    
    return render(request, 'App/pastmeet.html', context)
