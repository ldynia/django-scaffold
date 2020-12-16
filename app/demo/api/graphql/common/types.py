from graphene_django import DjangoObjectType

from demo.models import Dummy


class DummyType(DjangoObjectType):

    class Meta:
        model = Dummy
        description = 'Type definition for a single dummy.'

        # TODO generate this fields
        fields = (
            'id',
            'day',
            'weekday',
            'month',
            'year',
            'pre_seeded',
            'created_at',
            'updated_at',
        )