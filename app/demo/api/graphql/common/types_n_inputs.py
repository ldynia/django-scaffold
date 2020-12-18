from graphene_django_extras import DjangoListObjectType
from graphene_django_extras import DjangoObjectType
from graphene_django_extras import DjangoSerializerMutation
from rest_framework import serializers

from demo.models import Dummy


class DummyType(DjangoObjectType):

    class Meta:
        model = Dummy
        description = 'Type definition for a single Dummy.'
        filter_fields = {
            'id': ('exact',),
            'day': ('icontains', 'iexact'),
            'weekday': ('icontains', 'iexact'),
            'month': ('icontains', 'iexact'),
            'year': ('icontains', 'iexact'),
            'pre_seeded': ('exact',),
            'created_at': ('icontains', 'iexact'),
            'updated_at': ('icontains', 'iexact'),
        }


class DummyListType(DjangoListObjectType):

    class Meta:
        model = Dummy
        description = 'Type definition for Dummy list.'
        filter_fields = {
            'id': ('exact',),
            'day': ('icontains', 'iexact'),
            'weekday': ('icontains', 'iexact'),
            'month': ('icontains', 'iexact'),
            'year': ('icontains', 'iexact'),
            'pre_seeded': ('exact',),
            'created_at': ('icontains', 'iexact'),
            'updated_at': ('icontains', 'iexact'),
        }


class DummySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Dummy
        fields = ['day', 'weekday', 'month', 'year', 'pre_seeded']


class DummySerializerMutation(DjangoSerializerMutation):
    
    class Meta:
        serializer_class = DummySerializer
        description = "Django Rest Framework serializer based Mutation for Dummy"
