from rest_framework import viewsets, generics, authentication, permissions
from .models import Aluno, Curso, Matricula
from .serializer import (
    AlunosSerializer,
    CursosSerializer,
    MatriculasSerializer,
    ListaMatriculasAlunoSerializer,
    ListaAlunosMatriculadosCursoSerializer,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()
    serializer_class = AlunosSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursosSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    # self -> referencia a instancia da classe usada (aluno)
    # kwargs -> dicionario com os parametros passados na url
    # aluno_id=self.kwargs["pk"] -> pega o id do aluno passado na url
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListaAlunosMatriculadosCurso(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaAlunosMatriculadosCursoSerializer
    authentication_classes = [authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
