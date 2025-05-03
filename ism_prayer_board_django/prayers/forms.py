from django import forms
from .models import PrayerRequest

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['student_name', 'ministry_group', 'status', 'content']
        labels = {
            'student_name': 'Name',
            'ministry_group': 'Mentor',
            'status': 'Status',
            'content': 'Prayer Request',
        }
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
