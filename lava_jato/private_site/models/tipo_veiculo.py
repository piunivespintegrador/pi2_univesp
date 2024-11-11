from django.db import models

class TipoVeiculo(models.Model):
    nome_veiculo = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tipo_veiculo'

    def __str__(self):
        return f"{self.nome_veiculo}"