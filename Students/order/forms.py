
from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(
        label='Имя покупателя',
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите ваше имя'
        })
    )

    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        widget=forms.TextInput(attrs={
            'placeholder': '+998 90 123 45 67'
        })
    )

    product = forms.ChoiceField(
        label='Товар',
        choices=[
            ('laptop', 'Ноутбук — 5 000 000 сум'),
            ('phone', 'Телефон — 3 000 000 сум'),
            ('headphones', 'Наушники — 200 000 сум'),
        ]
    )

    quantity = forms.IntegerField(
        label='Количество',
        min_value=1,
        initial=1
    )

    delivery = forms.ChoiceField(
        label='Доставка',
        choices=[
            ('pickup', 'Самовывоз — бесплатно'),
            ('courier', 'Курьер — 30 000 сум'),
        ]
    )

    address = forms.CharField(
        label='Адрес',
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите адрес доставки'
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        delivery = cleaned_data.get('delivery')
        address = cleaned_data.get('address')

        if delivery == 'courier' and not address:
            self.add_error('address', 'Укажите адрес доставки')

        return cleaned_data
