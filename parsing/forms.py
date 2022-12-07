from django import forms
from . import parser, models

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('INAI_KG', 'INAI_KG'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        field = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'INAI_KG':
            film_parser = parser.parser()
            for i in film_parser:
                models.News.objects.create(**i)