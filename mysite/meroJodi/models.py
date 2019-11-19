from django.db import models
from django import forms
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
# from imagekit.models import ImageSpecField
# from imagekit.processors import *
import string
import random
from datetime import date

# Create your models here.


# def upload_location(instance, filename):
#     return "%s/%s" % (instance.slug, filename)


class Profile(models.Model):
    #=========Registration page 1 ==========#
    email = models.CharField(max_length=50)
    mobileno = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    confirmPassword = models.CharField(max_length=20)
    #=============END=======================#
    #========Registration page 2 ============#
    hometown = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    liveWithFamily_choices = (
        ('yes', "Yes"),
        ('no', 'No'),
    )
    liveWithFamily = models.BooleanField(
        choices=liveWithFamily_choices, default=True)
    maritalStatus_choices = (
        ('single', 'Single'),
        ('divorced', 'Divorced'),
        ('widowed', 'Widowed'),
    )
    maritalStatus = models.CharField(
        max_length=25, choices=maritalStatus_choices, default='single')
    diet_choices = (
        ('veg', 'Veg'),
        ('non-veg', 'Non-Veg'),
        ('occasionally non-veg', 'Occasionally Non-Veg'),
        ('eggetarian', 'Eggetarian'),
    )
    diet = models.CharField(max_length=20, choices=diet_choices, default='veg')
    height_choices = (
        ('one', ' 4\'0\"-4\'3\" '),
        ('two', ' 4\'4\"-4\'7\" '),
        ('three', ' 4\'8\"-4\'11\" '),
        ('four', ' 5\'0\"-5\'3\" '),
        ('five', ' 5\'4\"-5\'7\" '),
        ('six', ' 5\'8\"-5\'11\" '),
        ('seven', ' 6\'0\"-6\'3\" '),
        ('eight', ' 6\'3\"-6\'7\" '),
        ('nine', ' Above 6\'8\" '),
    )
    height = models.CharField(
        max_length=20, choices=height_choices, default="4\'0\"-4\'3\"")
    caste_choices = (
        ('Others/Undefined'),
        ('Foreigners'),
        ('Amat'),
        ('Athpahariya'),
        ('Badhaee'),
        ('Badi'),
        ('Bahing'),
        ('Bantawa'),
        ('Bantar/Sardar'),
        ('Barai'),
        ('Bengali'),
        ('Bhote'),
        ('Bhujel'),
        ('Bin'),
        ('Bote'),
        ('Brahmin-Hill/Bahun'),
        ('Brahmin-Tarai(Maithil, Kanyakubja, Bhumihar)'),
        ('Brahmu/Baramo'),
        ('Byansi/Sauka'),
        ('Chamar/Harijan/Ram'),
        ('Chamling'),
        ('Chepang'),
        ('Chhantyal'),
        ('Chhetri'),
        ('Chidimar'),
        ('Damai/Dholi'),
        ('Darai'),
        ('Danuwar'),
        ('Dev'),
        ('Dhandi'),
        ('Dhankar/Dharikar'),
        ('Dhanuk'),
        ('Dhobi'),
        ('Dhimal'),
        ('Dhuniya'),
        ('Dolpo'),
        ('Dom'),
        ('Dusadh/Pasawan/Pasi'),
        ('Dura'),
        ('Gaderi/Bhediyar'),
        ('Gangai'),
        ('Gaine'),
        ('Ghale'),
        ('Gurung'),
        ('Halkhor'),
        ('Hayu'),
        ('Hyolmo'),
        ('Jhangar/Uraon'),
        ('Jirel'),
        ('Kami'),
        ('Kalwar'),
        ('Kanu/Haluwai'),
        ('Kathabaniyan'),
        ('Kewat'),
        ('Khatwe'),
        ('Koiri/Kushwaha'),
        ('Kumal'),
        ('Kurmi'),
        ('Kahar'),
        ('Kayastha'),
        ('Kulung'),
        ('Kumhar'),
        ('Koche'),
        ('Kamar'),
        ('Kisan'),
        ('Khaling'),
        ('Kusunda'),
        ('Kalar'),
        ('Kori'),
        ('Khawas'),
        ('Lodh'),
        ('Lohar'),
        ('Limbu'),
        ('Lepcha'),
        ('Lhomi'),
        ('Lhopa'),
        ('Lohorung'),
        ('Magar'),
        ('Musahar'),
        ('Mallaha'),
        ('Majhi'),
        ('Mewahang'),
        ('Munda'),
        ('Meche'),
        ('Mali'),
        ('Marwadi'),
        ('Nuniya'),
        ('Newar'),
        ('Nachhring'),
        ('Natuwa'),
        ('Nurang'),
        ('Pathakatta/Kushwadia'),
        ('Punjabi'),
        ('Pahari'),
        ('Raji'),
        ('Rajput/Terai Kshetriya'),
        ('Rajdhob'),
        ('ajbhar'),
        ('ai'),
        ('aute'),
        ('ajbanshi'),
        ('udhi'),
        ('arki'),
        ('Sherpa'),
        ('Sanyasi/Dasnami'),
        ('Sunwar'),
        ('Sonar'),
        ('Santhal'),
        ('Sampang'),
        ('Sarabaria'),
        ('Thakali'),
        ('Thami'),
        ('Tatma/Tatwa'),
        ('Teli'),
        ('Tamang'),
        ('Thakuri'),
        ('Tharu'),
        ('Thakur/Hajam'),
        ('Topkegola'),
        ('Thulung'),
        ('Tajpuriya'),
        ('Walung'),
        ('Yamphu'),
        ('Yadav'),
        ('Yakkha'),
    )
    caste = models.CharField(
        max_length=60, choices=[(caste_choices, str(caste_choices)) for caste_choices in caste_choices], default='Others/Undefined')
    #============END=======================#
    #========Registration page 3 ============#

    education_level_choices = (
        ('Associaction Degree', 'Association Degree'),
        ('Bachelors', 'Bachelors'),
        ('Diploma', 'Diploma'),
        ('High School', 'High School'),
        ('Honours Degree', 'Honours Degree'),
        ('Trade School', 'Trade School'),
        ('Undergraduate', 'Undergraduate'),
        ('Masters', 'Masters'),
        ('Less than High School', 'Less than High School'),
    )
    education_level = models.CharField(
        max_length=30, choices=education_level_choices)

    education_field_choices = (
        ('Administrative Service'),
        ('Architecture'),
        ('Armed Forces'),
        ('Arts'),
        ('Computers/IT'),
        ('Commerce'),
        ('Engineering/Technology'),
        ('Education'),
        ('Fashion'),
        ('Finance'),
        ('Fine Arts'),
        ('Health Sciences/Nursing'),
        ('Law'),
        ('Management'),
        ('Marketing/Advertising'),
        ('Medicine'),
        ('Music'),
        ('Office Administration'),
        ('Science'),
        ('Shipping'),
        ('Travel & Tourism'),
    )
    education_field = models.CharField(max_length=40, choices=[(education_field_choices, str(
        education_field_choices)) for education_field_choices in education_field_choices])
    college_name = models.CharField(max_length=50)
    work_with_choices = (
        ('Business/Self Employed', 'Business/Self Employed'),
        ('Civil Services', 'Civil Services'),
        ('Government/Public Sector', 'Government/Public Sector'),
        ('Private Company', 'Private Company'),
        ('Not Working', 'Not Working'),
    )
    work_with = models.CharField(max_length=40, choices=work_with_choices)
    monthly_income_choices = (
        ('5k+', '> 5000'),
        ('15k+', '> 15000'),
        ('25k+', '> 25000'),
        ('40k+', '> 40000'),
        ('60k+', '> 60000'),
        ('1l+', '> 1Lakh'),
        ('3l+', '> 3Lakh'),
        ('5l+', '> 5Lakh'),
        ('8l+', '> 8Lakh'),
        ('12l+', '> 12Lakh'),
    )
    monthly_income = models.CharField(
        max_length=20, choices=monthly_income_choices)
    #=============END=======================#

    # for monthly_income_choices, monthlyIncome in enumerate(monthly_income_choices):

    # user = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                          default=1, on_delete=models.CASCADE)

    # Basics & Lifestyle
    # tmId = models.AutoField(primary_key=True)
    # pId = models.CharField(max_length=10, default='TMG')
    # slug = models.SlugField(unique=True)
    # name = models.CharField(max_length=50)
    # image = models.ImageField(upload_to=upload_location, null=True,
    #                           blank=True, default="{% static 'meroJodi/images/pimage.png' %}")
    # thumbnail = ImageSpecField(

    #     source='image', processors=[SmartResize(600, 600)], format='JPEG',
    #     options={'quality': 70},

    # )
    # maritalStatus_choices = (
    #     ('single', 'Single'),
    #     ('married', 'Married'),
    #     ('divorced', 'Divorced'),
    # )
    # maritalStatus = models.CharField(
    #     max_length=25, choices=maritalStatus_choices, default='single')
    # body_Type = models.CharField(max_length=15)
    # height = models.CharField(max_length=15)
    # weight = models.CharField(max_length=15)
    # matrimonyProfileFor_choices = (
    #     ('son', 'Son'),
    #     ('daughter', 'Daughter'),
    #     ('brother', 'Brother'),
    #     ('sister', 'Sister'),
    #     ('self', 'Self'),
    # )
    # matrimonyProfileFor = models.CharField(
    #     max_length=25, choices=matrimonyProfileFor_choices, default='personal')
    # drink = models.CharField(max_length=15)
    # smoke = models.CharField(max_length=15)
    # dateOfBirth = models.DateTimeField(
    #     'Date of Birth/Time - Format : YYYY-MM-DD HH:MM', auto_now=False, auto_now_add=False,)

    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # age = models.IntegerField(default=0)
    # motherTongue = models.CharField(max_length=50)
    # gender_choices = (
    #     ('male', 'Male'),
    #     ('female', 'Female'),

    # )
    # gender = models.CharField(max_length=15, choices=gender_choices)
    # blood_group = models.CharField(max_length=20, default="not specified")
    # diet = models.CharField(max_length=20)

    # Religious / Social & Astro Background

    # timeOfBirth = models.TimeField( default= "00:00")
    # religion_choices = (
    #     ('hindu', 'Hindu'),
    #     ('cristian', 'Cristian'),
    #     ('muslim', 'Muslim'),
    #     ('sikh', 'Sikh'),
    #     ('buddhist', 'Buddhist')
    # )
    # religion = models.CharField(max_length=50, choices=religion_choices)
    # caste = models.CharField(max_length=50)
    # sub_caste = models.CharField(max_length=25)
    # DOB
    # placeOfBirth = models.CharField(max_length=30)
    # rassi = models.CharField(max_length=30)

    # Education & Career

    # education = models.CharField(max_length=50)
    # ================================> <========= #
    # education_field = models.CharField(max_length=50)
    # education_level = models.CharField(max_length=50)
    # work_with = models.CharField(max_length=50)
    # college_name = models.CharField(max_length=50)
    # ================================> <========= #

    # education_detail = models.CharField(max_length=50)
    # occupation_detail = models.CharField(max_length=100)
    # ================================> <========= #
    # monthly_income = models.CharField(max_length=20, default="not specified")
    # annual_income = models.CharField(max_length=20, default="not specified")
    # current_location = models.CharField(max_length=25)

    # Family Details

    # father_occupation = models.CharField(max_length=50)
    # mother_occupation = models.CharField(max_length=50)
    # no_of_sisters = models.IntegerField(default=0)
    # no_of_brother = models.IntegerField(default=0)

    # ========partner prefrences======

    # p_age_min = models.IntegerField(default=0)
    # p_age_max = models.IntegerField(default=0)
    # p_Marital_Status = models.CharField(max_length=10)
    # p_Body_Type = models.CharField(max_length=25)
    # p_Complexion = models.CharField(max_length=25)
    # p_Height = models.CharField(max_length=25)

    # p_Diet = models.CharField(max_length=25)
    # p_Manglik = models.CharField(max_length=25)
    # p_Religion = models.CharField(max_length=25)
    # p_Caste = models.CharField(max_length=25)
    # p_Mother_Tongue = models.CharField(max_length=25)
    # p_Education = models.CharField(max_length=25)
    # p_Country_Of_Residence = models.CharField(max_length=25)
    # p_State = models.CharField(max_length=25)

    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # def __str__(self):
    #     return self.pId

    # def get_absolute_url(self):
    #     return reverse("profiles:detail", kwargs={"slug": self.slug})

    # class Meta:
    #     ordering = ["-timestamp", "-updated"]


# def create_slug(instance, new_slug=None):
#     slug = slugify(instance.name)
#     if new_slug is not None:
#         slug = new_slug
#     qs = profiles.objects.filter(slug=slug).order_by("-tmId")
#     exists = qs.exists()
#     if exists:
#         new_slug = "%s-%s" % (slug, qs.first().tmId)
#         return create_slug(instance, new_slug=new_slug)
#     return slug


# def pre_save_post_signal_reciever(sender, instance, *args, **kwargs):

#     if not instance.slug:
#         instance.slug = create_slug(instance)


# pre_save.connect(pre_save_post_signal_reciever, sender=Profile)

# email = models.EmailField(null=True, blank=True)
# mobileno = models.PositiveIntegerField(null=True, blank=True)
# password = models.CharField(max_length=20, null=True, blank=True)
# hometown = models.CharField(max_length=30, null=True, blank=True)
# city = models.CharField(max_length=20, null=True, blank=True)
# country = models.CharField(max_length=20, null=True, blank=True)
# live_with_family = models.BooleanField(null=True, blank=True)
# marital_status = models.CharField(max_length=15, null=True, blank=True)
# diet = models.CharField(max_length=20, null=True, blank=True)
# height = models.CharField(max_length=20, null=True, blank=True)
# caste = models.CharField(max_length=20, null=True, blank=True)
# education_level = models.CharField(max_length=20, null=True, blank=True)
# education_field = models.CharField(max_length=20, null=True, blank=True)
# college_name = models.CharField(max_length=20, null=True, blank=True)
# work_with = models.CharField(max_length=20, null=True, blank=True)
# monthly_income = models.CharField(max_length=20, null=True, blank=True)
