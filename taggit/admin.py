from django.contrib import admin

from hvad.admin import TranslatableAdmin
from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem

class TagAdmin(TranslatableAdmin):
    list_display = ('__unicode__', 'all_translations', )
    inlines = [
        TaggedItemInline
    ]


admin.site.register(Tag, TagAdmin)
