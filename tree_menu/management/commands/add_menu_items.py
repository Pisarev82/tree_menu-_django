from django.core.management.base import BaseCommand
from tree_menu.models import MenuItem


class Command(BaseCommand):
    help = 'Не использовать в боевой БД, только для первоначального заполнения'

    def handle(self, *args, **options):

        MenuItem.objects.all().delete()

        menu_items = [
            # Главное меню
            MenuItem(
                id=1,
                name='Главная',
                url='/',
                menu_name='main_menu',
                order=1
            ),
            MenuItem(
                id=2,
                name='О нас',
                url='/about/',
                menu_name='main_menu',
                order=2
            ),
            MenuItem(
                id=3,
                name='Услуги',
                url='/services/',
                menu_name='main_menu',
                order=3
            ),
            MenuItem(
                id=4,
                name='Веб-разработка',
                named_url='web_services',
                menu_name='main_menu',
                parent_id=3,  # Родитель - Услуги
                order=1
            ),
            MenuItem(
                id=5,
                name='Мобильная разработка',
                named_url='mobile_services',
                menu_name='main_menu',
                parent_id=3,  # Родитель - Услуги
                order=2
            ),
            MenuItem(
                id=6,
                name='Контакты',
                named_url='contact',
                menu_name='main_menu',
                order=4
            ),

            # Меню в футере
            MenuItem(
                id=7,
                name='Документы',
                url='/docs/',
                menu_name='footer_menu',
                order=1
            ),

            # Дополнительные пункты (пример вложенности 3 уровня)
            MenuItem(
                id=8,
                name='Frontend',
                named_url='frontend_services',
                menu_name='main_menu',
                parent_id=4,  # Родитель - Веб-разработка
                order=1
            ),
            MenuItem(
                id=9,
                name='Backend',
                named_url='backend_services',
                menu_name='main_menu',
                parent_id=4,  # Родитель - Веб-разработка
                order=2
            )
        ]

        MenuItem.objects.bulk_create(menu_items)

        self.stdout.write(
            self.style.SUCCESS(f'Успешно создано меню')
        )