from django.contrib import admin

from bulletins.models import Bulletin


# Register your models here.
class BulletinAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description", "price", "hashtags")


admin.site.register(Bulletin, BulletinAdmin)
