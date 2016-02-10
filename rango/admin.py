from django.contrib import admin
from rango.models import Bares, Tapas
from rango.models import UserProfile

class BaresAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class TapasAdmin(admin.ModelAdmin):
    list_display = ('title', 'bares', 'url')

admin.site.register(Bares, BaresAdmin)
admin.site.register(Tapas, TapasAdmin)
admin.site.register(UserProfile)
