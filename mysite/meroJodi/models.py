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
        (' 4\'0\"-4\'3\" '),
        (' 4\'4\"-4\'7\" '),
        (' 4\'8\"-4\'11\" '),
        (' 5\'0\"-5\'3\" '),
        (' 5\'4\"-5\'7\" '),
        (' 5\'8\"-5\'11\" '),
        (' 6\'0\"-6\'3\" '),
        (' 6\'3\"-6\'7\" '),
        (' Above 6\'8\" '),
    )
    height = models.CharField(
        max_length=15, choices=[(height_choices, str(height_choices)) for height_choices in range(1, 10)], default="4\'0\"-4\'3\"")
    caste_choices = (
        ('0', 'Others/Undefined'),
        ('1', 'Foreigners'),
        ('2', 'Amat'),
        ('3', 'Athpahariya'),
        ('4', 'Badhaee'),
        ('5', 'Badi'),
        ('6', 'Bahing'),
        ('7', 'Bantawa'),
        ('8', 'Bantar/Sardar'),
        ('9', 'Barai'),
        ('10', 'Bengali'),
        ('11', 'Bhote'),
        ('12', 'Bhujel'),
        ('13', 'Bin'),
        ('14', 'Bote'),
        ('15', 'Brahmin-Hill/Bahun'),
        ('16', 'Brahmin-Tarai(Maithil, Kanyakubja, Bhumihar)'),
        ('17', 'Brahmu/Baramo'),
        ('18', 'Byansi/Sauka'),
        ('19', 'Chamar/Harijan/Ram'),
        ('20', 'Chamling'),
        ('21', 'Chepang'),
        ('22', 'Chhantyal'),
        ('23', 'Chhetri'),
        ('24', 'Chidimar'),
        ('25', 'Damai/Dholi'),
        ('26', 'Darai'),
        ('27', 'Danuwar'),
        ('28', 'Dev'),
        ('29', 'Dhandi'),
        ('30', 'Dhankar/Dharikar'),
        ('31', 'Dhanuk'),
        ('32', 'Dhobi'),
        ('33', 'Dhimal'),
        ('34', 'Dhuniya'),
        ('35', 'Dolpo'),
        ('36', 'Dom'),
        ('35', 'Dusadh/Pasawan/Pasi'),
        ('36', 'Dura'),
        ('37', 'Gaderi/Bhediyar'),
        ('38', 'Gangai'),
        ('39', 'Gaine'),
        ('40', 'Ghale'),
        ('41', 'Gurung'),
        ('42', 'Halkhor'),
        ('43', 'Hayu'),
        ('44', 'Hyolmo'),
        ('45', 'Jhangar/Uraon'),
        ('46', 'Jirel'),
        ('47', 'Kami'),
        ('48', 'Kalwar'),
        ('49', 'Kanu/Haluwai'),
        ('50', 'Kathabaniyan'),
        ('51', 'Kewat'),
        ('52', 'Khatwe'),
        ('53', 'Koiri/Kushwaha'),
        ('54', 'Kumal'),
        ('55', 'Kurmi'),
        ('56', 'Kahar'),
        ('57', 'Kayastha'),
        ('58', 'Kulung'),
        ('59', 'Kumhar'),
        ('60', 'Koche'),
        ('61', 'Kamar'),
        ('62', 'Kisan'),
        ('63', 'Khaling'),
        ('64', 'Kusunda'),
        ('65', 'Kalar'),
        ('66', 'Kori'),
        ('67', 'Khawas'),
        ('68', 'Lodh'),
        ('69', 'Lohar'),
        ('70', 'Limbu'),
        ('71', 'Lepcha'),
        ('72', 'Lhomi'),
        ('73', 'Lhopa'),
        ('74', 'Lohorung'),
        ('75', 'Magar'),
        ('76', 'Musahar'),
        ('77', 'Mallaha'),
        ('78', 'Majhi'),
        ('79', 'Mewahang'),
        ('80', 'Munda'),
        ('81', 'Meche'),
        ('82', 'Mali'),
        ('83', 'Marwadi'),
        ('84', 'Nuniya'),
        ('85', 'Newar'),
        ('86', 'Nachhring'),
        ('87', 'Natuwa'),
        ('88', 'Nurang'),
        ('89', 'Pathakatta/Kushwadia'),
        ('90', 'Punjabi'),
        ('91', 'Pahari'),
        ('92', 'Raji'),
        ('93', 'Rajput/Terai Kshetriya'),
        ('94', 'Rajdhob'),
        ('95', 'Rajbhar'),
        ('96', 'Rai'),
        ('97', 'Raute'),
        ('98', 'Rajbanshi'),
        ('99', 'Sudhi'),
        ('100', 'Sarki'),
        ('101', 'Sherpa'),
        ('102', 'Sanyasi/Dasnami'),
        ('103', 'Sunwar'),
        ('104', 'Sonar'),
        ('105', 'Santhal'),
        ('106', 'Sampang'),
        ('107', 'Sarabaria'),
        ('108', 'Thakali'),
        ('109', 'Thami'),
        ('110', 'Tatma/Tatwa'),
        ('111', 'Teli'),
        ('112', 'Tamang'),
        ('113', 'Thakuri'),
        ('114', 'Tharu'),
        ('115', 'Thakur/Hajam'),
        ('116', 'Topkegola'),
        ('117', 'Thulung'),
        ('118', 'Tajpuriya'),
        ('119', 'Walung'),
        ('120', 'Yamphu'),
        ('121', 'Yadav'),
        ('122', 'Yakkha'),
    )
    caste = models.CharField(max_length=50, choices=[(caste_choices, str(caste_choices))
                                                     for caste_choices in range(1, 123)], default='Others/Undefined')
    #=============END=======================#
    #========Registration page 3 ============#

    education_level_choices = (
        ('Association Degree'),
        ('Bachelors'),
        ('Diploma'),
        ('High School'),
        ('Honours Degree'),
        ('Trade School'),
        ('Undergraduate'),
        ('Masters'),
        ('Less than High School'),
    )
    education_level = models.CharField(
        max_length=20, choices=[(education_level_choices, str(education_level_choices)) for education_level_choices in range(1, 10)])

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
    education_field = models.CharField(max_length=20, choices=[(education_field_choices, str(
        education_field_choices)) for education_field_choices in range(1, 22)])
    college_name = models.CharField(max_length=50)
    work_with_choices = (
        ('Business/Self Employed'),
        ('Civil Services'),
        ('Government/Public Sector'),
        ('Private Company'),
        ('Not Working'),
    )
    work_with = models.CharField(max_length=20, choices=work_with_choices)
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
        max_length=20, choices=[(monthly_income_choices, str(monthly_income_choices)) for monthly_income_choices in range(1, 11)])
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
