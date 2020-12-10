import graphene
from demo.models import Dummy
from demo.api.graphql.common.types import DummyType


# TODO: Step 5 Create this file
class DummyQuery(graphene.ObjectType):
    all_dummies = graphene.List(DummyType)

    def resolve_all_dummies(root, info):
        return Dummy.objects.all()