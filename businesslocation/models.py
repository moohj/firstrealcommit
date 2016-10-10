from django.db import models


# Create your models here.
class BusinesSignUp(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=120, )
	email = models.EmailField(max_length=120, )
	name_types = (
        ('bus','Business' ),
        ('pers','Personal'),
     )
	name_type = models.CharField(
        max_length=8,
        choices=name_types,
        default='Business',
    )


	def __str__(self):
	 	return self.name


		




		