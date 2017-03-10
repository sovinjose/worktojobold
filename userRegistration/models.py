from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)


COMPANY_TYPE_CHOICE = (

        ('Consultant', 'Consultant'),
        ('Company', 'Company')
    )


class CompanyProfile(models.Model):
    user_profile = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    description = models.TextField()
    industry_type = models.CharField(max_length=100)
    address = models.TextField()
    contact_number =  models.CharField(max_length=20)
    company_type = models.CharField(max_length=100, null=True, blank=True)
    website = models.URLField(blank=True)
    logo = models.ImageField(upload_to='cmpny_logo', blank=True, null=True)


INDUSTRY_CHOICES = (
                ("IT-Software / Software Services", "IT-Software / Software Services"),
                ("BPO / Call Centre / ITES", "BPO / Call Centre / ITES"),
                ("Automobile / Auto Anciliary / Auto Components", "Automobile / Auto Anciliary / Auto Components"),
                ("Accounting / Finance", "Accounting / Finance"),
                ("Advertising / PR / MR / Event Management", "Advertising / PR / MR / Event Management"), 
                ("Agriculture / Dairy", "Agriculture / Dairy"),
                ("Animation / Gaming", "Animation / Gaming"),
                ("Architecture / Interior Design", "Architecture / Interior Design"),
                ("Aviation / Aerospace Firms", "Aviation / Aerospace Firms"),
                ("Banking / Financial Services / Broking", "Banking / Financial Services / Broking"),
                ("Brewery / Distillery", "Brewery / Distillery"),
                ("Broadcasting", "Broadcasting"),
                ("Consumer Electronics / Appliances / Durables", "Consumer Electronics / Appliances / Durables"),
                ("Education / Teaching / Training", "Education / Teaching / Training"),
                ("Electricals / Switchgears", "Electricals / Switchgears"),
)

FUNCTIONAL_AREA_CHOICES = (
                ("IT-Software / Software Services", "IT-Software / Software Services"),
                ("BPO / Call Centre / ITES", "BPO / Call Centre / ITES"),
                ("Automobile / Auto Anciliary / Auto Components", "Automobile / Auto Anciliary / Auto Components"),
                ("Accounting / Finance", "Accounting / Finance"),
                ("Advertising / PR / MR / Event Management", "Advertising / PR / MR / Event Management"), 
                ("Agriculture / Dairy", "Agriculture / Dairy"),
                ("Animation / Gaming", "Animation / Gaming"),
                ("Architecture / Interior Design", "Architecture / Interior Design"),
                ("Aviation / Aerospace Firms", "Aviation / Aerospace Firms"),
                ("Banking / Financial Services / Broking", "Banking / Financial Services / Broking"),
                ("Brewery / Distillery", "Brewery / Distillery"),
                ("Broadcasting", "Broadcasting"),
                ("Consumer Electronics / Appliances / Durables", "Consumer Electronics / Appliances / Durables"),
                ("Education / Teaching / Training", "Education / Teaching / Training"),
                ("Electricals / Switchgears", "Electricals / Switchgears"),
)

QUALIFICATIONS = (
                ('Graduation', 'Graduation'),
                ('Post Graduation', 'Post Graduation'),
                ('Ph.D', 'Ph.D'),
)

MIN_EXPERINCE = ((str(i), str(i)) for i in range(0, 31))
MAX_EXPERINCE = ((str(i), str(i)) for i in range(0, 31))

NO_OPENINGS = ((str(i), str(i)) for i in range(0, 20))


class OpeningDetails(models.Model):
    company = models.ForeignKey(CompanyProfile)
    job_title = models.CharField(max_length=100)
    job_id = models.CharField(max_length=100)
    job_description = models.TextField()
    #Keywords = models.TextField()
    work_experienc_min = models.CharField(max_length=100, choices=MIN_EXPERINCE)
    work_experienc_max = models.CharField(max_length=100, choices=MAX_EXPERINCE)
    annual_ctc_min = models.CharField(max_length=100)
    annual_ctc_max = models.CharField(max_length=100)
    number_of_vacancies = models.CharField(max_length=100, choices=NO_OPENINGS)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)
    functional_area = models.CharField(max_length=100, choices=FUNCTIONAL_AREA_CHOICES)
    job_role = models.TextField()
    qualifications = models.CharField(max_length=100, choices=QUALIFICATIONS)
    skill = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.CharField(max_length=100)
    active_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)





