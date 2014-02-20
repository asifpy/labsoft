from django.db.models import *
from django.contrib.auth.models import User

class Base(Model):
    "Abstract class to  use the name field in other models"
    name = CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract=True

class ClientCompany(Base):
    "Represents client company"
    pass

class ClientEmployee(Base):
    "Information about Employee of Client Company"
    company = ForeignKey('ClientCompany', blank=True, null=True, related_name='employees')
    mobile = CharField(max_length=15, blank=True, null=True)
    telephone = CharField(max_length=15, blank=True, null=True)
    email = EmailField(max_length=50, blank=True, null=True)
    address = CharField(max_length=100, blank=True, null=True)

class UserProfile(Model):
    """convenience class to relate employee to user."""
    user = OneToOneField(User, related_name='profile')
    employee = OneToOneField('ClientEmployee', related_name='profile')
    
class Transformer(Model):
    pass

class SampleData(Model):
    pass

class Analysis(Model):
    pass

class TestResult(Model):
    pass