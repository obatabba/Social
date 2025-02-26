from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseForbidden, HttpResponseNotAllowed, JsonResponse

from .models import Tweet, Profile
from .forms import TweetForm, ProfileEditForm, ProfilePicForm, RegistrationForm


class CustomLogoutView(LogoutView):
    next_page = 'home'
    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)
    

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    return render(request, 'registration/register.html', {'form': form})
    

def home(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    form = None
    if request.user.is_authenticated:
        form = TweetForm()
        
        if request.method == 'POST':
            form = TweetForm(request.POST, request.FILES)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()
                messages.success(request, 'Your tweet has been posted!')
                return redirect('home')
        
    return render(request, 'home.html', {'tweets': tweets, 'form': form})


@login_required()
def profile(request, id):
    profile= get_object_or_404(Profile, user_id=id)
    tweets = Tweet.objects.filter(user_id=id).order_by("-created_at")

    if request.method == 'POST':
        action = request.POST['action']
        if action == 'follow':
            request.user.profile.follows.add(profile)
        elif action == 'unfollow':
            request.user.profile.follows.remove(profile)
        request.user.save()

    return render(request, 'profile.html', {'profile': profile, 'tweets': tweets})


@login_required()
def edit_profile(request):
    user_profile = Profile.objects.get(user__id=request.user.id)

    if request.method == 'POST':
        profile_form = ProfileEditForm(
            request.POST, request.FILES, instance=request.user)
        
        profile_pic_form = ProfilePicForm(
            request.POST, request.FILES, instance=user_profile)

        if profile_form.is_valid() and profile_pic_form.is_valid():
            profile_form.save()
            profile_pic_form.save()
            messages.success(request, 'Your profile has been updated.')
    else:
        profile_form = ProfileEditForm(instance=request.user)
        profile_pic_form = ProfilePicForm(instance=user_profile) 

    return render(request, 'edit_profile.html',
        context={'form': profile_form, 'picture_form': profile_pic_form}
    )


@login_required()
def followers(request, user_id):
    if Profile.objects.filter(user_id=user_id).exists():
        followers = Profile.objects.filter(follows=user_id).exclude(user_id=user_id)
        return render(request, 'profile_list.html', {'profiles': followers})
    else:
        messages.success(request, 'Profile was not found :(')
        return redirect('home')
    

@login_required()
def follows(request, user_id):
    if Profile.objects.filter(user_id=user_id).exists():
        followers = Profile.objects.filter(followed_by=user_id).exclude(user_id=user_id)
        return render(request, 'profile_list.html', {'profiles': followers})
    else:
        messages.success(request, 'Profile was not found :(')
        return redirect('home')
    

@login_required()
def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)

    return render(request, 'profile_list.html', {'profiles': profiles})


def tweet_like(request, tweet_id):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.method == 'POST':
        if tweet.likes.filter(id=request.user.id).exists():
            tweet.likes.remove(request.user)
            value = 'unlike'
        else:
            tweet.likes.add(request.user)
            value = 'like'

        data = {
            'action': value,
            'likes': tweet.likes_count()
        }
        return JsonResponse(data, safe=False)
    
    return redirect('home')


@login_required()
def delete_tweet(request, tweet_id):
    if request.method == 'DELETE':
        tweet = get_object_or_404(Tweet, id=tweet_id)
        if request.user == tweet.user:
            tweet.delete()
            return JsonResponse({'message': 'Tweet deleted successfully.' }, status=200)
        else:
            return HttpResponseForbidden()
    return HttpResponseNotAllowed(['DELETE'])


@login_required()
def edit_tweet(request, tweet_id):
    if request.method == 'POST':
        tweet = get_object_or_404(Tweet, id=tweet_id)
        if request.user == tweet.user:
            form = TweetForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data['body']
                tweet.body = data
                tweet.save()
                return JsonResponse(
                    {'modified_tweet': tweet.body, 'message': 'Tweet edited successfully.' })
        else:
            return JsonResponse({'error': 'Not allowed.'}, status=403)
    return HttpResponseNotAllowed(['POST',])
