from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from rango.models import Bares, Tapas
from rango.forms import BaresForm, TapasForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def index(request):
    
    bares_list = Bares.objects.order_by('-likes')[:5]
    tapas_list = Tapas.objects.order_by('-views')[:5]

    context_dict = {'baress': bares_list, 'tapas': tapas_list}

    return render(request, 'rango/index.html', context_dict)


def bares(request, bares_name_slug):

    context_dict = {}

    try:
        
        bares = Bares.objects.get(slug=bares_name_slug)
        context_dict['bares_name'] = bares.name

        tapas = Tapas.objects.filter(bares=bares)

        context_dict['tapas'] = tapas
        context_dict['bares'] = bares

	bares.views += 1
	bares.save()

    except Bares.DoesNotExist:
        pass

    return render(request, 'rango/bares.html', context_dict)


def add_bares(request):
    if request.method == 'POST':
        form = BaresForm(request.POST)


        if form.is_valid():

            form.save(commit=True)

            return index(request)
        else:

            print form.errors
    else:

        form = BaresForm()

    return render(request, 'rango/add_bares.html', {'form': form})


def add_tapas(request, bares_name_slug):

    try:
        bar = Bares.objects.get(slug=bares_name_slug)
    except Bares.DoesNotExist:
        bar = None

    if request.method == 'POST':
        form = TapasForm(request.POST)
        if form.is_valid():
            if bar:
                tapas = form.save(commit=False)
                tapas.bares = bar
                tapas.views = 0
                tapas.save()

                return bares(request, bares_name_slug)
        else:
            print form.errors
    else:
        form = TapasForm()

    context_dict = {'form':form, 'bares':bar}

    return render(request, 'rango/add_tapas.html', context_dict)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True

        else:
            print user_form.errors, profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/register.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered} )


def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:            
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'rango/login.html', {})


@login_required
def restricted(request):
    return HttpResponse("Tienes que estar logueado para ver esto")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')

@login_required
def like_bares(request):

    bar_id = None
    if request.method == 'GET':
        bar_id = request.GET['bares_id']

    likes = 0
    if bar_id:
        bar = Bares.objects.get(id=int(bar_id))
        if bar:
            likes = bar.likes + 1
            bar.likes =  likes
            bar.save()

    return HttpResponse(likes)



def reclama_datos (request):

	bares = Bares.objects.all()
	datos = []

	for bar in bares:
		datos.append({'name': bar.name, 'data':[bar.views]})



	return JsonResponse(datos, safe=False)


def about(request):
    context_dict = {'boldmessage': "Rango says here is the about page."}

    return render(request, 'rango/about.html', context_dict)

