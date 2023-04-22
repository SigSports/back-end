from rest_framework import generics

from .models import Matricula, Modalidade, CategoriaModalidade
from .serializes import MatriculaSerializer, ModalidadeSerializer, CategoriaModalidadeSerializer
# Create your views here.

class ListarModalidades(generics.ListCreateAPIView):
    queryset = Modalidade.objects.all()
    serializer_class = ModalidadeSerializer


class ListarCategorias(generics.ListCreateAPIView):
    queryset = CategoriaModalidade.objects.all()
    serializer_class = CategoriaModalidadeSerializer


class FazerMatricula(generics.ListCreateAPIView):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer