from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from escola.views import (
    AlunosViewSet,
    CursosViewSet,
    MatriculasViewSet,
    ListaMatriculasAluno,
    ListaAlunosMatriculadosCurso,
)

router = routers.DefaultRouter()
router.register("alunos", AlunosViewSet, basename="Alunos")
router.register("cursos", CursosViewSet, basename="Cursos")
router.register("matriculas", MatriculasViewSet, basename="Matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("alunos/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("cursos/<int:pk>/matriculas/", ListaAlunosMatriculadosCurso.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
