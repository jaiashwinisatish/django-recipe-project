from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def receipes(request):

    if request.method == 'POST':
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        Recipe_name = data.get('receipe_name')
        Recipe_description = data.get('receipe_description')

        Recipe.objects.create(
            Recipe_name=Recipe_name,
            Recipe_description=Recipe_description,
            Recipe_image=receipe_image
        )

        return redirect('/receipes/')

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(Recipe_name__icontains=request.GET.get('search'))

    context = {'receipes': queryset}
    return render(request, 'receipes.html', context)

def update_receipe(request, id):
    queryset = Recipe.objects.filter(id=id)

    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get('receipe_image')
        Recipe_name = data.get('receipe_name')
        Recipe_description = data.get('receipe_description')

        queryset.Recipe_name = Recipe_name
        queryset.Recipe_description = Recipe_description

        if  receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()
        return redirect('/receipes/')    


    context = {'receipe': queryset}
    return render(request, 'update_receipe.html', context)



def delete_receipe(request, id):
    queryset = Recipe.objects.filter(id=id)
    queryset.delete()
    return redirect('/receipes/')