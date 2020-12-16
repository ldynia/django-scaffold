import graphene

from demo.models import Dummy
from demo.api.graphql.common.types import DummyType


class WeekdayEnum(graphene.Enum):
    Monday = 'Monday'
    Tuesday = 'Tuesday'
    Wednesday = 'Wednesday'
    Thursday = 'Thursday'
    Friday = 'Friday'
    Saturday = 'Saturday'
    Sunday = 'Sunday'


class MonthEnum(graphene.Enum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    October = 10
    November = 11
    December = 12


# TODO: Step 5 Create this file
class CreateDummy(graphene.Mutation):

    # Response argument
    ok = graphene.Boolean(default_value=True)
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID()
        day = graphene.Int(required=True)
        weekday = WeekdayEnum(required=True)
        month = MonthEnum(required=True)
        year = graphene.Int(required=True)

    @classmethod
    def mutate(cls, root, info, **data):
        try:
            dummy = Dummy.objects.create(**data)
        except Dummy.DoesNotExist:
            return cls(ok=False, dummy=None)
        
        return cls(dummy=dummy)


class UpdateDummy(graphene.Mutation):

    # Response argument
    ok = graphene.Boolean(default_value=True)
    dummy = graphene.Field(DummyType)

    class Arguments:
        id = graphene.ID(required=True)
        day = graphene.Int()
        weekday = WeekdayEnum(required=True)
        month = MonthEnum(required=True)
        year = graphene.Int()

    @classmethod
    def mutate(cls, root, info, id, **data):
        try:
            dummy = Dummy.objects.get(id=id)
            if Dummy.objects.filter(id=id).update(**data):
                dummy = Dummy.objects.get(id=id)
        except Dummy.DoesNotExist:
            return cls(ok=False, dummy=None)
        
        return cls(dummy=dummy)


class DeleteDummy(graphene.Mutation):

    # Response argument
    ok = graphene.Boolean(default_value=True)

    class Arguments:
        id = graphene.ID(required=True)

    @classmethod
    def mutate(cls, root, info, id):
        try:
            Dummy.objects.get(id=id).delete()
        except Dummy.DoesNotExist:
            return cls(ok=False)
    
        return cls(ok=True)


class DummyMutations(graphene.ObjectType):
    create_dummy = CreateDummy.Field()
    update_dummy = UpdateDummy.Field()
    delete_dummy = DeleteDummy.Field()
