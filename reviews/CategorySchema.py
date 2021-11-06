import graphene
from graphene_django import DjangoObjectType
from .models import Category, Movie, Review, User
class MainCategory:
    # Querys
    class CategoryType(DjangoObjectType):
        class Meta:
            model = Category
    
    
    class Query(graphene.ObjectType):
        category = graphene.List(CategoryType)
    
        def resolve_category(self, info, **kwargs):
            return Category.objects.all()
    
    # Fin de querys
    
    
    # Mutations
    class CategoryInput(graphene.InputObjectType):
        id = graphene.ID()
        name = graphene.String()
        color = graphene.String()
    
    
    class CreateCategory(graphene.Mutation):
        class Arguments:
            input = CategoryInput(required=True)
    
        ok = graphene.Boolean()
        category = graphene.Field(CategoryType)
    
        @staticmethod
        def mutate(root, info, input=None):
            ok = True
            category_instance = Category(name=input.name,color=input.color)
            category_instance.save()
            return CreateCategory(ok=ok, category=category_instance)
    
    