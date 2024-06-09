from django.urls import path
#from django.conf.urls impport url
from . import views
urlpatterns=[
               path('',views.index, name='index'),
               path('aboutus/',views.aboutus),
               path('footer/',views.footer),
               path('login/',views.login),
               path('help/',views.help),
               path('map/',views.map),
               path('journey/',views.journey),
               path('signup/',views.signup),
               path('viewmore/',views.viewmore),

              ]