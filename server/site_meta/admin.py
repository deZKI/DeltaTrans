from django.contrib import admin
from .models import AboutUs, AboutUsImage


class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 1


class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInline]


admin.site.register(AboutUs, AboutUsAdmin)
