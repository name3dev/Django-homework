from django import forms

OPERATION_CHOICES = [
    ("add", "Сложение (+)"),
    ("subtract", "Вычитание (-)"),
    ("multiply", "Умножение (*)"),
    ("divide", "Деление (/)"),
]

class Calculator(forms.Form):
    first_number = forms.FloatField(label="Первое число")
    second_number = forms.FloatField(label="Второе число")
    chose_function = forms.ChoiceField(
        label="Выберите вариант операций",
        choices=OPERATION_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
