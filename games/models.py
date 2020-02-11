from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    url = models.URLField(default = '', max_length = 200)
    developer = models.ForeignKey('users.Developer', on_delete = models.CASCADE, related_name = 'games')

    def __str__(self):
	    return self.title
