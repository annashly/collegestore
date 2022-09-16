from django import forms
from .models import Membership

GENDER_CHOICES = [
 ('Male', 'Male'),
 ('Female', 'Female')
]

MATERIALS_CHOICE = [
 ('Notebook', 'Notebook'),
 ('Pen', 'Pen'),
 ('Exampaper', 'Exampaper'),
 ('Chartpaper', 'Chartpaper'),
 ('Pencil', 'Pencil'),
 ('RecordBook', 'RecordBook')
]

class MembershipForm(forms.ModelForm):
 gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
 materials_provide = forms.MultipleChoiceField(label='Materials provided', choices=MATERIALS_CHOICE, widget=forms.CheckboxSelectMultiple)
 class Meta:
  model = Membership
  fields = ['name', 'dob','age', 'gender', 'mobile', 'email','address', 'department', 'course', 'purpose','materials_provide']
  labels = {'name':'Full Name', 'dob': 'Date of Birth', 'age':'Age', 'mobile':'Mobile No.', 'email':'Email ID', 'address':'Address'}
  widgets = {
   'name':forms.TextInput(attrs={'class':'form-control'}),
   'dob':forms.DateInput(attrs={'class':'form-control', 'id':'datepicker'}),
   'age':forms.NumberInput(attrs={'class':'form-control'}),
   'course':forms.TextInput(attrs={'class':'form-control'}),
   'address':forms.TextInput(attrs={'class':'form-control'}),
   'department':forms.Select(attrs={'class':'form-select'}),
   'mobile':forms.NumberInput(attrs={'class':'form-control'}),
   'email':forms.EmailInput(attrs={'class':'form-control'}),
   'purpose':forms.Select(attrs={'class':'form-select'}),
  }