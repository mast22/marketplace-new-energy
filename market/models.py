from django.template.defaultfilters import slugify
from django.db import models
from users.models import CustomUser
from .constants import REGIONS_CHOICES

def get_image_filename(instance, filename):
    slug = slugify(instance.item.contract_id)
    return 'item_images/{}/{}'.format(slug, filename)

class Item(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Заявитель'
    )
    name = models.CharField('Краткое описание работ', max_length=100)
    extra_info = models.TextField('Дополнительная информация', blank=True)
    contract_id = models.CharField('Номер договора', max_length=20)
    contract_date = models.DateField('Дата договора')
    oriented_price = models.PositiveIntegerField(
        'Приблизительная стоимость работ',
        blank=True,
        null=True
    )
    date_added = models.DateTimeField('Дата добавления', auto_now_add=True)
    deadline = models.DateField('Конечный срок исполнения')
    locality = models.CharField('Населённый пункт', max_length=100)
    region = models.CharField(choices=REGIONS_CHOICES, max_length=2, verbose_name='Район')
    file = models.FileField('Тех. условия', blank=True)
    choosen_offer = models.IntegerField('ID Выбранного предложения', blank=True, null=True)
    power = models.PositiveIntegerField('Мощность', blank=True, null=True)

    def __str__(self):
        return f'{self.contract_id} от {self.contract_date}'


class Offer(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Подрядчик'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Работа',
        null=True
    )
    date_added = models.DateTimeField('Дата создания предложения', auto_now_add=True)
    price = models.IntegerField('Предлагаемая цена')
    desc = models.TextField('Описание работы подрядчика')
    review = models.TextField('Отзыв по сделаной работе', blank=True)
    contractor_review = models.TextField('Отчёт по сделаной работе', blank=True)
    raiting = models.PositiveIntegerField('Оценка сделанной работы', blank=True, null=True)
    work_done_custome = models.BooleanField('Заявитель завершение работы', default=False)
    work_done_contractor = models.BooleanField('Подрядчик завершение работы', default=False)

    def work_done(self):
        return self.work_done_custome and self.work_done_contractor



    def __str__(self):
        return f'{self.owner} - {self.price}'


class Images(models.Model):
    item = models.ForeignKey(
        Item,
        default=None,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Фото'
    )

class Material(models.Model):
    name = models.CharField('Название материала', max_length=50)
    price = models.PositiveIntegerField('Цена материала')

    def __str__(self):
        return self.name

class Contract(models.Model):
    contract_id = models.CharField('Номер договора', max_length=20)
    contract_date = models.DateField('Дата договора')
    region = models.CharField(choices=REGIONS_CHOICES, max_length=2, verbose_name='Район')
    locality = models.CharField('Населённый пункт', max_length=100)
    file = models.FileField('Тех. условия', blank=True)
    power = models.PositiveIntegerField('Мощность', blank=True, null=True)
    image = models.ImageField(
        upload_to=get_image_filename,
        verbose_name='Фото',
        blank=True
    )
