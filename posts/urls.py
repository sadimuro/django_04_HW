from django.urls import path

from posts.views import hello, get_index, get_contacts, get_about, get_post, get_update_post, get_delete_post

urlpatterns = [
    path("hello/", hello, name="hello-view"),
    path("", get_index, name="index-page"),
    path("about/", get_about, name="about-page"),
    path("contacts/", get_contacts, name="contacts-page"),
    path("get_post/", get_post, name="post_detail-page"),
    path("update_post/", get_update_post, name="post_update-page"),
    path("delete_post/", get_delete_post, name="post_create-page"),
    ]