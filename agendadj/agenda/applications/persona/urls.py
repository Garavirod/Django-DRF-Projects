from django.urls import path, re_path

from . import views

app_name = 'persona_app'
urlpatterns = [
    path(
        'personas/',
        views.PersonaListView.as_view(),
        name='personas'
    ),
    path(
        'api/persona/list/',
        views.PersonaListApiView.as_view(),        
    ),
    path(
        'api/persona/one/<idPersona>',
        views.GetOnePerson.as_view(),        
    ),
    path(
        'api/persona/names/<namePersona>/',
        views.GetNames.as_view(),        
    )
]
