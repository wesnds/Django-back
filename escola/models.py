from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome


class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )
    codigo_curso = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    nivel = models.CharField(
        max_length=1,
        choices=NIVEL,
        blank=False,
        null=False,
        default="B",
    )

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
    PERIODO = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    )

    # .CASCADE -> se deletar um aluno/curso, deleta a matricula
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1,
        choices=PERIODO,
        blank=False,
        null=False,
        default="M",
    )

    def __str__(self):
        return f"{self.aluno} está matriculado em {self.curso}"
