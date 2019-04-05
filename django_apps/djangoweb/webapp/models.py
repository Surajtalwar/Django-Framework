from django.db import models

class Home(models.Model):
	Name = models.CharField(max_length=120)
	class Meta:
		ordering = ('Name',)

	def __str__(self):
		return self.Name
