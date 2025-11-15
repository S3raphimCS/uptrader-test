from django.contrib import admin

from server.apps.menu.help_texts import MENU_HELPTEXT, MENUITEM_HELPTEXT
from server.apps.menu.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)
    fieldsets = (
        (
            None,
            {
                "fields": ("name",),
                "description": MENU_HELPTEXT
            }
        ),
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu', 'parent', 'url', 'named_url')
    list_filter = ('menu',)
    search_fields = ('name',)
    fieldsets = (
        (
            None,
            {
                "fields": ("name", "menu", "parent", "url", "named_url",),
                "description": MENUITEM_HELPTEXT
            }
        ),
    )

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """
        Переопределяем этот метод, чтобы отфильтровать список родителей.
        Теперь в списке родителей будут только пункты из текущего меню.
        """
        if db_field.name == 'parent':
            object_id = request.resolver_match.kwargs.get('object_id')

            if object_id:
                try:
                    current_item_menu = MenuItem.objects.get(pk=object_id).menu
                    kwargs['queryset'] = MenuItem.objects.filter(
                        menu=current_item_menu
                    ).exclude(pk=object_id)
                except MenuItem.DoesNotExist:
                    pass

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
