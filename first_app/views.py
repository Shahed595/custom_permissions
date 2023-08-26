from django.shortcuts import render
from rest_framework import viewsets
from . import models,serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from . import permissions

# For Doing CRUD Operation
# Create,Read,Update,Delete
class ProductViewSet(viewsets.ModelViewSet):
    #This one is Global Permission
    # permission_classes = [IsAuthenticatedOrReadOnly ] #This will use when it will be authenticated user
    # permission_classes = [permissions.AdminOrReadOnly] #This will use to see product but cannot edit product
    
    #This one is Custom Permission
    permission_classes = [permissions.AdminOrReadOnly]
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
    
# For Doing CRUD Operation
# Create,Read,Update,Delete
class ProductReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.ReviewOrReadOnly]
    queryset = models.ProductReview.objects.all()
    serializer_class = serializers.ProductReviewSerializers