from django.contrib import admin

from portfolio.models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'slug', 'technology')
    list_filter = "technology",
    search_fields = ['title', 'description', 'slug', 'technology']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Project, ProjectAdmin)
