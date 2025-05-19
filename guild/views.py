from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.contrib import messages
from .forms import SignupForm, LoginForm, ReviewForm, VolunteerRequestForm
from .models import Event, GuildLeader, Campaign, Member, GuildActivity, Review, VolunteerRequest
from django.db.models import Q
from django.urls import reverse
from django.views.decorators.http import require_POST

def signup_view(request):
    try:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Account created successfully!")
                return redirect('home')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = SignupForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
    return render(request, 'guild/signup.html', {'form': form})

def login_view(request):
    try:
        if request.method == 'POST':
            form = LoginForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            form = LoginForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
    return render(request, 'guild/login.html', {'form': form})

@login_required
def home_view(request):
    try:
        leaders = GuildLeader.objects.all()
        members = Member.objects.all()
    except Exception as e:
        messages.error(request, f"An error occurred while loading data: {e}")
        leaders, members = [], []
    return render(request, 'guild/home.html', {'leaders': leaders, 'members': members})

@login_required
def events_view(request):
    try:
        events = Event.objects.all()
        campaigns = Campaign.objects.all()
    except Exception as e:
        messages.error(request, f"An error occurred while loading events: {e}")
        events, campaigns = [], []
    return render(request, 'guild/events.html', {'events': events, 'campaigns': campaigns})

@login_required
def about_view(request):
    try:
        guild_info = GuildLeader.objects.first()
    except Exception as e:
        messages.error(request, f"An error occurred while loading guild information: {e}")
        guild_info = None
    return render(request, 'guild/about.html', {'guild_info': guild_info})

@login_required
def get_involved_view(request):
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                Review.objects.create(
                    user=request.user,
                    content=form.cleaned_data['content']
                )
                messages.success(request, "Your review has been submitted!")
                return redirect('get_involved')
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = ReviewForm()
        reviews = Review.objects.all().order_by('-created_at')
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        reviews = []
    return render(request, 'guild/get_involved.html', {'form': form, 'reviews': reviews})

def submit_review(request):
    try:
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = Review.objects.create(
                    user=request.user,
                    content=form.cleaned_data['content']
                )
                return JsonResponse({
                    'user': {'username': review.user.username},
                    'content': review.content,
                    'created_at': review.created_at.strftime('%B %d, %Y, %I:%M %p'),
                })
            else:
                return JsonResponse({'error': 'Invalid form submission'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f"An error occurred: {e}"}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

def search_view(request):
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        # Search across multiple models and fields
        event_results = Event.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        leader_results = GuildLeader.objects.filter(Q(name__icontains=query) | Q(title__icontains=query) | Q(description__icontains=query))
        campaign_results = Campaign.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        member_results = Member.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
        activity_results = GuildActivity.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        # Combine results into a single list with a type label
        results = list(event_results) + list(leader_results) + list(campaign_results) + list(member_results) + list(activity_results)
    return render(request, 'guild/search_results.html', {'results': results, 'query': query})

@login_required
def dashboard_view(request):
    context = {
        'event_count': Event.objects.count(),
        'campaign_count': Campaign.objects.count(),
        'member_count': Member.objects.count(),
        'review_count': Review.objects.count(),
        'activity_count': GuildActivity.objects.count(),
    }
    return render(request, 'guild/dashboard.html', context)

@login_required
@require_POST
def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    user = request.user
    if user in review.likes.all():
        review.likes.remove(user)
    else:
        review.likes.add(user)
    return redirect('get_involved')

@login_required
def volunteer_view(request):
    user = request.user
    if request.method == 'POST':
        form = VolunteerRequestForm(request.POST)
        if form.is_valid():
            VolunteerRequest.objects.create(
                user=user,
                message=form.cleaned_data['message'],
                status='pending'
            )
            messages.success(request, 'Your volunteer request has been submitted!')
            return redirect('volunteer')
    else:
        form = VolunteerRequestForm()
    requests = VolunteerRequest.objects.filter(user=user).order_by('-created_at')
    return render(request, 'guild/volunteer.html', {'form': form, 'requests': requests})
