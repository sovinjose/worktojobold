import re
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import UserProfile, CompanyProfile, OpeningDetails


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class CompanyProfileForm(ModelForm):

    email = forms.CharField(label='E-mail')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')

    class Meta:
        model = CompanyProfile
        exclude = ['user_profile', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class' : "form-control"})
        self.fields['first_name'].widget.attrs.update({'class' : "form-control"})
        self.fields['last_name'].widget.attrs.update({'class' : "form-control"})
        self.fields['name'].widget.attrs.update({'class' : "form-control"})
        self.fields['description'].widget.attrs.update({'class' : "form-control"})
        self.fields['industry_type'].widget.attrs.update({'class' : "form-control"})
        self.fields['contact_number'].widget.attrs.update({'class' : "form-control"})
        self.fields['company_type'].widget.attrs.update({'class' : "form-control"})
        self.fields['website'].widget.attrs.update({'class' : "form-control"})
        self.fields['logo'].widget.attrs.update({'class' : "form-control"})
        self.fields['address'].widget.attrs.update({'class' : "form-control"})

    def clean_email(self):
        try:
            user = User.objects.get(
                username=self.cleaned_data['email']
            )
        except ObjectDoesNotExist:
                return self.cleaned_data['email']
        raise forms.ValidationError('This e-mail ID already exists.')

    def clean_first_name(self):
        if re.match(r"^([a-zA-Z._ ]*)$", self.cleaned_data['first_name'].strip()):
            return self.cleaned_data['first_name'].strip()
            if len(self.cleaned_data['first_name']) > 30:
                raise forms.ValidationError('Name seems to be too long')
        raise forms.ValidationError('Please enter a valid  name')

    def clean_name(self):
        if re.match(r"^([a-zA-Z._ ]*)$", self.cleaned_data['name'].strip()):
            return self.cleaned_data['name'].strip()
            if len(self.cleaned_data['name']) > 20:
                raise forms.ValidationError('Name seems to be too long')
        raise forms.ValidationError('Please enter a valid  company name')

    def clean_contact_number(self):
        if re.match(r"^([0-9+(). -]{6,15})$", self.cleaned_data['contact_number']):
            if len(self.cleaned_data['contact_number']) < 6:
                raise forms.ValidationError('Phone Number must contain at least six digits')
            return self.cleaned_data['contact_number'].strip()
        raise forms.ValidationError('Invalid Contact No.')





class OpeningDetailsForm(ModelForm):

    class Meta:
        model = OpeningDetails
        exclude = ['company', 'created_at', 'active_status']

    def __init__(self, *args, **kwargs):
        super(OpeningDetailsForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_id'].widget.attrs.update({'class' : "form-control"})

        self.fields['job_description'].widget.attrs.update({'class' : "form-control"})
        #self.fields['Keywords'].widget.attrs.update({'class' : "form-control"})
        self.fields['skill'].widget.attrs.update({'class' : "form-control"})
        self.fields['work_experienc_min'].widget.attrs.update({'class' : "form-control"})
        self.fields['work_experienc_max'].widget.attrs.update({'class' : "form-control"})
        self.fields['annual_ctc_min'].widget.attrs.update({'class' : "form-control"})
        self.fields['annual_ctc_max'].widget.attrs.update({'class' : "form-control"})
        self.fields['number_of_vacancies'].widget.attrs.update({'class' : "form-control"})
        self.fields['location'].widget.attrs.update({'class' : "form-control"})
        self.fields['industry'].widget.attrs.update({'class' : "form-control"})
        self.fields['functional_area'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_role'].widget.attrs.update({'class' : "form-control"})
        self.fields['qualifications'].widget.attrs.update({'class' : "form-control"})
        self.fields['contact_number'].widget.attrs.update({'class' : "form-control"})
        self.fields['contact_email'].widget.attrs.update({'class' : "form-control"})



