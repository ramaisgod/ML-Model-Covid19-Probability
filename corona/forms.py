from django import forms


ChoicesYesNo = (('', '---------'), ('1', 'Yes'), ('0', 'No'))
ChoicesBreath = (('', '---------'), ('1', 'Very Difficulty'), ('0', 'Small Difficulty'), ('-1', 'No Difficulty'))


class TestForm(forms.Form):
    # name = forms.CharField(max_length=100, required=True, label="Patient Name")
    age = forms.IntegerField(required=True, min_value=1, max_value=105)
    travel_history = forms.ChoiceField(required=True, choices=ChoicesYesNo, label="International Travel History ?")
    fever = forms.FloatField(required=True, min_value=98, max_value=105, label="Body Temperature", help_text="Average human body temperature is 98.2 °F")
    body_pain = forms.ChoiceField(required=True, choices=ChoicesYesNo, label="Do you have body pain?")
    runny_nose = forms.ChoiceField(required=True, choices=ChoicesYesNo, label="Is your nose runny?")
    diff_breathing = forms.ChoiceField(required=True, choices=ChoicesBreath, label="Difficulty in breathing?")

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
