import graphene
from graphene_django import DjangoObjectType
from patients.models import Patients

class PatientsType(DjangoObjectType):
    class Meta:
        model = Patients
        fields = ("id", "name", "gender", "date_of_birth", "address", "medical_history")

class Query(graphene.ObjectType):

    all_patients = graphene.List(PatientsType)

    def resolve_all_patients(root, info):
        return Patients.objects.all()

schema = graphene.Schema(query=Query)
