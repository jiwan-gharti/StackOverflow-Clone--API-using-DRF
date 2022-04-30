from django.contrib import admin

from posts.models import (
    Answer,
    Comment,
    Post,
    Tag
)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    summernote_fields = ('desciption', )
    list_display = ['user','title','description','upvote_count','tag','verified']

@admin.register(Answer)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post','user','answer','correct','upvote_count']

@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post','user','answer','comment']


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post','tag']
