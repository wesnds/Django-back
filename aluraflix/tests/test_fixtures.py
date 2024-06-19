from django.test import TestCase
from aluraflix.models import Programa


class FixtureDataTestCase(TestCase):
    fixtures = ["programas_iniciais"]

    def test_fixture_data(self):
        """Testa se os dados do fixture foram carregados"""
        programa_bizarro = Programa.objects.get(pk=1)
        todos_programas = Programa.objects.all()
        self.assertEqual(programa_bizarro.titulo, "Coisas bizarras")
        self.assertEqual(todos_programas.count(), 9)
