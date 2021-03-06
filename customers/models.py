from django.db import models
from users.managers import CustomUserManager
from enterprise.models import Enterprise
from phone_field import PhoneField
# Create your models here

class Customer(models.Model):

	class Meta:
		verbose_name_plural = "Customers"

	id=models.AutoField(primary_key=True)
	enterprise=models.ForeignKey(Enterprise,on_delete=models.CASCADE,related_name='customer',blank=True,null=True)
	customer_name=models.CharField(max_length=100,blank=True)
	customer_email=models.EmailField(null=True,blank=True,unique=True)
	customer_phone = PhoneField(blank=True, help_text='Contact phone number',E164_only=False,unique=True)
	customer_address=models.CharField(max_length=200)
	

	objects=CustomUserManager()

	def __str__(self):
		return f"{self.id} {self.enterprise} - {self.customer_name} {self.customer_phone}"

