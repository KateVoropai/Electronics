import datetime

from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    release_date = serializers.DateField(input_formats=["%d.%m.%Y"])

    def create(self, validated_data):
        release_date = validated_data.get('release_date')
        
        current_date = datetime.datetime.now().date()
        if release_date > current_date:
            raise serializers.ValidationError("Дата выхода продукта на рынок не может быть в будущем.")
        return Product.objects.create(**validated_data)

    class Meta:
        model = Product
        fields = '__all__'
