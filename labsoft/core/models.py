from django.db.models import *
from django.contrib.auth.models import User

from labsoft.core import constants

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
    company = ForeignKey('ClientCompany', blank=True,
              null=True, related_name='employees')
    mobile = CharField(max_length=15, blank=True, null=True)
    telephone = CharField(max_length=15, blank=True, null=True)
    email = EmailField(max_length=50, blank=True, null=True)
    address = CharField(max_length=100, blank=True, null=True)

class UserProfile(Model):
    """convenience class to relate employee to user."""
    user = OneToOneField(User, related_name='profile')
    employee = OneToOneField('ClientEmployee', related_name='profile')

class EquipmentType(Base):
    "Actual equipment, eg: Transformer, Generator"
    pass

class Equipment(Model):
    serial_no = CharField(max_length=20, blank=True, null=True, unique=True)
    id_no = CharField(max_length=20, blank=True, null=True)
    manufacturer_name = CharField(max_length=20, blank=True, null=True)
    manufacturer_country = CharField(max_length=20,
                           blank=True, null=True,
                           choices=constants.COUNTRIES)
    manufacturer_year = IntegerField(blank=True, null=True)
    equipment_type = ForeignKey('EquipmentType', blank=True,
                     null=True, related_name='equipments')
    contact_person = ForeignKey('ClientEmployee', blank=True,
                     null=True, related_name='equipments')
    station_name = CharField(max_length=20, blank=True, null=True)
    location = CharField(max_length=20, blank=True, null=True)
    operated_power_rate = CharField(max_length=20, blank=True, null=True)
    load = CharField(max_length=20, blank=True, null=True)
    operating_period = CharField(max_length=20, blank=True, null=True)
    phase_no = CharField(max_length=20, blank=True, null=True)
    tension = CharField(max_length=20, blank=True, null=True)
    oil_type = CharField(max_length=20, blank=True, null=True)
    cooling_type = CharField(max_length=20, blank=True, null=True)
    oil_weight = CharField(max_length=20, blank=True, null=True)
    tc_type = CharField(max_length=20, blank=True, null=True)
    sealing_system = CharField(max_length=20, blank=True, null=True)
    tc_chamber = CharField(max_length=20, blank=True, null=True)

class EquipmentSample(Model):
    sample_no = IntegerField()
    equipment = ForeignKey('Equipment', blank=True,
                null=True, related_name='samples')
    sampling_date = DateField(blank=True, null=True)
    arrival_date = DateField(blank=True, null=True)
    report_date = DateField(blank=True, null=True)
    sampling_from = CharField(max_length=30, blank=True, null=True)
    sampling_reason = CharField(max_length=30, blank=True, null=True)
    oil_temp = CharField(max_length=30, blank=True, null=True)

class Analysis(Model):
    pass

class TestResult(Model):
    pass