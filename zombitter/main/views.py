from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.views.decorators.cache import cache_page
from django.template import RequestContext
from main.models import Twitt, Zombie
from main.forms import TwittForm, ZombieForm


@cache_page(60 * 15)
def home(request):
    twitts = Twitt.objects.all()
    return render_to_response('home.html', {
        'twitts': twitts,
    })


@cache_page(60 * 15)
def show_zombie(request, pk):
    zombie = Zombie.objects.get(pk=pk)
    twitts = Twitt.objects.filter(zombie=pk)
    return render_to_response('show_zombie.html', {
        'zombie': zombie, 'twitts': twitts,
    })


def show_twitt(request, pk):
    twitt = Twitt.objects.get(pk=pk)
    return render_to_response('show_twitt.html', {
        'twitt': twitt,
    })


def add_twitt(request):
    form = TwittForm()
    if request.method == 'POST':
        form = TwittForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_twitt.html', {
        'form': form,
    }, RequestContext(request))


def edit_twitt(request, pk):
    twitt = get_object_or_404(Twitt, pk=pk)
    form = TwittForm(instance=twitt)
    if request.method == 'POST':
        form = TwittForm(request.POST, instance=twitt)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_twitt.html', {
        'form': form,
        }, RequestContext(request))


def delete_twitt(request, pk):
    Twitt.objects.filter(pk=pk).delete()
    return redirect('home')


def add_zombie(request):
    form = ZombieForm()
    if request.method == 'POST':
        form = ZombieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
    }, RequestContext(request))


def edit_zombie(request, pk):
    zombie = get_object_or_404(Zombie, pk=pk)
    form = ZombieForm(instance=zombie)
    if request.method == 'POST':
        form = ZombieForm(request.POST, instance=zombie)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render_to_response('add_zombie.html', {
        'form': form,
        }, RequestContext(request))


def delete_zombie(request, pk):
    Zombie.objects.filter(pk=pk).delete()
    return redirect('home')
