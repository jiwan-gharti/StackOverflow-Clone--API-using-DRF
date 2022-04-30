from django.db import models
# from django.contrib.auth.models import User
from django.conf import settings
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

class Post(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL, null= True, related_name='post_user')
    title = models.CharField(max_length=500)
    description = RichTextUploadingField()
    upvote_count = models.IntegerField(default=0)
    tag = models.CharField(max_length=50)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f'{ self.title } by { self.user.email }'

class Answer(BaseModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='answer_post')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='answer_user')
    answer = models.TextField()
    correct = models.BooleanField(default=False)
    upvote_count = models.IntegerField(default = 0)


    def __str__(self):
        return f'{ self.answer}'

class Comment(BaseModel):
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comment_post')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comment_user')
    answer = models.ForeignKey(Answer, on_delete=models.SET_NULL, null=True, related_name='comment_answer')
    comment = models.TextField()

    def __str__(self):
        return f'{ self.post}'


class Tag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null= True, related_name='tag_post')
    tag = models.CharField(max_length=255, unique= True)

    def __str__(self):
        return self.tag
    




