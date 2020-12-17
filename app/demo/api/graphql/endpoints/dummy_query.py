import graphene
from graphene_django_extras import DjangoObjectField, DjangoListObjectField, DjangoFilterPaginateListField, DjangoFilterListField, LimitOffsetGraphqlPagination

from demo.api.graphql.common.types import DummyType
from demo.api.graphql.common.types import DummyListType
from demo.api.graphql.common.types import DummyFilterSet


class DummyQuery(graphene.ObjectType):
    dummy_by_id = DjangoObjectField(DummyType, description='Single User query')
    all_dummies = DjangoListObjectField(DummyListType, description='All Users query')
