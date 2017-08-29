import pytest
from codeschool.lms.organizations.models import Discipline
from codeschool.lms.organizations.models import DescriptiveModel
from codeschool.lms.organizations.models import Organization
from django.utils import timezone

class TestDiscipline:

    def create_descriptive_model(self):
        slug = "FGA"
        name = "Universidade de Brasilia - Campus Gama"
        description = "Terra, Lama e Poeira"
        return DescriptiveModel(slug=slug,name=name,
                                               description=description)

    def create_organization(self):
        organization = self.create_descriptive_model()
        return organization

    def create_discipline(self):
        faculty = self.create_organization()
        school_id = "22"
        since = timezone.now()
        syllabus = "MES"
        program = "Manutencao e evolucao de uns software zuado"
        bibliography = "Codar, codar, codar, google, stackoverflow"

        return Discipline(school_id=school_id, since=since,
        syllabus=syllabus, program=program, bibliography=bibliography)

    def test_create_discipline(self):
        discipline = self.create_discipline()
