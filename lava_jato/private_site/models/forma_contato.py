from django.db import models

class FormaContato(models.Model):
    forma_nome = models.CharField(max_length=50)

    def __str__(self):
        return self.forma_nome

    class Meta:
        app_label = 'mysql'