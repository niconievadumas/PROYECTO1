from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate    
# Create your views here.

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid:
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
        
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(username, password)
                
    
    form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})
    
