from rest_framework import serializers
from . models import Product,ProductReview

class ProductSerializers(serializers.ModelSerializer):
    reviews = serializers.StringRelatedField(many = True) 
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'