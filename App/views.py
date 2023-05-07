from django.shortcuts import render
# Create your views here.

def Home(request):
    # recent_news = Post.objects.all().order_by('-created')[:2]
    # slider = Post.objects.all().order_by('-views')[:5]
    # most_views = Post.objects.all().order_by('-views')[:2]
    # others1 = Post.objects.all().order_by('-created')[2:4]
    # others2 = Post.objects.all().order_by('-created')[4:6]
    # footer = Footer.objects.last()
    # contact = Cont.objects.last()
    # context = {'footer': footer, 'recent':recent_news, 'most':most_views, 'others1':others1, 'others2':others2, 'slider':slider, 'contact':contact}
    
    return render(request, 'App/index.html', context={'page':'home'})
