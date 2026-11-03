from django import forms


class StudentForm(forms.Form):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    age = forms.IntegerField(label='Возраст')
    email = forms.EmailField(label='Email')