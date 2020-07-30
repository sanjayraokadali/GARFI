from django.conf.urls import url
from App import views

app_name = 'App'

urlpatterns = [

    url(r'^$',views.NextView.as_view(),name='nextview'),
    url(r'^Users/',views.DisplayView,name='displayview')

]
