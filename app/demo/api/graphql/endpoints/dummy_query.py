import graphene

from demo.models import Dummy
from demo.api.graphql.common.types import DummyType


# TODO: Step 5 Create this file
class DummyQuery(graphene.ObjectType):
    all_dummies = graphene.List(DummyType)
    get_dummy_by_id = graphene.Field(DummyType, id=graphene.ID(required=True))

    def resolve_all_dummies(root, info):
        return Dummy.objects.all()
    
    def resolve_get_dummy_by_id(root, info, id):
        try:
            return Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            return None
        