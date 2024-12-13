from django import forms
from .models import Recording

class RecordingForm(forms.ModelForm):
    class Meta:
        model = Recording
        fields = ['name', 'price_morning', 'price_afternoon', 'price_evening' 'timeslot']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['timeslot'].choices = [
            (slot, slot.strftime('%Y-%m-%d %H:%M'))
            for slot in Recording.get_available_timeslots()
        ]
