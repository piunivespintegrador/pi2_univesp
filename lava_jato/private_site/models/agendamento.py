from django.db import models

class Agendamento(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    is_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.data} {self.hora}"
    
    class Meta:
        app_label = 'mysql'