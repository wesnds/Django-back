from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer


class ProgramaSerializerTestCase(TestCase):
    def setUp(self):
        self.programa = Programa.objects.create(
            titulo="Programa de teste",
            tipo="F",
            data_lancamento="2021-01-01",
            likes=10,
            dislikes=5,
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verifica_campos_serializados(self):
        """Verifica os campos serializados"""

        # pegando campos do serializer
        data = self.serializer.data

        # set garante saída do serializer com as chaves exatas esperadas
        self.assertEqual(
            set(data.keys()),
            set(
                [
                    "titulo",
                    "tipo",
                    "data_lancamento",
                    "likes",
                ]
            ),
        )

    def test_verifica_conteudo_campos_serializados(self):
        """Verifica o conteúdo dos campos serializados"""

        data = self.serializer.data

        self.assertEqual(data["titulo"], "Programa de teste")
        self.assertEqual(data["tipo"], "F")
        self.assertEqual(data["data_lancamento"], "2021-01-01")
        self.assertEqual(data["likes"], 10)
        self.assertNotIn("dislikes", data)
