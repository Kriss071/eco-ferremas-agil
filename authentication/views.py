from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *



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