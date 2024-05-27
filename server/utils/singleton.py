from django.db import models

from django.core.exceptions import ValidationError


class SingletonModel(models.Model):
    """
    Абстрактная база данных для синглтон-моделей.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and self.__class__.objects.exists():
            raise ValidationError(f"Невозможно создать больше одного экземпляра {self.__class__.__name__}.")
        return super().save(*args, **kwargs)
