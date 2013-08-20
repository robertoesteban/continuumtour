from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from thumbs import ImageWithThumbsField
import os
from django import forms

# Create your models here.

#path project
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

"""
List option to select the sex
"""
GENDER_CHOICES = (
    ('M',('Masculino')),
    ('F',('Femenimo')),
)


class Speaker(models.Model):
	first_name = models.CharField(_('Nombre'), max_length=100)
	last_name = models.CharField(_('Nombre'), max_length=100)
	birthday = models.DateField(_('Fecha de Nacimiento'), help_text= 'dd/mm/yyyy')
	gender = models.CharField(_('Genero'),max_length=1,choices=GENDER_CHOICES,blank=True, null=True)
	email = models.EmailField(_('Email'),max_length=100,blank=True, null=True)
	avatar =  ImageWithThumbsField(_('Avatar'),upload_to="person/", blank=True, null=True, sizes=((50,50),(200,200)))
	contact = models.CharField(_('Contacto Twitter'), max_length=100,blank=True, null=True)	
	date = models.DateTimeField(_('Fecha'), default=datetime.datetime.today(),editable=False)


	def __unicode__(self):
		return "%s" %(self.full_name())

	def full_name(self):
		return self.first_name + ' ' + self.last_name

	full_name.short_description = _('Nombre Completo')

    	class Meta:
        	verbose_name = _('Nombre Completo')
        	verbose_name_plural = _('Nombre Completo')

