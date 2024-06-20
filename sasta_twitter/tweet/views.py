from django.shortcuts import render
from .models import Tweet
from .forms import TweetForm
from django.shortcuts import get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at') # here - negative means descending 
    return render(request, 'tweet_list.html', {'tweets':tweets})

def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES) #when we have files, we add this second argument.
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets_all') #a view method above
    else:
        form = TweetForm()
    return render(request, 'tweet_form.html', {'form':form})

def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)   #pk means primary key 
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweets_all')
    else:
        form = TweetForm(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})

def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user) 
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweets_all')
    return render(request, 'tweet_confirm_delete.html', {'tweet':tweet})