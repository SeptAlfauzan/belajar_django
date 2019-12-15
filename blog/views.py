from django.shortcuts import render

def blog_view(request):
    context = {
        'blog_page': 'active'
    }
    return render(request, 'blog_page/index.html', context)
# Create your views here.
