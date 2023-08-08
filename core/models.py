from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# models.Model è nosso mano que gerencia bancos de dados, esse velho gordo que vai intermediar com o banco de dados.
AGE_CHOICES=(
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_TYPE=(
    ('single','Single'),
    ('seasonal','Seasonal')
)

class CustomUser(AbstractUser):
    profiles=models.ManyToManyField('Profile')


class Profile(models.Model):
    name=models.CharField(max_length=225)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)


    def __str__(self):
        return self.name +" "+self.age_limit
#Essa gracinha aqui esta complicando minha vida então vou reescrever e resetar as migrates.
class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    #ManyToManyField ta lincando esssa porra a varios videos diferentes, talvez isso seja eficiente para series?
    videos=models.ManyToManyField('Video')
    #o valor Defaul vai evitar um erro idiota
    flyer=models.ImageField(upload_to='flyers',blank=True,null=True, default= 'media/flyers/erro.png')
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)
    '''

class Movie(models.Model):
    title:str=models.CharField(max_length=225)
    description:str=models.TextField()
    uuid=models.UUIDField(default=uuid.uuid4,unique=True)
    created =models.DateTimeField(auto_now_add=True)
    type=models.CharField(max_length=10,choices=MOVIE_TYPE)
    file=models.FileField(upload_to='movies')
    flyer=models.CharField(max_length=2250)
    age_limit=models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True, default= 'All')
'''

class Video(models.Model):
    title:str = models.CharField(max_length=225,blank=True,null=True)
    file=models.FileField(upload_to='movies')
    
    

    

