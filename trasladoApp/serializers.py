from rest_framework import routers, serializers, viewsets
from trasladoApp.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'is_staff')

class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MotoristaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'

class DepartamentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class FuncionarioSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many = False)
    class Meta:
        model = Funcionario
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('usuario')
        u = User.objects.create(**user_data)
        f = Funcionario.objects.create(usuario = u, **validated_data)
        return f

class SolicitarSerializer(serializers.HyperlinkedModelSerializer):
    #funcionarios = FuncionarioSerializer(many = False)
    class Meta:
        model = Solicitar
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('funcionarios')
        s = Solicitar.objects.create(**validated_data)
        return s

class AtenderSerializer(serializers.HyperlinkedModelSerializer):
    #motorista = MotoristaSerializer(many = False)
    #veiculo = VeiculoSerializer(many = False)
    class Meta:
        model = Atender
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('motorista')
        user_data2 = validated_data.pop('veiculo')
        a = Atender.objects.create(**validated_data)
        return a
