from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Client, Restaurant, Reserve, client, restaurant
from django.template import loader

def dinespotapp(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def restaurant(request):
    template = loader.get_template('restaurant.html')
    return HttpResponse(template.render())

def reservations(request):
    template = loader.get_template('reservations.html')
    return HttpResponse(template.render())

def business(request):
    template = loader.get_template('business.html')
    return HttpResponse(template.render())

@login_required(login_url='signinRestaurant')
def infoRestaurant(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Restaurant.objects.get(user=user_object)
    return render(request, 'infoRestaurant.html', {'user_profile':user_profile})

@login_required(login_url='signinClient')
def infoClient(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Client.objects.get(user=user_object)
    return render(request, 'infoClient.html', {'user_profile':user_profile})

@login_required(login_url='signinClient')
def settingsClient(request):
    client_profile = Client.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST['f_name']
        last_name = request.POST['l_name']
        tel = request.POST['tel']
        mail = request.POST['mail']

        client_profile.name = name
        client_profile.last_name = last_name
        client_profile.tel = tel
        client_profile.mail = mail
        client_profile.save()

        return redirect('settingsClient')
    return render(request, 'settingsClient.html', {'client_profile': client_profile})

@login_required(login_url='signinRestaurant')
def settingsRestaurant(request):
    restaurant_profile = Restaurant.objects.get(user=request.user)
    if request.method == 'POST':
        image = restaurant_profile.profileimg
        name = request.POST['name']
        description = request.POST['description']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        p_code = request.POST['p_code']
        colony = request.POST['colony']
        street = request.POST['street']
        num_ext = request.POST['num_ext']
        num_int = request.POST['num_int']
        max_cap = request.POST['max_cap']

        restaurant_profile.profileimg = image
        restaurant_profile.name = name
        restaurant_profile.description = description
        restaurant_profile.country = country
        restaurant_profile.state = state
        restaurant_profile.city = city
        restaurant_profile.p_code = p_code
        restaurant_profile.colony = colony
        restaurant_profile.street = street
        restaurant_profile.num_ext = num_ext
        restaurant_profile.num_int = num_int
        restaurant_profile.max_cap = max_cap
        restaurant_profile.save()
        return redirect('settingsRestaurant')
    return render(request, 'settingsRestaurant.html', {'restaurant_profile': restaurant_profile})

def signupClient(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        
        if password == password2: 
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signupClient')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signupClient')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Client.objects.create(user=user_model, client_id=user_model.id)
                new_profile.save()
                
                return redirect('infoClient')
        else:
            messages.info(request, "Password Not Matching")
            return redirect('signupClient')
    else: return render(request, 'signupClient.html')

def signupRestaurant(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signupRestaurant')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signupRestaurant')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Restaurant.objects.create(user=user_model, rest_id=user_model.id)
                new_profile.save()

                return redirect('infoRestaurant')
        else: 
            messages.info(request, "Password Not Matching")
            return redirect('signupRestaurant')
    else: return render(request, 'signupRestaurant.html')

def signinClient(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('infoClient')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signinClient')
    
    else: return render(request, 'signinClient.html')

def signinRestaurant(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('infoRestaurant')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signinRestaurant')
    
    else: return render(request, 'signinRestaurant.html')

@login_required(login_url='signinClient')
def logoutClient(request):
    auth.logout(request)
    return redirect('signinClient')

@login_required(login_url='signinRestaurant')
def logoutRestaurant(request):
    auth.logout(request)
    return redirect('signinRestaurant')