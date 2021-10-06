from django.contrib import admin
from app.models import Character, Pirate, Insult

class CharacterAdmin(admin.ModelAdmin):
    pass

class PirateAdmin(admin.ModelAdmin):
    pass

class InsultAdmin(admin.ModelAdmin):
    pass

admin.site.register(Character, CharacterAdmin)
admin.site.register(Pirate, PirateAdmin)
admin.site.register(Insult, InsultAdmin)