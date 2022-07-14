from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as dj_login
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
        
            user = authenticate(username=username, password=password)
            
            if user is not None:
                dj_login(request, user)  #no es la funcion este login
                # redirect('index')
                return render(request, 'index.html')
            else:
                return render(request, 'accounts/login.html', {'form': form})
            
        else:
            return render(request, 'accounts/login.html', {'form': form})
            
                
    
    form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    
    return render(request, 'accounts/register.html', {'form': ''})
    
    
