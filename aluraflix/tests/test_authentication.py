from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import force_authenticate
from aluraflix.views import ProgramaViewSet


class UserAuthenticationTestCase(TestCase):
    def setUp(self):
        self.list_url = reverse("programas-list")
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
        )

    def test_user_authentication(self):
        """Testa autenticação de usuário com credenciais corretas"""
        user = authenticate(username="testuser", password="testpassword")
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica requisicao GET sem autenticacao"""

        # client é disponibilizado pelo apitestcase
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_username_incorreto(self):
        """Testa autenticação com username incorreto"""
        user = authenticate(
            username="testuser_errado",
            password="testpassword",
        )
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_password_incorreto(self):
        """Testa autenticação com username incorreto"""
        user = authenticate(
            username="testuser",
            password="testpassword_errado",
        )
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_get_authenticated_user(self):
        """Testa requisicao GET com user autenticado"""
        factory = RequestFactory()
        user = User.objects.get(username="testuser")
        view = ProgramaViewSet.as_view({"get": "list"})

        request = factory.get(self.list_url)
        force_authenticate(request, user=user)
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
