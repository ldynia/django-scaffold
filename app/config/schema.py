# TODO: Step 3 create this file
import graphene

from demo.api.graphql.dummy.query import DummyQuery
from demo.api.graphql.dummy.mutation import DummyMutations


class Queries(DummyQuery):
    pass


class Mutations(DummyMutations):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)