from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    entity_name = models.CharField(blank=True, verbose_name="Имя юр. лица", max_length=100)
    PERSON_CHOICES = (
        ('entity', 'Юридическое лицо'),
        ('individual', 'Физическое лицо'),
    )
    ROLE_CHOICES = (
        ('custome', 'Заявитель'),
        ('contractor', 'Подрядчик'),
        ('staff', 'Сотрудник')
    )
    person = models.CharField(choices=PERSON_CHOICES, max_length=10, blank=True, verbose_name='Категория')
    role = models.CharField(choices=ROLE_CHOICES, max_length=10, blank=True, verbose_name='Участник')

    approved = models.BooleanField(
        default=False,
        verbose_name='Подтверждённый пользователь',
        )

    permission = models.FileField(
        blank=True,
        verbose_name='Разрешения для работы',
        upload_to='uploads/user/%d/%m/%Y/permission/'
        )
    staff = models.FileField(
        blank=True,
        verbose_name='Персонал',
        upload_to='uploads/user/%d/%m/%Y/staff/'
        )
    equip = models.FileField(
        blank=True,
        verbose_name='Техника',
        upload_to='uploads/user/%d/%m/%Y/equip/'
        )
    exp = models.FileField(
        blank=True,
        verbose_name='Опыт работы',
        upload_to='uploads/user/%d/%m/%Y/exp/'
        )
    reviews = models.FileField(
        blank=True,
        verbose_name='Отзывы и рекомендации',
        upload_to='uploads/user/%d/%m/%Y/reviews/'
        )

    def __str__(self):
        """
        Если это юр. лицо, то возвращаем название его предприятия, либо имя руководителя
        """
        if self.person == 'entity':
            return self.entity_name or self.get_full_name()
        else:
            return self.get_full_name()
