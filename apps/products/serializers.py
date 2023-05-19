from rest_framework import serializers
from .models import Category, Product
from apps.reviews.serializers import CommentSerializer, StarsSerializer, GetCommentsSerializer, GetStarsSerializer
from ..reviews.models import Comment, Stars


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description')

    # def create(self, validated_data):
    #     title = validated_data['title']
    #     description = validated_data['description']
    #     obj = Category.objects.create(
    #         title=title,
    #         description=description
    #     )
    #     return obj


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'description', 'price', 'image', 'category')


class GetProductSerializer(serializers.ModelSerializer):
    comments = GetCommentsSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'image', 'category', 'comments', 'get_rating')
