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
        'api/persona/detail/<pk>/',
        views.GetOnePerson.as_view(),        
    ),
    path(
        'api/persona/names/<namePersona>/',
        views.GetNames.as_view(),        
    ),
    path(
        'api/persona/register/',
        views.PersonCreateView.as_view(),        
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonDeleteView.as_view(),        
    ),
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateView.as_view(),        
    ),
    path(
        'api/persona/updateretrieve/<pk>/',
        views.PersonRetrieveView.as_view(),        
    )
]
