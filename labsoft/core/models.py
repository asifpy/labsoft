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

class SampleRequestor(Base):
    "Information about Employee of Client Company"
    company = ForeignKey('ClientCompany', blank=True,
              null=True, related_name='employees')
    mobile = CharField(max_length=15, blank=True, null=True)
    telephone = CharField(max_length=15, blank=True, null=True)
    email = EmailField(max_length=50, blank=True, null=True)
    address = CharField(max_length=100, blank=True, null=True)
    
    def __unicode__(self):
        return '{} - {}'.format(self.name, self.company.name)
        
class UserProfile(Model):
    """convenience class to relate employee to user."""
    user = OneToOneField(User, related_name='profile')
    requestor = OneToOneField('SampleRequestor', related_name='profile')

class EquipmentType(Base):
    "Actual equipment, eg: Transformer, Generator"
    pass

class Equipment(Model):
    serial_no = CharField(
        max_length=20,
        blank=True,
        null=True,
        unique=True
    )
    id_no = CharField(max_length=20, blank=True, null=True)
    manufacturer_name = CharField(max_length=20, blank=True, null=True)
    manufacturer_country = CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=constants.COUNTRIES
    )
    manufacturer_year = IntegerField(blank=True, null=True)
    equipment_type = ForeignKey(
        'EquipmentType',
        blank=True,
        null=True,
        related_name='equipments'
        )
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
    
    def __unicode__(self):
        return '{}-{}'.format(self.serial_no, self.equipment_type)
    
class EquipmentSample(Model):
    sample_no = IntegerField(unique=True)
    equipment = ForeignKey(
        'Equipment',
        blank=True,
        null=True,
        related_name='samples'
    )
    requestor = ForeignKey(
        'SampleRequestor',
        blank=True,
        null=True,
        related_name='equipments'
    )
    sampling_date = DateField(blank=True, null=True)
    arrival_date = DateField(blank=True, null=True)
    report_date = DateField(blank=True, null=True)
    sampling_from = CharField(max_length=30, blank=True, null=True)
    sampling_reason = CharField(max_length=30, blank=True, null=True)
    oil_temp = CharField(max_length=30, blank=True, null=True)
    unit_in_operation = BooleanField(default=False)
    top_oil_temp = CharField(max_length=30, blank=True, null=True)
    winding_temp = CharField(max_length=30, blank=True, null=True)
    ambient_temp = CharField(max_length=30, blank=True, null=True)
    sample_condition = CharField(
        max_length=20,
        blank=True,
        null=True,
        choices=[
            ('good_condition', 'Good Condition'),
            ('follow_up', 'Follow Up'),
            ('take_action', 'Take Action')
            ])
    sample_action = CharField(max_length=20,
        blank=True,
        null=True,
        choices=[
            ('regeneration', 'Re-generation'),
            ('filtration', 'Filtration'),
            ('de_eneragized', 'De-energized'),
            ('el_tests', 'EL tests')
            ])
    
    ambient_humidity = CharField(max_length=30, blank=True, null=True)
    status = CharField(
        max_length=20,
        blank=True, null=True,
        choices=[
            ('not_started', 'Not Started'),
            ('in_progress', 'In-Progress'),
            ('completed', 'Completed')
            ])
    
    analysis_status = CharField(
        max_length=20,
        blank=True, null=True,
        choices=[
            ('not_started', 'Not Started'),
            ('in_progress', 'In-Progress'),
            ('completed', 'Completed')
            ])
    
    recommendation = TextField(blank=True, null=True)
    
class SampleAnalysis(Model):
    sample = ForeignKey('EquipmentSample', blank=True,
                null=True, related_name='analyses')
    type = CharField(max_length=20,
                     blank=True, null=True,
                     choices=constants.ANALYSIS_TYPES)
    evaluation = TextField(blank=True, null=True)
    notes = TextField(blank=True, null=True)
    
class TestResult(Model):
    pass