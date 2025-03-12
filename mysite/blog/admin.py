from django.contrib import admin
from .models import Author, Category, Post

#admin.site.register(Author)
#admin.site.register(Category)
#admin.site.register(Post)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'about_me')
    search_fields = ['user']
    prepopulated_fields = {'about_me': ('user',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author','timestamp')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
