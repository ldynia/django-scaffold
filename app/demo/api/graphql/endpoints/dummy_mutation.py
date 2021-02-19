import graphene
from graphene_django_extras import DjangoSerializerMutation
from rest_framework.serializers import ModelSerializer

from demo.models import Dummy


class DummySerializer(ModelSerializer):

    class Meta:
        model = Dummy
        fields = ['day', 'weekday', 'month', 'year', 'pre_seeded']


class DummySerializerMutation(DjangoSerializerMutation):

    class Meta:
        serializer_class = DummySerializer
        description = "Django Rest Framework serializer based Mutation for Dummy."


class DummyMutations(graphene.ObjectType):
    create_dummy = DummySerializerMutation.CreateField()
    update_dummy = DummySerializerMutation.UpdateField()
    delete_dummy = DummySerializerMutation.DeleteField()