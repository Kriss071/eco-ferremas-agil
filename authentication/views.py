from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from store import models
from .models import *



# Create your views here.

@login_required
def profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    
    context = {
        'form': form
    }
    
    return render(request, 'profile.html', context)

@staff_member_required
def profile_category(request):
    if request.method == 'POST':
        form = CategoriesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(profile_category)
    else:
        form = CategoriesForm()        
        categories = models.Category.objects.all()

        context = {
            'categories': categories,
            'form': form
        }
    
    return render(request, 'profile_categories.html', context)

@staff_member_required
def delete_category(request, id_category):
    category = get_object_or_404(models.Category, pk=id_category)
    category.delete()
    return redirect(profile_category)

@staff_member_required
def profile_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(profile_product)
    else:
        form = ProductForm()
        
        context = {
            'form': form
        }
        
    return render(request, 'profile_product.html', context)

def profile_directions(request):
    
    if request.method == 'POST':
        form = DirectionForm(request.POST)
        if form.is_valid():
            direction = form.save(commit=False)  
            direction.id_usuario = request.user  
            direction.save() 
            return redirect(profile_directions)
    else:
        form = DirectionForm()    
        
        directions = Directions.objects.all()
        
        context = {
            'directions': directions,
            'form': form
        }
    
    return render(request, 'profile_directions.html', context)