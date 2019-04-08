from django import forms

from .models import Item, Images
from users.models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class PostItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ('contract_id', 'contract_date', 'name', 'deadline', 'power', 'extra_info', 'oriented_price', 'locality', 'region', 'file')
        widgets = {
            'contract_date': DateInput(),
            'deadline': DateInput()
        }

class ImageForm(forms.ModelForm):
    image = forms.ImageField(label="Фото")

    class Meta:
        model = Images
        fields = ('image', )