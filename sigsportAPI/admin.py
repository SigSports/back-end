from django.contrib import admin
from .models import Bolsista, Modalidade, CategoriaModalidade, Matricula
# Register your models here.

admin.site.register(Bolsista)
admin.site.register(Modalidade)
admin.site.register(CategoriaModalidade)
admin.site.register(Matricula)