# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import uuid

from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import AbstractUser, Group, Permission


#Cartas
class Cartas(models.Model):
	carta = models.CharField(max_length=100, verbose_name='carta')
	efeito = models.BooleanField(verbose_name='efeito')
	cor = models.CharField(max_length=100, verbose_name='cor')
	descricao = models.TextField(null = True, blank=True, verbose_name='efeito da carta')
	foto = models.ImageField(verbose_name='foto', upload_to='cartas')



#Usuário
class User(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Partida(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	cartas = models.ForeignKey(Cartas, on_delete=models.CASCADE)