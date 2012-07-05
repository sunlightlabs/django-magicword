from django.contrib import admin
from magicword.models import MagicWord


class MagicWordAdmin(admin.ModelAdmin):
    list_display = ('password', 'is_enabled')
    list_editable = ('is_enabled',)

admin.site.register(MagicWord, MagicWordAdmin)
