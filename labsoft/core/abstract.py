from django.db import models
from django.contrib.auth.models import User

class Base(models.Model):
    "Abstract class to  use the name field in other models"
    name = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract=True

class AuditCreator(models.Model):
    is_prepared = models.BooleanField(default=False)
    prepared_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='+'
    )
    prepared_on = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract=True

class Auditable(models.Model):
    """Abstract auditable model"""
    is_reviewed = models.BooleanField(default=False)
    reviewed_by = models.ForeignKey(
        User,
        blank=True,
        null=True,
        related_name='+'
    )
    reviewed_on = models.DateTimeField(null=True, blank=True)

    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, blank=True, null=True, related_name='+')
    approved_on = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        abstract=True

