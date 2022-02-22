from django import forms
from .models import ImageUploadingTest, ApplicationRound


class ApplicationForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = ImageUploadingTest
        fields = ('title', 'image', 'doc')

class ApplicationRoundForm(forms.ModelForm):

    class Meta:
        model = ApplicationRound
        fields = ('title', 'start_date', 'end_date', 'visible', 'active')

        date_input_type = forms.DateInput()
        date_input_type.input_type = 'date'

        widgets = {
            'title' : forms.TextInput(),
            'start_date': date_input_type,
            'end_date' : date_input_type,
            'visible' : forms.CheckboxInput(),
            'active' : forms.CheckboxInput(),

        }