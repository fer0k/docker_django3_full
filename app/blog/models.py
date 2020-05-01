from django.db import models


class Post(models.Model):
    """
    Модель поста
        - name - заголовок
        - text - текстовое содержание
        - src - иллюстрация
        - updated_at - дата обновления файла
        - user - автор, раз уже
    """
    name = models.CharField(null=False, max_length=500)
    text = models.TextField(null=False, default='Текст блога')
    src = models.FileField(null=True, upload_to='posts/')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} at {self.created_at}'
