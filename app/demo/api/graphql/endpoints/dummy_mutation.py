import graphene

from demo.api.graphql.endpoints.dummy_common import DummySerializerMutation


class DummyMutations(graphene.ObjectType):
    create_dummy = DummySerializerMutation.CreateField()
    update_dummy = DummySerializerMutation.UpdateField()
    delete_dummy = DummySerializerMutation.DeleteField()