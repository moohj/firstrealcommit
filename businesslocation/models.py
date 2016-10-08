from django.db import models


# Create your models here.
class BusinesSignUp(models.Model):
	"""record and manipulate data for address"""
	"""default={
	"street":'',
	"zip":"",
	"city":"",
	"state":"",
	"country":"",
	"longitude":"",
	"latitude":"",
	}
	set_defaults()"""

	# phone_number = models.CharField(max_length=10, )
	# business_name = models.CharField(max_length=120, )
	# street = models.CharField(max_length=120,)
	# zip_code = models.CharField(max_length=5, )
	# city = models.CharField(max_length=120, )
	# state = models.CharField(max_length=120, )
	# county = models.CharField(max_length=120, )
	# country = models.CharField(max_length=120, default='United States')
	# longitude = models.CharField(max_length=120, )
	# latitude = models.CharField(max_length=120, )

	# def __str__(self):
	# 	return self.business_name
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


		




		