from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Raca(models.Model):
    raca = models.CharField('Raça', max_length=50)

    def __str__(self) -> str:
        return self.raca
    
class Tag(models.Model):
    tag = models.CharField('Tag', max_length=100)

    def __str__(self) -> str:
        return self.tag
    
class Pet(models.Model):
    choices_status = (('P', 'Para adoção'), 
                      ('A', 'Adotado'))
    
    state_choice = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
        ('DF', 'Distrito Federal'),
    )
    
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to="fotos_pets")
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField()
    estado = models.CharField('Estado', max_length=50, choices=state_choice)
    cidade = models.CharField('Cidade', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)
    tags = models.ManyToManyField(Tag)
    raca = models.ForeignKey(Raca, on_delete=models.DO_NOTHING)
    status = models.CharField('Status', max_length=1, choices=choices_status, default='P')

    def __str__(self) -> str:
        return self.nome