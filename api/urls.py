from django.urls import path, include
from . import views
from rest_framework import routers
from api.views import AlunosViewSet, CursosViewSet

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")


urlpatterns = [
    path(
        "",
        include(router.urls),
    )
]
