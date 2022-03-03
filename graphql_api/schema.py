import graphene
from posts.schema import Query as PostsQuery


class Query(
    PostsQuery,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
