from django.contrib import admin
from .models import Farmer,AgriExpert,AgriAssistant,States,Cities,Talukas
# Register your models here.

admin.site.register(Farmer)
admin.site.register(AgriExpert)
admin.site.register(AgriAssistant)
admin.site.register(States)
admin.site.register(Cities)
admin.site.register(Talukas)