from django import forms

class EstudianteRegistroForm(forms.Form):
    Tarjeta_identidad = forms.CharField(max_length=20)
    Clave = forms.CharField(max_length=100, widget=forms.PasswordInput)

class ProfesorRegistroForm(forms.Form):
    Cedula = forms.CharField(max_length=20)
    Clave = forms.CharField(max_length=100, widget=forms.PasswordInput)
