from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Aluno, Curso, Matricula
from .serializer import (
    AlunosSerializer,
    CursosSerializer,
    MatriculasSerializer,
    ListaMatriculasAlunoSerializer,
    ListaAlunosMatriculadosCursoSerializer,
    AlunosSerializerV2,
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""

    queryset = Aluno.objects.all()

    def get_serializer_class(self):
        if self.request.version == "v2":
            return AlunosSerializerV2
        else:
            return AlunosSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""

    queryset = Curso.objects.all()
    serializer_class = CursosSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
    ]

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data["id"])
            response["Location"] = request.build_absolute_uri() + id
            return response


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""

    queryset = Matricula.objects.all()
    serializer_class = MatriculasSerializer
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
    ]

    @method_decorator(cache_page(20))
    def dispatch(self, *args, **kwargs):
        return super(MatriculasViewSet, self).dispatch(*args, **kwargs)


class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""

    # self -> referencia a instancia da classe usada (aluno)
    # kwargs -> dicionario com os parametros passados na url
    # aluno_id=self.kwargs["pk"] -> pega o id do aluno passado na url
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculadosCurso(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaAlunosMatriculadosCursoSerializer
