from rest_framework import serializers
from .models import Product, Category, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'text', 'stars', 'product']

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Отзыв не должен быть пустым.")
        return value

    def validate_stars(self, value):
        if not 1 <= value <= 5:
            raise serializers.ValidationError("Рейтинг должен быть в диапазоне от 1 до 5.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'category', 'reviews', 'average_rating']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'products_count']

    def get_products_count(self, instance):
        return instance.products_count()

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Название категории должно содержать не менее 3 символов.")
        return value

class ProductDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Цена не может быть отрицательной .")
        return value
