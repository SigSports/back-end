from django.db import models

# Create your models here.

class Bolsista(models.Model):
    nome = models.CharField(max_length=40)
    matricula = models.CharField(max_length=40)
    turno = models.CharField(max_length=40)
    email = models.CharField(max_length=35)
    
class Modalidade(models.Model):
    nomeModalidade = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.nomeModalidade}'
    
class CategoriaModalidade(models.Model):
    categoria = models.CharField(max_length=40)
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.categoria}'
    

class Matricula(models.Model):
    nomeAluno = models.CharField(max_length=120)
    matricula = models.CharField(max_length=120)
    modalidade = models.ForeignKey(Modalidade, on_delete = models.CASCADE)
    tipoCategoria = models.ForeignKey(CategoriaModalidade, on_delete = models.CASCADE, default=0)
    #dataInscricao = models.DateTimeField(auto_now_add=True, blank=True)
    autorizado = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nomeAluno}'
    


    

