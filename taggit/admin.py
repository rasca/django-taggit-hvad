from __future__ import unicode_literals

from django.contrib import admin

from hvad.admin import TranslatableAdmin
from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem


class TagAdmin(TranslatableAdmin):
    inlines = [
        TaggedItemInline
    ]
    list_display = ["slug", "all_translations"]
    ordering = ["slug"]
    search_fields = ["name"]


admin.site.register(Tag, TagAdmin)
