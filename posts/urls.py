from django.urls import path

from posts.views import hello, get_index, get_contacts, get_about

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path("", get_contacts, name="Contacts"),
    path("", get_about, name="About")
]