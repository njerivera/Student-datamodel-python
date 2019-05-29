from django.db import models

class Student(models.Model):
	first_name = models.CharFiled(max_length=50)
	last_name= models.CharFiled(max_length=50)
	date_of_birth = models.DateFiled()
	registration_number = models.CharFiled(max_length=50)
	place_of_residence = models.CharFiled(max_length=50)
	email= models.CharFiled(max_length=50)
	guardian_phone = models.CharFiled(max_length=50)
	id_number=models.CharFiled()
	date_joined = models.IntegerFiled()

