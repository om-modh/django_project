from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)    
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been created! You can now Log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required 
def profile(request):
    return render(request, 'users/profile.html')


# messages.debug
# messages.info
# messages.success
# messages.warning    
# messages.error