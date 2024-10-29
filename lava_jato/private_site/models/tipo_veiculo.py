from django.db import models

class TipoVeiculo(models.Model):
    nome_veiculo = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_veiculo
    
    class Meta:
        app_label = 'mysql'