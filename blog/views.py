from django.shortcuts import render
from django.utils import timezone
from .models import Equipement
from .models import Animal

def post_list(request):
    animaux = Animal.objects.all()
    return render(request, 'blog/post_list.html', {'billets': animaux})

from django.shortcuts import render, get_object_or_404

def post_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'blog/post_detail.html', {'billet': animal})

