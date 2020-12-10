from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

from config.schema import schema


urlpatterns = [
    path('admin/', admin.site.urls),
    # TODO: Step 1 Add this line
    path("api/graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]
