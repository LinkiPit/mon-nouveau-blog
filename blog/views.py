from django.shortcuts import render, get_object_or_404, redirect
from .forms import MoveForm
from .models import Animal, Equipement

def post_list(request):
    animaux = Animal.objects.filter()
    return render(request, 'blog/post_list.html', {'animaux': animaux})


def post_details(request, id_animal):
    animaux = Animal.objects.filter()
    animal = get_object_or_404(Animal, id_animal=id_animal)
    lieu = animal.lieu
    etat = animal.etat
    if request.method == "POST":
        form = MoveForm(request.POST, instance=animal)
    else:
        form = MoveForm()
    if form.is_valid():
        nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        lieu.disponibilite = "Disponible"
        lieu.save()
        form.save()
#        return render(request, 'blog/post_details.html',
#                   {'message': f"Le nouveau lieu est {nouveau_lieu} et l'ancien lieu est {lieu}, et l'animal est dans {animal.lieu} qui est maintenant {nouveau_lieu.disponibilite} ! {animal} est danns l'état {etat}"})

        if nouveau_lieu.disponibilite == "Disponible" :
            if nouveau_lieu.id_equip == 'Litière' :
                if etat == 'Endormi' :
                    animal.etat = "Affamé"
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                   'message': f"Super ! {animal.id_animal} a changé d'équipement ! Il est dans la litère"})
                else :
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                   'message': f"Super ! {animal.id_animal} a changé d'équipement ! Il est dans la litière"})
            elif nouveau_lieu.id_equip == "Mangeoire" :
                if etat == "Affamé" :
                    animal.etat = "Repus"
                    nouveau_lieu.disponibilite = "Occupé"
                    nouveau_lieu.save()
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                   'message': f"Super ! {animal.id_animal} a changé d'équipement ! Il dévore tout dans la mangeoire et est maintenant repus !"})
                else :
                    lieu.disponibilite = "Occupé"
                    lieu.save()
                    animal.lieu = lieu
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                    'message': f"Oh non ! {animal.id_animal} n'est pas affamé !"})
            elif nouveau_lieu.id_equip == "Nid" :
                if etat == "Fatigué" :
                    animal.etat = "Endormi"
                    nouveau_lieu.disponibilite = "Occupé"
                    nouveau_lieu.save()
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                   'message': f"Super ! {animal.id_animal} a changé d'équipement ! Il est maintenant endormi dans le nid !"})
                else:
                    lieu.disponibilite = "Occupé"
                    lieu.save()
                    animal.lieu = lieu
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                      'message': f"Oh non ! {animal.id_animal} n'est pas fatigué !"})
            elif nouveau_lieu.id_equip == "Roue" :
                if etat == "Repus" :
                    animal.etat = "Fatigué"
                    nouveau_lieu.disponibilite = "Occupé"
                    nouveau_lieu.save()
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                   'message': f"Super ! {animal.id_animal} a changé d'équipement ! Il se défoule dans la roue et est maintenant fatigué !"})
                else:
                    lieu.disponibilite = "Occupé"
                    lieu.save()
                    animal.lieu = lieu
                    animal.save()
                    return render(request, 'blog/post_details.html',
                                  {'animal': animal, 'form': form, 'etat': etat, 'animaux': animaux,
                                      'message': f"Oh non ! {animal.id_animal} n'est pas repus !"})
        else :
            if lieu.id_equip != "Litière" :
                lieu.disponibilite = "Occupé"
                lieu.save()
                animal.lieu = lieu
                animal.save()
            return render(request, 'blog/post_details.html',
                          {'animal': animal, 'lieu' : lieu, 'form' : form,'animaux': animaux, 'etat':etat, 'message': f"Oh non ! Cet équipement n'est pas disponible !"})
    else:
        form = MoveForm()
        return render(request,
                  'blog/post_details.html',
                  {'animal': animal, 'lieu' : lieu, 'form' : form, 'etat':etat, 'animaux': animaux,})
