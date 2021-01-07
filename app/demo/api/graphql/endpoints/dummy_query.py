import graphene
from graphene_django_extras import DjangoObjectField, DjangoListObjectField

from demo.api.graphql.endpoints.dummy_common import DummyType
from demo.api.graphql.endpoints.dummy_common import DummyListType


class DummyQuery(graphene.ObjectType):
    dummy_by_id = DjangoObjectField(DummyType, description='Single Dummy query')
    all_dummy = DjangoListObjectField(DummyListType, description='All Dummy query')