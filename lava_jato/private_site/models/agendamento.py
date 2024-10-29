from django.db import models

class Agendamento(models.Model):
    datetime_inicio = models.DateTimeField()
    datetime_fim = models.DateTimeField()
    disponivel = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'agendamento'

    def __str__(self):
        return f"{self.datetime_inicio} {self.datetime_fim} {self.disponivel}"