from django.db import models
from datetime import datetime, date

# Create your models here.

class Room(models.Model):
	id = models.AutoField(primary_key=True)
	phone = models.CharField('Phone', max_length=50, null=True, blank=True)

	def __str__(self):
		return str(self.id)


	class Meta:
		verbose_name = 'Room'
		verbose_name_plural = 'Rooms'


class MedCard(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField('Name', max_length=50, unique=True, null=True, blank=True)
	diagnos = models.CharField('Diagnos', max_length=50, null=True, blank=True)
	cause = models.CharField('Cause', max_length=50, null=True, blank=True)
	other = models.CharField('Other', max_length=50, null=True, blank=True)
	gender = models.CharField('Gender', max_length=1, null=True, blank=True)
	age = models.IntegerField('Age', null=True, blank=True)
	date = models.DateField('Date', auto_now_add=False, auto_now=False, blank=True, null=True, default='')

	def __str__(self):
		return str(self.id)


	class Meta:
		verbose_name = 'MedCard'
		verbose_name_plural = 'MedCards'


class Move(models.Model):
	id = models.AutoField(primary_key=True)
	medCard = models.ForeignKey(MedCard, on_delete=models.CASCADE)
	room = models.ForeignKey(Room, on_delete=models.CASCADE)
	date = models.DateField('Date', auto_now_add=False, auto_now=False, blank=True, null=True, default='')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Move'
		verbose_name_plural = 'Move'

class Healthy(models.Model):
	id = models.AutoField(primary_key=True)
	medCard = models.ForeignKey(MedCard, on_delete=models.CASCADE)
	discription = models.CharField('Discription', max_length=50, blank=True, null=True)
	date = models.DateField('Date', auto_now_add=False, auto_now=False, blank=True, null=True, default='')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Healthy'
		verbose_name_plural = 'Healthy'

