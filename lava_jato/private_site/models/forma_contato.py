from django.db import models

class FormaContato(models.Model):
    forma_nome = models.CharField(max_length=50)

    class Meta:
        db_table = 'forma_contato'

    def __str__(self):
        return self.forma_nome