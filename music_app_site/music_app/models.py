from django.db import models
from music21 import *




class Contact(models.Model):
	first_name = models.CharField(max_length=300)
	family_name = models.CharField(max_length=300)

	def createNote():
		c3 = note.Note()

	def __unicode__(self):
		return self.first_name