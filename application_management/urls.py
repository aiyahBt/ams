from django.urls import path
from . import views


app_name = 'appmanage'
urlpatterns = [
    path('application-announcement/', views.application_announcement_view, name='app_announce'),
    path('application-announcement/new-round', views.announce_new_application_round_view, name='new_round'),

    path('application-form/<int:application_round_id>', views.application_form_view, name='application_form'),

    path('upload/', views.image_upload_view, name='upload_image'),

]
