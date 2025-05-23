from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('events/', views.events_view, name='events'),
    path('about/', views.about_view, name='about'),
    path('get-involved/', views.get_involved_view, name='get_involved'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', LoginView.as_view(template_name='guild/login.html'), name='login'),
    path('search/', views.search_view, name='search'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('like-review/<int:review_id>/', views.like_review, name='like_review'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
]
