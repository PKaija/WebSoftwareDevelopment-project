# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User, AbstractUser
from django.db import models



class Account(AbstractUser):
	account_types = (
			('DEV', 'developer'),
			('PLR', 'player')
		)
	bio = models.TextField(blank = True, default = '', max_length = 1000)
	account_type = models.CharField(max_length = 3, choices = account_types, default = 'PLR')
	owned_games = models.ManyToManyField('games.Game')
	class Meta:
		permissions = (
			("can_buy_game", "Can buy game"),
			("can_play_game", "Can play game")
		)

class Developer(models.Model):
	user = models.OneToOneField(Account, on_delete = models.CASCADE, primary_key = True)
	class Meta:
		permissions = (
			("can_add_game", "Can add game"),
			("can_remove_own_game", "Can remove own game"),
		)

class Player(models.Model):
	user = models.OneToOneField(Account, on_delete = models.CASCADE, primary_key = True)
