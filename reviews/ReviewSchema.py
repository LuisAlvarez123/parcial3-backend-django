import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import User, Category, Review
from django.utils import timezone

# Create a GraphQL type for the Book model
class ReviewType(DjangoObjectType):
    class Meta:
        model = Review

# Create a Query type
class Query(ObjectType): 
    review = graphene.Field(ReviewType, id=graphene.Int())   
    reviews = graphene.List(ReviewType)   

    def resolve_review(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Review.objects.get(pk=id)

        return None
    
    
    def resolve_reviews(self, info, **kwargs):
        return Review.objects.all()


class ReviewInput(graphene.InputObjectType):
    id = graphene.ID()
    comment = graphene.String()
    ranking = graphene.Int()
    movie = graphene.Int()
    user = graphene.Int()

class CreateReview(graphene.Mutation):
    class Arguments:
        input = ReviewInput(required=True)

    ok = graphene.Boolean()
    review = graphene.Field(ReviewType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        user_obj = User.objects.get(id=input.user)
        movie_obj = User.objects.get(id=input.user)
        review_instance = Review(
            ranking=input.ranking,
            comment=input.comment,
            createdAt=timezone.now(),
            updatedAt= timezone.now(),
            movie=movie_obj,
            user=user_obj
        )
        review_instance.save()
        return CreateReview(ok=ok, review=review_instance)


class UpdateReview(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = ReviewInput(required=True)

    ok = graphene.Boolean()
    review = graphene.Field(ReviewType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        review_instance = Review.objects.get(pk=id)
        if review_instance:
            ok = True           
            user_obj = User.objects.get(id=input.user)
            movie_obj = User.objects.get(id=input.user)

            review_instance.comment=input.comment
            review_instance.ranking=input.ranking
            review_instance.updatedAt=timezone.now()
            review_instance.movie=movie_obj
            review_instance.user=user_obj

            review_instance.save()            
            return UpdateReview(ok=ok, review=review_instance)
        return UpdateReview(ok=ok, review=None)


class Mutation(graphene.ObjectType):
    create_category = CreateCategory.Field()
    update_category = UpdateCategory.Field()

    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()

    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()

    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)