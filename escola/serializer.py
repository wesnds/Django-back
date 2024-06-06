from rest_framework import serializers

from .models import Aluno, Curso


# converte para forma nativa do python, para o ORM entender
class AlunosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            "id",
            "nome",
            "rg",
            "cpf",
            "data_nascimento",
        ]


class CursosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"
