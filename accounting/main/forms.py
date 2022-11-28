import imp
from .models import *
from django.forms import *
from django import forms
from .settings import *

class RoomForm(ModelForm):
	class Meta:
		model = Room
		fields = ["phone"]
		widgets = {
			"phone": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Телефон'
			})
		}


class MedCardForm(ModelForm):
	date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y', attrs={'placeholder': 'Дата', 'class': 'form-control'}), input_formats=DATE_INPUT_FORMATS)
	class Meta:
		model = MedCard
		fields = ["name", "diagnos", "cause", "gender", "age", "date", "other"]
		widgets = {
				"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'ФИО'
			}),
				"diagnos": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Диагноз'
			}),
				"cause": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Причина поступления'
			}),
				"gender": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Пол'
			}),
				"age": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Возраст'
			}),
				"other": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Остальное'
			}),
		}


class MoveForm(ModelForm):
	date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y', attrs={'placeholder': 'Дата', 'class': 'form-control'}), input_formats=DATE_INPUT_FORMATS)
	class Meta:
		model = Move
		fields = ["date", "medCard", "room"]
		widgets = {
				"medCard": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Мед Карта'
			}),
				"room": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Палата'
			}),
		}

class HealthyForm(ModelForm):
	date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y', attrs={'placeholder': 'Дата', 'class': 'form-control'}), input_formats=DATE_INPUT_FORMATS)
	class Meta:
		model = Healthy
		fields = ["medCard", "date", "discription"]
		widgets = {
				"medCard": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Мед Карта'
			}),
				"discription": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Причина выписки'
			}),
		}

class RoomOfMedCardForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'ФИО', 'class': 'form-control'}))

class MedCardOfDataForm(forms.Form):
	date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y', attrs={'placeholder': 'Дата', 'class': 'form-control'}), input_formats=DATE_INPUT_FORMATS)

class MedCardOfAgeForm(forms.Form):
	age = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder': 'Возраст', 'class': 'form-control'}))
