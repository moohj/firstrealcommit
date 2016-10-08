from django.db import models

# Create your models here.
class DataMine(models.Model):
	"""docstring for DataMine"""
	
	

	income_less_than_10k = models.PositiveIntegerField()
	income_10_15 = models.PositiveIntegerField()
	income_15_20 = models.PositiveIntegerField()
	income_20_25 = models.PositiveIntegerField()
	income_25_30 = models.PositiveIntegerField()
	income_30_35 = models.PositiveIntegerField()
	income_35_40 = models.PositiveIntegerField()
	income_40_45 = models.PositiveIntegerField()
	income_45_50 = models.PositiveIntegerField()
	income_50_60 = models.PositiveIntegerField()
	income_60_75 = models.PositiveIntegerField()
	income_75_100 = models.PositiveIntegerField()
	income_100_125 = models.PositiveIntegerField()
	income_125_150 = models.PositiveIntegerField()
	income_150_200 = models.PositiveIntegerField()
	income_greater_than_200 = models.PositiveIntegerField()

	f_15_17 = models.PositiveIntegerField()
	f_18_19 = models.PositiveIntegerField()
	f_20 = models.PositiveIntegerField()
	f_21 = models.PositiveIntegerField()
	f_22_24 = models.PositiveIntegerField()
	f_25_29 = models.PositiveIntegerField()
	f_30_34 = models.PositiveIntegerField()
	f_35_39 = models.PositiveIntegerField()
	f_40_44 = models.PositiveIntegerField()
	f_45_49 = models.PositiveIntegerField()
	f_50_54 = models.PositiveIntegerField()
	f_55_59 = models.PositiveIntegerField()
	f_60_61 = models.PositiveIntegerField()
	f_62_64 = models.PositiveIntegerField()
	f_65_66 = models.PositiveIntegerField()
	f_67_69 = models.PositiveIntegerField()
	f_70_74 = models.PositiveIntegerField()
	f_75_79 = models.PositiveIntegerField()
	f_80_84 = models.PositiveIntegerField()
	f_g_85 = models.PositiveIntegerField()

	m_15_17 = models.PositiveIntegerField()
	m_18_19 = models.PositiveIntegerField()
	m_20 = models.PositiveIntegerField()
	m_21 = models.PositiveIntegerField()
	m_22_24 = models.PositiveIntegerField()
	m_25_29 = models.PositiveIntegerField()
	m_30_34 = models.PositiveIntegerField()
	m_35_39 = models.PositiveIntegerField()
	m_40_44 = models.PositiveIntegerField()
	m_45_49 = models.PositiveIntegerField()
	m_50_54 = models.PositiveIntegerField()
	m_55_59 = models.PositiveIntegerField()
	m_60_61 = models.PositiveIntegerField()
	m_62_64 = models.PositiveIntegerField()
	m_65_66 = models.PositiveIntegerField()
	m_67_69 = models.PositiveIntegerField()
	m_70_74 = models.PositiveIntegerField()
	m_75_79 = models.PositiveIntegerField()
	m_80_84 = models.PositiveIntegerField()
	m_g_85 = models.PositiveIntegerField()

	school_enrollment_male_ug = models.PositiveIntegerField()
	school_enrollment_male_grad = models.PositiveIntegerField()
	school_enrollment_female_ug = models.PositiveIntegerField()
	school_enrollment_female_grad = models.PositiveIntegerField()

	blue_collar = models.PositiveIntegerField()
	white_collar = models.PositiveIntegerField()
	pink_collar = models.PositiveIntegerField()


	numb_bars = models.PositiveIntegerField()
	numb_restaurants = models.PositiveIntegerField()
	
	def __str__(self):
		return str(self.population_total_female_asian)
		