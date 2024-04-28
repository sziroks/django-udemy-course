from django.contrib import admin
from .models import Post, Author

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "id_post", "author", "date", "image")


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
