from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def register(request):
    if request.method == 'POST':
        Name = request.POST['Name'],
        Email = request.POST['Email'],
        Password = request.POST['Password'],

        user = User.objects.create_user(username=Name,Email=Email,Password=Password)
        user.save()
        print('user created')
        return redirect('/')
    else:    
        return render(request,'registration/registrate.html')
    