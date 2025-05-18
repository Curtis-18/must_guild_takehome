from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm, ReviewForm
from .models import Event, GuildLeader, Campaign, Member, GuildActivity, Review  # Added new models
from django.http import JsonResponse
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'guild/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'guild/login.html', {'form': form})

@login_required
def home_view(request):
    leaders = GuildLeader.objects.all()
    members = Member.objects.all()  # Ensure this query returns valid data
    return render(request, 'guild/home.html', {
        'leaders': leaders,
        'members': members  # Pass members to the template
    })

@login_required
def events_view(request):
    leaders = GuildLeader.objects.all()
    return render(request, 'guild/events.html', {
        'events': Event.objects.all(),
        'campaigns': Campaign.objects.all(),
        'activities': [],
        'leaders': leaders
    })

@login_required
def about_view(request):
    guild_info = GuildLeader.objects.first()
    return render(request, 'guild/about.html', {
        'guild_info': guild_info
    })

@login_required
def get_involved_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                user=request.user,
                content=form.cleaned_data['content'],
                created_at=form.cleaned_data.get('created_at', None)  # Optional
            )
            messages.success(request, "Your review has been submitted!")
            return redirect('get_involved')
        else:
            messages.error(request, "There was an error with your submission.")
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'guild/get_involved.html', {
        'form': form,
        'reviews': reviews
    })

def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review.objects.create(
                user=request.user,
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                rating=form.cleaned_data['rating']
            )
            return JsonResponse({
                'user': {'username': review.user.username},
                'content': review.content,
                'created_at': review.created_at.strftime('%B %d, %Y, %I:%M %p'),
            })
    return JsonResponse({'error': 'Invalid form submission'}, status=400)