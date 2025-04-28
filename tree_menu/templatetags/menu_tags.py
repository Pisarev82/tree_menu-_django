from django import template
from django.urls import resolve
from django.utils.safestring import mark_safe
from ..models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_url = request.path_info

    try:
        resolved_url = resolve(current_url)
        current_named_url = resolved_url.url_name
    except:
        current_named_url = None

    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')

    def build_menu_tree(items, parent=None) -> list:
        tree = []
        for item in items:
            if item.parent == parent:
                # Для себя, что бы легче читать код
                # РЕКУРСИЯ
                children = build_menu_tree(items, item)

                item_url = item.get_url()

                # Находим активный пункт меню на основе имени URL или URL
                if current_named_url and item.named_url:
                    is_active = current_named_url == item.named_url
                else:
                    is_active = current_url == item_url

                # Прокидываем родителю флаг активности, если у него активный дочерний пункт
                if not is_active and children:
                    is_active = any(child['is_active'] for child in children)

                tree.append({
                    'item': item,
                    'children': children,
                    'is_active': is_active,
                    'url': item_url
                })
        return tree

    menu_tree = build_menu_tree(menu_items)

    # Вынес построение HTML в отдельную функцию, чтобы была возможность сделать
    # разные представления, на пример другие требования у бокового меню, нижнего и тд.
    def render_menu(items: list):
        result = '<ul>'
        for item in items:
            active_class = ' active' if item['is_active'] else ''
            result += f'<li class="menu-item{active_class}">'
            result += f'<a href="{item["url"]}">{item["item"].name}</a>'

            if item['is_active'] and item['children']:
                # РЕКУРСИЯ
                result += render_menu(item['children'])

            result += '</li>'
        return result + '</ul>'

    return mark_safe(render_menu(menu_tree))