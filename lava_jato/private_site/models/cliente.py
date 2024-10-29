from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email_contato_1 = models.EmailField()
    email_contato_2 = models.EmailField(null=True, blank=True)
    telefone_contato_1 = models.CharField(max_length=20)
    telefone_contato_2 = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'cliente'

    def __str__(self):
        return f"{self.nome} {self.email_contato_1} {self.telefone_contato_1}"