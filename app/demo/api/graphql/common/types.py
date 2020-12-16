from graphene_django import DjangoObjectType

from demo.models import Dummy


class DummyType(DjangoObjectType):

    class Meta:
        model = Dummy
        # TODO generate this feelds
        fields = (
            "id",
            "day",
            "weekday",
            "month",
            "year",
            "created_at",
            "updated_at",
        )
