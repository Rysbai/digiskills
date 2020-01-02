from factory import DjangoModelFactory

from aboutus.models import AboutUs


class AboutUsFactory(DjangoModelFactory):
    class Meta:
        model = AboutUs

    payload_kg = 'Example payload in kyrgyz'
    payload_ru = 'Example payload in russian'
