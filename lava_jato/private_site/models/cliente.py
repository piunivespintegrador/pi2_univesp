from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    placa_carro = models.CharField(max_length=20, default="ABC1D23")
    email_contato_1 = models.EmailField(max_length=200)
    email_contato_2 = models.EmailField(max_length=200, null=True, blank=True)
    telefone_contato_1 = models.CharField(max_length=26)
    telefone_contato_2 = models.CharField(max_length=26, null=True, blank=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f"{self.nome} {self.placa_carro} {self.email_contato_1} {self.telefone_contato_1}"