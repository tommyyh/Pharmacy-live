from django.db import models

class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	time = models.CharField(max_length=255, null=True)
	postal_code = models.CharField(max_length=100, null=True)
	nhs_number = models.CharField(max_length=255, null=True)
	birth_date = models.DateField(null=True)
	date = models.DateField()
	has_texted = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.name}: {self.date} - {self.time}'
