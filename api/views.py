from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializers import AlunoSerializer, CursoSerialzier


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os launos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """exibindo todos os cursos"""

    query_set = Curso.objects.all()
    serializer_class = CursoSerialzier
