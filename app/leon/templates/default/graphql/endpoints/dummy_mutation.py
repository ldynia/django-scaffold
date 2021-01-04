import graphene

from demo.api.graphql.common.types_n_inputs import DummySerializerMutation


class DummyMutations(graphene.ObjectType):
    create_dummy = DummySerializerMutation.CreateField()
    update_dummy = DummySerializerMutation.UpdateField()
    delete_dummy = DummySerializerMutation.DeleteField()