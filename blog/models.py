from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Header(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.ImageField(upload_to="home/")

    def __str__(self):
        return f"{self.title}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/")
    status = models.CharField(max_length=255, choices=[
        ("draft", "Draft"),
        ("publish", "Published"),
    ], default="draft")
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"


class About(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.ImageField(upload_to="about/")
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, null=True, blank=True)
    background_image = models.ImageField(upload_to="contact/")
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"
