from django.forms import ModelForm
from .models import Frameworks


class FrameworksForm(ModelForm):
    class Meta:
        model = Frameworks
        fields = ['name', 'language', 'using_percentage', 'user']
        labels = {
            "name": "Nom du framework ",
            "language": "Nom du langage ",
            "using_percentage": "Popularité (en %) ",
            "user": "Utilisateur "
        }
