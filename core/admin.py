from django.contrib import admin
# from django.contrib import admin: Isso importa o módulo admin fornecido pelo Django,
#  que é responsável pela criação e gerenciamento do painel de administração.
from .models import CustomUser,Profile,Movie,Video
# models já é um arquivo do proprio sistema que usamos para preparar o terrreno para essa pagina
# Register your models here.
admin.site.register(CustomUser)
#admin.site.register(CustomUser): Isso registra o modelo CustomUser no painel de .
# administração do Django. Isso significa que você poderá gerenciar os registros do modelo 
# CustomUser (provavelmente relacionados a usuários personalizados) diretamente no painel de administração,
#  em vez de interagir diretamente com o banco de dados.
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)

# Esse arquivo esta instanciando as Viwers que seram geradas para ser a area de admin, porem tudo pre-fabricado.