from django import forms # type: ignore
from .models import Event, Member, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description']  # Ensure these match your Event model fields

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'role', 'bio']  # Use 'role' instead of 'position', and include 'bio'

