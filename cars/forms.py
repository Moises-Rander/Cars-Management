from django import forms
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_value(self):
        value = self.cleaned_data.get('value')
        cost = self.cleaned_data.get('cost')
        if cost:
            if value < (cost * 1.1):
                self.add_error('value', 'O valor do carro deve ser pelo menos 10% maior que o valor de custo para evitar prejuízos.')
        return value
