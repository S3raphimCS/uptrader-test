from django import template

from server.apps.menu.models import MenuItem


register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = request.path

    # Шаг 1: Выполняем ровно один запрос к БД
    menu_items_qs = MenuItem.objects.filter(menu__name=menu_name).select_related('parent')

    # Шаг 2: Преобразуем QuerySet в структуры, удобные для обработки в Python
    items_by_id = {item.id: item for item in menu_items_qs}
    root_items = []
    active_item = None

    for item in menu_items_qs:
        # Добавляем каждому объекту атрибут для хранения дочерних элементов
        item.children_list = []

        # Находим активный пункт
        if not active_item and item.get_url() == current_path:
            active_item = item

        # Строим дерево
        if item.parent_id:
            parent = items_by_id.get(item.parent_id)
            if parent:
                parent.children_list.append(item)
        else:
            root_items.append(item)

    # Шаг 3: Определяем ID всех активных элементов (выбранный и все его родители)
    active_branch_ids = set()
    if active_item:
        active_branch_ids.add(active_item.id)
        parent = active_item.parent
        while parent:
            active_branch_ids.add(parent.id)
            parent = parent.parent

    return {
        'menu_items': root_items,
        'active_branch_ids': active_branch_ids,
    }
