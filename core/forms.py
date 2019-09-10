from django import forms
from django.forms import inlineformset_factory, modelformset_factory, formset_factory
from .models import Profile, FamilyMember, Programmer, Language

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('fname', 'lname')

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ('profile', 'name', 'relationship')

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ('name',)

class ProgrammerForm(forms.ModelForm):
    class Meta:
        model = Programmer
        fields = ('name',)

FamilyMemberFormSet = inlineformset_factory(
    Profile, FamilyMember, form=FamilyMemberForm, extra=1
)

# inlineformset_factory
LanguageInlineFormset = inlineformset_factory(Programmer, Language, fields=('name', ), extra=1)

# modelformset_factory
LanguageModelFormset = modelformset_factory(Language, fields=('name',))

# formset_factory
LanguageFormset = formset_factory(LanguageForm, extra=1)