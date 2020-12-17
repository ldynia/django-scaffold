from graphene_django_extras import DjangoObjectType, DjangoListObjectType, DjangoInputObjectType
from graphene_django_extras.paginations import LimitOffsetGraphqlPagination

from demo.models import Dummy


import django_filters as filters


class DummyFilterSet(filters.FilterSet):
    class Meta:
        model = Dummy
        fields = {
            'id': ('exact',),
            'day': ('icontains', 'iexact'),
            'weekday': ('icontains', 'iexact'),
            'month': ('icontains', 'iexact'),
            'year': ('icontains', 'iexact'),
            'pre_seeded': ('exact',),
            'created_at': ('icontains', 'iexact'),
            'updated_at': ('icontains', 'iexact'),
        }

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
        exclude_fields: {}


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
        exclude_fields: {}


class DummyInput(DjangoInputObjectType):
    
    class Meta:
        model = Dummy
        description = "Dummy InputType definition to dummy as input on an Arguments class on traditional Mutations"
