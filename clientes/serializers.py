from rest_framework import serializers
from clientes.models import Cliente
from .validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

    def validate(self, data):
        if not cpf_valido(data["cpf"]):
            raise serializers.ValidationError({"cpf": "CPF inválido"})

        if not nome_valido(data["nome"]):
            raise serializers.ValidationError({"nome": "Nome inválido"})

        if not rg_valido(data["rg"]):
            raise serializers.ValidationError({"rg": "RG inválido"})

        if not celular_valido(data["telefone_fixo"]):
            raise serializers.ValidationError(
                {"celular": "Número de telefone inválido. Siga o modelo: 99 99999-9999"}
            )

        return data
