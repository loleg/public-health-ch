# -*- coding: utf-8 -*-

from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)

from .models import Entry, Stream
from .models.admin import ExportModelAdminMixin

class EntryModelAdmin(ModelAdmin):
    model = Entry
    menu_icon = 'date'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = True
    list_display = ('published', 'title', 'author', 'tags')
    list_filter = ('author', 'tags')
    search_fields = ('title', 'author', 'content', 'tags')

modeladmin_register(EntryModelAdmin)

class StreamModelAdmin(ModelAdmin):
    model = Stream
    menu_icon = 'date'
    menu_order = 1000
    add_to_settings_menu = True
    exclude_from_explorer = True
    list_display = ('title', 'ident')

modeladmin_register(StreamModelAdmin)

class EntryModelAdmin(ExportModelAdminMixin, ModelAdmin):
    model = Entry
    index_template_name = 'templates/modeladmin/feedler/entry/index.html'

modeladmin_register(EntryModelAdmin)
