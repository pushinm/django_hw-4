from django.contrib import admin
from .models import Clinic
""" from .models import Article

# Register your models here.

class AdminArticle(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content',)
    list_display_links = ('pk',)
    list_editable = ('title', )
    list_filter = ('title',)
    search_fields =  ('pk', 'title', 'content',)

admin.site.register(Article, AdminArticle) """
admin.site.register(Clinic)