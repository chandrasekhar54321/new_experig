from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class student_register(models.Model):
	user=models.ForeignKey(User, related_name='student_signup', on_delete=models.CASCADE)
	location=models.CharField(max_length=240)
	type_of_user=models.CharField(max_length=20)