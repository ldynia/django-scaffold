import graphene

from graphene_django_extras import DjangoListObjectField
from graphene_django_extras import DjangoListObjectType
from graphene_django_extras import DjangoObjectField
from graphene_django_extras import DjangoObjectType

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


class DummyQuery(graphene.ObjectType):
    dummy_by_id = DjangoObjectField(DummyType, description='Single Dummy query.')
    all_dummy = DjangoListObjectField(DummyListType, description='All Dummy query.')\
