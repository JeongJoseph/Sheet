from django.contrib import admin
from sheets.models import Person

class PersonAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person,PersonAdmin)

