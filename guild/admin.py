from django.contrib import admin
from .models import Event, GuildLeader, Campaign, Member, GuildActivity, Review

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Enable search by title and description
    list_filter = ('date',)  # Add filtering by date

@admin.register(GuildLeader)
class GuildLeaderAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'description')  # Fields to display in the admin list view
    search_fields = ('name', 'title')  # Enable search by name and title

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'description')  # Fields to display in the admin list view
    search_fields = ('title', 'description')  # Enable search by title and description
    list_filter = ('date',)  # Add filtering by date

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'joined_date')  # Fields to display in the admin list view
    search_fields = ('name', 'email')  # Enable search by name and email
    list_filter = ('joined_date',)  # Add filtering by joined date

@admin.register(GuildActivity)
class GuildActivityAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'event')  # Fields to display in the admin list view
    search_fields = ('name', 'description')  # Enable search by name and description
    list_filter = ('date', 'event')  # Add filtering by date and event

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'content')  # Fields to display in the admin list view
    search_fields = ('user__username', 'content')  # Enable search by username and content
    list_filter = ('created_at',)  # Add filtering by creation date
