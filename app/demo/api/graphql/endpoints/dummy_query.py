import graphene
from graphene_django_extras import DjangoObjectField, DjangoListObjectField, DjangoFilterPaginateListField, DjangoFilterListField, LimitOffsetGraphqlPagination

from demo.api.graphql.common.types_n_inputs import DummyType
from demo.api.graphql.common.types_n_inputs import DummyListType


class DummyQuery(graphene.ObjectType):
    dummy_by_id = DjangoObjectField(DummyType, description='Single Dummy query')
    all_dummy = DjangoListObjectField(DummyListType, description='All Dummy query')