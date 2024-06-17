from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import *
from store import models



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

def delete_category(request, id_category):
    category = get_object_or_404(models.Category, pk=id_category)
    category.delete()
    return redirect(profile_category)