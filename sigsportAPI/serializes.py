from rest_framework import serializers

from .models import Matricula, Modalidade, CategoriaModalidade


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nomeAluno', 'matricula', 'modalidade','tipoCategoria',)
        model = Matricula

class ModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'nomeModalidade', 'descricao',)
        model = Modalidade

class CategoriaModalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'categoria', 'descricao',)
        model = CategoriaModalidade