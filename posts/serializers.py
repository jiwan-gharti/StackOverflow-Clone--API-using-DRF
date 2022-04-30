from django.utils.safestring import mark_safe

from rest_framework import serializers

from .models import (
    Answer,
    Comment,
    Post,
    Tag
)

class PostSerializer(serializers.ModelSerializer):

    answer_post = serializers.StringRelatedField(many = True, read_only = True)
    comment_post = serializers.StringRelatedField(many = True, read_only = True)
    description = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','user','title','description','upvote_count','tag','answer_post','comment_post']
        
    def get_description(self, instance):
        print(instance.description)
        return mark_safe(instance.description)

    

class AnswerSerializer(serializers.ModelSerializer):
    comment_answer = serializers.StringRelatedField(many = True, read_only = True)
    post = PostSerializer(read_only = True)

    class Meta:
        model = Answer
        fields = ['id','user','post','answer','correct','upvote_count','comment_answer']

class CommentSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only = True)
    post = PostSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = ['id','post','user','answer','comment']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id','post','tag']
