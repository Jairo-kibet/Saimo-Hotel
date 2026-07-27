from django.urls import path,include
from . import views as v


urlpatterns = [
    path("", v.index, name="home"),
    path("xxx/", v.xxx, name="xxx"),
     path("accommodation/", v.accommodation, name="accommodation"),
     path("swimming/", v.swimming, name="swimming"),
     path("recreational/", v.recreational, name="recreational"),
    path("dining/", v.dining, name="dining"),
    path("gallery/", v.gallery, name="gallery"),
    path("bar/", v.bar, name="bar"),
    path("contact/", v.contact, name="contact"),
    path("conference/", v.conference, name="conference"),
]