from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def aboutus(request):
    return render(request,'General/aboutUs.html')

def loginView(request):
    if request.method == "GET":
        return render(request,'General/login.html',{})
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user is not None :
            login(request,user)
            return render(request, 'Mainmenu/mainmenu.html', {})
        else:
            return render(request,'General/login.html',{})

def logout_view(request):
    logout(request)
    return render(request,"General/logout.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            #user = authenticate(username=username, password=raw_password)
            login(request, user)
            return render(request,"home.html")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
            return render(request=request,template_name='General/signup.html',context={"form":form})
    else:
        form = UserCreationForm()
        return render(request, 'General/signup.html', {'form': form})

def mainmenu(request):
    return render(request,'Mainmenu/mainmenu.html')