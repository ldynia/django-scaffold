# TODO: Step 3 create this file
import graphene
from demo.api.graphql.endpoints.dummy_query import DummyQuery


class Mutation():
    pass


class Query(DummyQuery):
    pass


schema = graphene.Schema(query=Query)
# schema = graphene.Schema(query=Query, mutation=Mutation)