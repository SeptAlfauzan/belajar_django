from django.shortcuts import render
from home.models import Food

def home_view(request):
    foods_list = Food.objects.all()
    context = {
        'home_page':'active',
        'judul': 'Belajar Django Pemula',
        'foods_list': foods_list
        }
    return render(request, 'home/index.html', context)

# Create your views here.
