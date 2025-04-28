from django.db import models
from django.urls import reverse, NoReverseMatch
from django.utils.text import slugify

class MenuItem(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название пункта')
    named_url = models.CharField(
        max_length=100,
        blank=True,
        verbose_name='Именованный URL',
        help_text='Имя URL из urls.py. Если заполнено, поле "URL" будет игнорироваться.'
    )
    url = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='URL',
        help_text='URL для перехода. Можно оставить пустым для родительских пунктов.'
    )
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE,
        verbose_name='Родительский пункт'
    )
    menu_name = models.CharField(
        max_length=50,
        verbose_name='Имя меню',
        help_text='Название меню, к которому принадлежит пункт'
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name='Порядок сортировки'
    )

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.named_url
        return self.url or '#'

    def save(self, *args, **kwargs):
        if not self.url and not self.named_url:
            self.url = slugify(self.name)
        super().save(*args, **kwargs)