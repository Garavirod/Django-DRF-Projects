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
        name = 'detail-person'        
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
    ),
    path(
        'api/persona/list2/',
        views.GetListPerson.as_view(),
    ),
    path(
        'api/persona/extendedlist/',
        views.GetLitsPersonExtended.as_view(),
    ),
    path(
        'api/hobbies/',
        views.GetHobbies.as_view(),
    ),
    path(
        'api/meetings/',
        views.GetMeetings.as_view(),
    ),
    path(
        'api/hobbiesperson/',
        views.GetPersonHobbies.as_view(),
    ),
    path(
        'api/meetings2/',
        views.GetMeetings2.as_view(),
    )
    ,
    path(
        'api/meetings-link/',
        views.GetApiListaLink.as_view(),
    ),
    path(
        'api/pagination-Listperson/',
        views.GetApiListPaginacion.as_view()
    )
]
