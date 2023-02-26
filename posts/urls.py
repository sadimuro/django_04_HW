from django.urls import path

from posts.views import hello, get_index, contacts, about

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path("", get_contacts, name="contacts"),
    path("", get_about, name="about")
]