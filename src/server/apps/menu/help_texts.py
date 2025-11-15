from django.utils.safestring import mark_safe


MENU_HELPTEXT = "Название - это название меню, которое используется в коде. Реализованы 'main_menu' и 'footer_menu'."
MENUITEM_HELPTEXT = mark_safe("""
Родительский пункт не может быть выбран из другого меню и наоборот.<br>
Прямой URL и Named URL не могут быть заполнены одновременно.
Может быть указано что-то одно или ничего.<br>
Реализованные в коде named url:  <b>home, about_page, portfolio, project_1, project_2, contacts, terms-of-service, privacy_policy</b>.<br>
Реализованные в коде прямые url: <b>/, /about/, /portfolio/, /portfolio/project-1/, /portfolio/project-2/, /contacts/, /terms-of-service/, /privacy-policy/</b>.
""")
