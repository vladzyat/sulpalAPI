from rest_framework import serializers
from .models import Stars, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('text',
                  'customer_id',
                  'product_id',
                  'datetime')


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = ('rating',
                  'customer_id',
                  'product_id',
                  'datetime')


class GetCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'text', 'customer_id')


class GetStarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        fields = ('id', 'rating', 'customer_id', 'datetime')
