import graphene
from graphene import relay, ObjectType
from graphene_django.types import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User


class UserNode(DjangoObjectType):
    class Meta:
        model = User
        # Permite un filtrado mas avanzado
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'surname': ['exact',],
            'username': ['exact',],
            'password': ['exact',],
            'role': ['exact'],            
        }
        interfaces = (relay.Node, )


class Query(object):
    user = relay.Node.Field(UserNode)
    all_users = DjangoFilterConnectionField(UserNode)


class CreateUser(graphene.Mutation):
# Definiendo los argumentos que se le van a pasar a crear
    class Arguments:
        name= graphene.String()
        surname= graphene.String()
        username= graphene.String()
        password= graphene.String()    
        rol = graphene.Boolean()

# Retorna el usuario creado
    user = graphene.Field(UserNode)

#la verdadera mutación
    def mutate(self, info, name, surname, username, password, role):        
        user = User.objects.create(
            name = name,
            surname = surname,
            username=username,
            password= password,
            role=role
        )           

        user.save()
    # return an instance of the Mutation 🤷‍♀️
        return CreateUser(
            user=user
        )

# Mutaciones 🦁 


