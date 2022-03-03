import graphene
from graphene_django import DjangoObjectType
from .models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('id', 'title', 'description', 'image')

    def resolve_image(self, info):
        return self.image.thumbnails.large.url


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post = graphene.Field(PostType, id=graphene.Int())

    @staticmethod
    def resolve_posts(root, info):
        return Post.objects.all()

    @staticmethod
    def resolve_post(root, info, id):
        return Post.objects.get(pk=id)
