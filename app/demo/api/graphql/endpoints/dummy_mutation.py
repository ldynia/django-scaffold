import graphene

from demo.models import Dummy
from demo.api.graphql.common.types import DummyType


# TODO: Step 5 Create this file
class UpdateDummy(graphene.Mutation):

    # Response argument
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID(required=True)
        day = graphene.Int()
        weekday = graphene.String()
        month = graphene.String()
        year = graphene.Int()

    @classmethod
    def mutate(cls, root, info, id, **data):
        try:
            dummy = Dummy.objects.get(id=id)
            if Dummy.objects.filter(id=id).update(**data):
                dummy = Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            return cls(dummy=None)
        
        return cls(dummy=dummy)


class CreateDummy(graphene.Mutation):

    # Response argument
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID(required=True)
        day = graphene.Int()
        weekday = graphene.String()
        month = graphene.String()
        year = graphene.Int()

    @classmethod
    def mutate(cls, root, info, **data):
        try:
            dummy = Dummy.objects.create(data)
        except Dummy.DoesNotExist:
            return cls(dummy=None)
        
        return cls(dummy=dummy)


class DeleteDummy(graphene.Mutation):

    # Response argument
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            dummy = Dummy.objects.get(id=id)
            dummy.delete()
        except Dummy.DoesNotExist:
            return cls(dummy=None)
        
        return cls(dummy=None)


class DummyMutations(graphene.ObjectType):
    create_dummy = CreateDummy.Field()
    update_dummy = UpdateDummy.Field()
    delete_dummy = DeleteDummy.Field()
