from django.urls import path
#from .views import ListarModalidades, ListarCategorias, FazerMatricula
from . import views
app_name = 'sigsportAPI'



urlpatterns = [
    path('M<int:pk>/', views.ListarModalidades.as_view()),
    path('C<int:pk>/', views.ListarCategorias.as_view()),
    path('', views.FazerMatricula.as_view()),
    path('modalidade', views.ListarModalidades.as_view()),
]

'''
urlpatterns = [
    path('', FazerMatricula.as_view()),
]
'''