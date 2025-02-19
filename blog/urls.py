from django.urls import path
from blog.views import home_page, about_view, blog_detail, contact_view

urlpatterns = [
    path("", home_page, name="home-page"),
    path("blog/<int:id>", blog_detail, name="blog-detail"),
    path("about/", about_view, name="about-page"),
    path("contact/", contact_view, name="contact-page"),
]
