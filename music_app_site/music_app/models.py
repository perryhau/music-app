from django.db import models

class Contact(models.Model):
	first_name = models.CharField(max_length=300)
	family_name = models.CharField(max_length=300)

