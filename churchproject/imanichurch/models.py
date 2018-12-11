import uuid
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

# implements model inheritance


class CommonModelInfo(models.Model):
    image = models.ImageField(
        upload_to='imanichurch/static/images',
        max_length=100, blank=True, null=True,
        help_text="Upload a Picture *Optional")

    description = models.TextField(
        max_length=100, blank=False, null=False,
        help_text="Write your description here")

    title = models.CharField(
        max_length=150, blank=False, null=False,
        help_text="Enter a title")

    class Meta:
        abstract = True

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.title


class CommonCategoryFields(models.Model):
    """
    Model representing common fields in 
    Designation, Department, SermonCategory, EventCategory models
    """
    category = models.CharField(max_length=50, blank=False, null=False,)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['date_created']

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.category


class User(AbstractUser, CommonModelInfo):
    title = None
    email = models.EmailField(
        max_length=100, blank=False, null=False, unique=True,
        help_text="Enter a valid Email",
        error_messages={'unique': 'A user with that email already exists.'})

    phone_number = models.PositiveIntegerField(
        blank=False, null=False, unique=True,
        help_text="Enter a valid Email",
        error_messages={'unique': 'The phone number already exists.'})

    password = models.CharField(max_length=100, blank=False, null=False,)
    date_modified = models.DateTimeField(auto_now=True)

    # one to one relationship with Designation
    member_type = models.OneToOneField(
        "Designation", on_delete=models.CASCADE, blank=True, null=True)

    class Meta(CommonModelInfo.Meta):
        ordering = ['date_joined']

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username


class Sermon(CommonModelInfo, CommonCategoryFields):
    """
    Model representing sermons.
    """
    category = None

    # one to many relationship with User
    sermon_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # one to many relationship with sermon category
    sermon_category = models.ForeignKey(
        'SermonCategory', on_delete=models.CASCADE)


class Event(CommonModelInfo, CommonCategoryFields):
    """
    Model representing events and announcements.
    """
    category = None
    event_location = models.CharField(
        max_length=200, blank=False, null=False,
        help_text="Enter the location of the Event")

    event_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()

    # one to many relationship with User
    individual_organized = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # one to many relationship with Department
    department_organized = models.ForeignKey(
        'Department', on_delete=models.CASCADE)


class Department(CommonCategoryFields):
    """
    Model representing Departments in the church
    eg womans guild, PCMF, Choir
    """


class Designation(CommonCategoryFields):
    """
    Model representing membership types in the church
    eg Rev, deacon, member
    """


class EventCategory(CommonCategoryFields):
    """
    Model representing events categories 
    eg Announcements, weddings, crusades, fellowships.
    """


class SermonCategory(CommonCategoryFields):
    """
    Model representing sermon categories
    eg Baptism, national prayers
    """
