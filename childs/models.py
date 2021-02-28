from sponser.models import Sponser
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
# from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


# managers
class PublishedPostsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = "publish")


# models
class UserProfile(models.Model):
    HEALTH_STATE = (
        ("healthy","Healthy"),
        ("sick","Sick")
    )
    sponser = models.ForeignKey(Sponser, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30, default='')
    last_name = models.CharField(max_length=30, default='')
    membership_number = models.IntegerField(null=False, blank=False, unique=True)
    file_number = models.IntegerField(null=False, blank=False, unique=True)
    is_orphan = models.BooleanField()
    is_clever = models.BooleanField()
    is_rejected = models.BooleanField()
    is_poor = models.BooleanField()
    image = models.ImageField(upload_to="files/images")
    age = models.IntegerField()
    birthday = models.DateField()
    province_birthday = models.CharField(max_length=20)
    city_birthday = models.CharField(max_length=20)
    educational_class = models.CharField(max_length=10)
    last_year_score = models.FloatField()
    description = models.TextField()
    health_state = models.CharField(choices=HEALTH_STATE, default="healthy",max_length=10)
    sickness_description = models.TextField()
    donation_needs = models.CharField(max_length=20,blank=True, null=True)

    def  __str__(self):
        return self.first_name
    
    def get_absolute_url(self):
        return reverse("childs:child_details", kwargs={"id": self.pk})
    


class House(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=CASCADE,null= True)
    SITUATION = (
        ("owner","Owner"),
        ("tenant","Tenant")
    )
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    section = models.CharField(max_length=20)
    situation = models.CharField(choices=SITUATION, default="tenant",max_length=10)
    rooms_count = models.IntegerField()
    rent_amount = models.CharField(max_length=20)
    status_description = models.TextField()

    def  __str__(self):
        return self.user.first_name
    
    def get_absolute_url(self):
        return reverse("childs:house_details", kwargs={"id": self.pk})
    

class Family(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=CASCADE,null= True)
    father_name = models.CharField(max_length=20)
    mother_name = models.CharField(max_length=20)
    father_birthday  = models.DateTimeField()
    mother  = models.DateTimeField()
    father_education = models.CharField(max_length=15)
    father_education = models.CharField(max_length=15)
    brothers_count = models.IntegerField()
    sisters_count = models.IntegerField()
    supervisor = models.CharField(max_length=20)
    father_is_dead = models.BooleanField()
    mother_is_dead = models.BooleanField()
    father_dead_reason = models.CharField(max_length=15)
    mother_dead_reason = models.CharField(max_length=15)
    father_is_sick_or_defective = models.BooleanField()
    mother_is_sick_or_defective = models.BooleanField()
    father_defective_type = models.CharField(max_length=20)
    mother_defective_type = models.CharField(max_length=20)
    another_source_support = models.BooleanField(default=False)
    source_support = models.CharField(max_length=30, null= True)
    support_ammount = models.CharField(max_length=20, null= True)

    

    def  __str__(self):
        return self.user.first_name
    
    def get_absolute_url(self):
        return reverse("childs:family_details", kwargs={"id": self.pk})
    
class Requirements(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=CASCADE,null= True)
    medical = models.BooleanField()
    educational = models.BooleanField()
    food = models.BooleanField()
    clothing = models.BooleanField()
    family = models.BooleanField()
    other = models.BooleanField()
    description = models.TextField()
    def  __str__(self):
        return self.user.first_name
    
    def get_absolute_url(self):
        return reverse("childs:family_details", kwargs={"id": self.pk})
    

class News(models.Model):
    STATUS = (
        ("draft","Draft"),
        ("publish","Publish")
    )
    # objects = models.ObjectManager
    title = models.CharField(max_length=100)
    slug = models.SlugField( max_length=50, unique=True, allow_unicode=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images')
    publish_date = models.DateTimeField(default= timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(default="Draft",max_length=7, choices=STATUS)
    objects  = models.Manager()
    published_posts = PublishedPostsManager()

    def get_absolute_url(self):
        return reverse("childs:news_one", kwargs={"id": self.pk, "slug": self.slug})
    

    def  __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("childs:news_one", kwargs={"id": self.pk, "slug": self.slug})

class Events(models.Model):
    STATUS = (
        ("draft","Draft"),
        ("publish","Publish")
    )
    # objects = models.ObjectManager
    title = models.CharField(max_length=100)
    slug = models.SlugField( max_length=50, unique=True, allow_unicode=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body = models.TextField()
    image = models.ImageField(upload_to='files/images')
    publish_date = models.DateTimeField(default= timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    status = models.CharField(default="Draft",max_length=7, choices=STATUS)
    objects  = models.Manager()
    published_posts = PublishedPostsManager()

    def get_absolute_url(self):
        return reverse("childs:news_one", kwargs={"id": self.pk, "slug": self.slug})
    

    def  __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("childs:news_one", kwargs={"id": self.pk, "slug": self.slug})

class Office(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    ave = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    phone = models.CharField(max_length=14)
    fax = models.CharField(max_length=14, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    another_phone = models.CharField(max_length=14, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    country = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    intrest_in = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField()
