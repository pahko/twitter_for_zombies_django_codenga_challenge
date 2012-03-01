from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from main.models import Tweet, Zombie
from main.forms import ZombieForm


def home(request):
    tweets = Tweet.objects.all()
    return render_to_response('index.html', {
        'tweets': tweets
    }, RequestContext(request))


def zombie_tweets(request, zombie_name):
    zombie = get_object_or_404(Zombie, name=zombie_name)
    return render_to_response('tweets_zombies.html', {
        'tweets': zombie.tweets
    }, RequestContext(request))


def tweet(request, id_tweet):
    tweet = get_object_or_404(Tweet, pk=id_tweet)
    return render_to_response('tweet.html', {
        'tweet': tweet
    }, RequestContext(request))


def crud(request):
    zombies = Zombie.objects.all()
    return render_to_response('zombies.html', {
        'zombies': zombies
    }, RequestContext(request))


def delete_zombie(request, zombie_id):
    zombie = get_object_or_404(Zombie, pk=zombie_id)
    zombie.delete()
    return redirect('crud')


def edit_zombie(request, zombie_id):
    zombie = get_object_or_404(Zombie, pk=zombie_id)
    zombie_form = ZombieForm(instance=zombie)
    if request.method == 'POST':
        zombie_form = ZombieForm(request.POST, instance=zombie)
        if zombie_form.is_valid():
            zombie_form.save()
    return render_to_response('edit.html', {
        'zombie': zombie,
        'zombie_form': zombie_form
    }, RequestContext(request))


def add_new(request):
    zombie_form = ZombieForm()
    if request.method == 'POST':
        zombie_form = ZombieForm(request.POST)
        if zombie_form.is_valid():
            zombie_form.save()
            return redirect('crud')
    return render_to_response('edit.html', {
        'zombie_form': zombie_form
    }, RequestContext(request))
