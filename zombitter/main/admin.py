from django.contrib import admin
from main.models import Zombie, Twitt


class ZombieAdmin(admin.ModelAdmin):
    list_display = ('name', 'graveyard',)
    search_fields = ('name', 'graveyard',)


class TwittAdmin(admin.ModelAdmin):
    list_display = ('status', 'zombie', 'created_at',)
    search_fields = ('status', 'zombie',)

admin.site.register(Zombie, ZombieAdmin)
admin.site.register(Twitt, TwittAdmin)
