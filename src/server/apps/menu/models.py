from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """Модель меню."""
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Название меню'
    )

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """Модель пунктов меню."""
    name = models.CharField(
        max_length=100,
        verbose_name='Название пункта'
    )
    menu = models.ForeignKey(
        Menu,
        related_name='items',
        on_delete=models.CASCADE,
        verbose_name='Меню'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Родительский пункт'
    )
    url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Прямой URL'
    )
    named_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Named URL'
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ('pk',)

    def get_url(self):
        """Возвращает URL для пункта меню."""
        if self.named_url:
            try:
                return reverse(self.named_url)
            except Exception:
                # В случае ошибки возвращаем заглушку, чтобы не ломать сайт
                return '#'
        return self.url if self.url else '#'

    def clean(self):
        """Кастомная логика валидации:
        1) Проверка, что заполнено только одно из полей URL.
        2) Проверка, что родитель принадлежит тому же меню
        """

        super().clean()

        if self.url and self.named_url:
            raise ValidationError('Пожалуйста, заполните только одно из полей: "Прямой URL" или "Named URL".')

        if not self.menu_id:
            raise ValidationError({"menu": "Поле не может быть пустым."})

        if self.parent and self.parent.menu != self.menu:
            raise ValidationError(
                {
                    'parent': 'Выбранный родительский пункт принадлежит другому меню. '
                              'Пожалуйста, выберите родителя из этого же меню.'
                }
            )

    def __str__(self):
        return self.name
