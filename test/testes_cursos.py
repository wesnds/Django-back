from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("Cursos-list")
        self.curso_1 = Curso.objects.create(
            codigo_curso="CTT1",
            descricao="Curso teste 1",
            nivel="B",
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso="CTT2",
            descricao="Curso teste 2",
            nivel="A",
        )

    def test_get_cursos(self):
        """Teste para verificar se a lista de cursos está correta"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_curso(self):
        """Teste para verificar se o curso foi criado corretamente"""
        data = {
            "codigo_curso": "CTT3",
            "descricao": "Curso teste 3",
            "nivel": "A",
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Curso.objects.count(), 3)

    def test_delete_curso(self):
        """Teste para verificar DELETE nao permitido"""
        response = self.client.delete(f"/cursos/1/")
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_curso(self):
        """Teste para verificar se o curso foi atualizado"""
        data = {
            "codigo_curso": "CTT1",
            "descricao": "Curso teste 1 atualizado",
            "nivel": "I",
        }
        response = self.client.put(f"/cursos/1/", data=data)
        self.curso_1.refresh_from_db()
        self.assertEqual(self.curso_1.descricao, data["descricao"])
        self.assertEqual(self.curso_1.nivel, data["nivel"])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
