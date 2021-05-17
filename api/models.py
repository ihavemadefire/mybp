from django.db import models
import uuid

# Create your models here.

class Patient(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.first_name + " " + self.middle_name[0] + " " + self.last_name
  
class Reading(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  diastol = models.IntegerField(null=True)
  systol = models.IntegerField(null=True)
  weight = models.IntegerField(null=True)
  patient = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)


class Doctor(models.Model):
  id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
  first_name = models.CharField(max_length=200, null=True)
  middle_name = models.CharField(max_length=200, null=True)
  last_name = models.CharField(max_length=200, null=True)
  

  def __str__(self):
    return self.first_name + " " + self.middle_name[0] + " " + self.last_name