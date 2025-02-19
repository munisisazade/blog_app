from django.contrib import admin
from blog.models import (
    Header,
    Blog,
    About,
    ContactMessage,
    Contact
)

admin.site.register(Header)
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(ContactMessage)
admin.site.register(Contact)