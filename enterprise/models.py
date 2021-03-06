from django.db import models
from users.managers import CustomUserManager
from users.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

class Enterprise(models.Model):
	id=models.AutoField(primary_key=True)
	user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name='enterprise')
	contact_name=models.CharField(max_length=200)
	phone=models.CharField(max_length=10)
	shop_name=models.CharField(max_length=200)
	gst_number=models.CharField(max_length=20,unique=True)
	shop_address=models.CharField(max_length=400)
	#shop_photo=models.ImageField(upload_to='images/')
	created_at = models.DateTimeField(auto_now_add=True)
	#updated_at = models.DateTimeField(auto_now_add=True)
	objects = CustomUserManager()

	def __str__(self):
		return str(self.id)

@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Enterprise.objects.create(user=instance,contact_name=instance.contact_name,
			phone=instance.phone,shop_name=instance.shop_name,gst_number=instance.gst_number,
			shop_address=instance.shop_address)

@receiver(post_save,sender=CustomUser)
def save_profile(sender,instance,**kwargs):
	try:
		instance.enterprise.save()
	except ObjectDoesNotExist:
		Enterprise.objects.create(user=instance)
