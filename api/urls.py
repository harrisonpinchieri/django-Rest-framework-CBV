from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import (
    AlunosViewSet,
    CursosViewSet,
    MatriculasViewSet,
    ListaMatriculasAluno,
    ListaAlunosMatriculados,
)

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculasViewSet, basename="Matriculas")


urlpatterns = [
    path("", include(router.urls)),
    path("aluno/<str:pk>/matriculas", ListaMatriculasAluno.as_view()),
    path("curso/<str:pk>/matriculas", ListaAlunosMatriculados.as_view()),
]
