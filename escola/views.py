from rest_framework import viewsets
from .models import Aluno, Curso, Matricula
from .serializer import AlunosSerializer, CursosSerializer, MatriculasSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursosSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
