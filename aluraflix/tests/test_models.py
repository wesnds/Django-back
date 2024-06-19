from django.test import TestCase
from aluraflix.models import Programa


class ProgramaModelTestCase(TestCase):
    def setUp(self):
        self.programa = Programa(
            titulo="teste",
            tipo="S",
            data_lancamento="2024-06-19",
            likes=666,
        )

    def test_verifica_atributos(self):
        """Verifica os atrivutos de um programa com valores default"""
        self.assertEqual(self.programa.titulo, "teste")
        self.assertEqual(self.programa.tipo, "S")
        self.assertEqual(self.programa.data_lancamento, "2024-06-19")
        self.assertEqual(self.programa.likes, 666)
        self.assertEqual(self.programa.dislikes, 0)
