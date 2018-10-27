from django import forms


class AirportForm(forms.Form):
	code = forms.CharField(max_length=3, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Airport Code'
		}))
	city = forms.CharField(max_length=30, widget=forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Airport City'
		}))