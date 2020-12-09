from graphene_django import DjangoObjectType

from demo.models import Dummy


# TODO: Step 4 crate this file
class DummyType(DjangoObjectType):

    class Meta:
        model = Dummy
        # TODO generate this feelds
        fields = (
            "id",
            "name",
            "day",
            "weekday",
            "month",
            "year",
            "created_at",
            "updated_at",
        )
