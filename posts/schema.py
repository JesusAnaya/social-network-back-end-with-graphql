import graphene
from graphene_django import DjangoObjectType

from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image')


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.Int())

    @staticmethod
    def resolve_questions(root, info):
        return PostType.objects.all()

    @staticmethod
    def resolve_post(root, info, id):
        return PostType.objects.get(pk=id)
