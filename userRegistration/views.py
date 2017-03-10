from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from .forms import UserProfileForm, CompanyProfileForm, OpeningDetailsForm
from. models import CompanyProfile, OpeningDetails


class HomeView(View):

    def get(self, requests):
        return HttpResponseRedirect('/company/details')


class CreateUserProfileView(View):
    def get(self, requests):
        return render(requests, 'user_registration.html')


class CreateCompanyAccount(View):

    def get(self, requests):
        cmpny_form = CompanyProfileForm()
        context = {
            'cmpny_form' : cmpny_form
        }
        return render(requests, 'user_registration.html', context)

    def post(self, requests):
        email = requests.POST.get('email', None)
        password = requests.POST.get('password', None)
        password2 = requests.POST.get('password2', None)
        #try:
        if email and password:
            cmpny_form = CompanyProfileForm(requests.POST)
            if cmpny_form.is_valid():
                user = User.objects.create_user(
                                username=email,
                                password=password,
                                first_name=requests.POST.get('first_name'),
                                last_name=requests.POST.get('last_name'),
                                email=email
                            )
                cmp_frm = cmpny_form.save(commit=False)
                cmp_frm.user_profile = user
                cmp_frm.save()
                messages.add_message(requests, messages.INFO, 'successfully crested the user')
                user = authenticate(username=email, password=password)
                login(requests, user)
                return HttpResponseRedirect('/company/details')
            else:
                messages.add_message(requests, messages.ERROR, cmpny_form.errors)
        else:
            messages.add_message(requests, messages.ERROR, 'Please enter Email And Apssword.')
        #except Exception as e:
        #    messages.add_message(requests, messages.ERROR, e.message)
        context = {
            'cmpny_form' : CompanyProfileForm(requests.POST)
        }
        return render(requests, 'user_registration.html', context)


class CompanyAccountDetails(View):

    def get(self, requests):
        cmp_details = CompanyProfile.objects.get(user_profile=requests.user)
        openong_details = OpeningDetails.objects.filter(company__user_profile = requests.user, active_status=True)
        context = {
            'cmp_details' : cmp_details,
            'openong_details' : openong_details
        }
        return render(requests, 'company_details.html', context)


class PostNewJob(View):

    def get(self, requests):
        form = OpeningDetailsForm()
        context = {
            'form' : form
        }
        return render(requests, 'post_job.html', context)

    def post(self, requests):
        print requests.POST
        form = OpeningDetailsForm(requests.POST)
        if form.is_valid():
            cmp_obj = CompanyProfile.objects.get(user_profile=requests.user)
            form_obj = form.save(commit=False)
            form_obj.company = cmp_obj
            form_obj.save()
            return HttpResponseRedirect('/company/details')
        else:
            print form.errors
            context = {
                'form' : form
            }
        return render(requests, 'post_job.html', context)


class JobDetails(View):

    def get(self, requests, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        context = {
            'opng_details' : opng_details
        }
        return render(requests, 'job_details.html', context)


class CloseJobStatus(View):

    def post(self, requests, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        opng_details.active_status = False
        opng_details.save()
        return HttpResponseRedirect('/')


class CompanyJobListView(View):

    def get(self, requests):
        cmp_details = CompanyProfile.objects.get(user_profile=requests.user)
        opng_details = OpeningDetails.objects.all()
        context = {
            'opng_details' : opng_details,
            'cmp_details' : cmp_details
        }
        return render(requests, 'company_job_list.html', context)



