from django.shortcuts import render

# Create your views here.
def about_view(request):
    context = {'about_page': 'active'}
    return render(request, 'about/index.html', context)