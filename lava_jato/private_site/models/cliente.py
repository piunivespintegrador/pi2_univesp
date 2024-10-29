from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email_contato_1 = models.EmailField()
    telefone_contato_1 = models.CharField(max_length=20)
    telefone_contato_2 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        app_label = 'mysql'