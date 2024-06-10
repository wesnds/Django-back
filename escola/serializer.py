from rest_framework import serializers

from .models import Aluno, Curso, Matricula


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


class MatriculasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaAlunosMatriculadosCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source="aluno.nome")

    class Meta:
        model = Matricula
        fields = ["aluno_nome"]


class AlunosSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            "id",
            "nome",
            "celular",
            "rg",
            "cpf",
            "data_nascimento",
        ]
