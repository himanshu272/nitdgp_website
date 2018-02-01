from django.db import models
import datetime
import uuid

class Department(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name=models.CharField(max_length=255)
	short_code=models.CharField(max_length=4)
	about_us=models.TextField()

class Faculty(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name=models.CharField(max_length=255)
	research_interest=models.TextField()
	email=models.CharField(max_length=255,default="")
	mobile=models.IntegerField()
	joining_year=models.DateField(auto_now_add=True)
	department=models.ForeignKey(Department,on_delete=models.CASCADE)

class Research(models.Model):
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	department=models.ForeignKey(Department,on_delete=models.CASCADE)
	collab_inst=models.TextField()
	area=models.CharField(max_length=255)
	faculty_involved=models.TextField()
	date=models.DateField(auto_now_add=True)

class Electives(models.Model):
	id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
	short_code=models.CharField(max_length=7) #for example if an elective is MME 461 total size is 7 including the space
	title=models.CharField(max_length=200)
	is_open=models.BooleanField(default=True)
	department=models.ForeignKey(Department,on_delete=models.CASCADE)

class FacultyRoles(models.Model):
	department=models.ForeignKey(Department,on_delete=models.CASCADE)
	faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    #role=models.ForeignKey(Roles,on_delete=models.CASCADE)

# class Roles(models.Model):
# # Create your models here.
#     pass
