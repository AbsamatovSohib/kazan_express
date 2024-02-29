from rest_framework import generics, permissions
from .models import Shop, Product, Category
from .admin import HasRolePermission
from kazan import serializer
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ShopAdminView(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = serializer.ShopSerializer

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ['shop_admin']

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('title', )

    search_fields = ('title','shops__title')


class ShopUpdateApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.ShopSerializer
    queryset = Shop.objects.all()

    lookup_field = 'pk'

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ('shop_admin', )


class ProductListApiview(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ('product_admin', )

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('title', "id")


class UpdateProductApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.ProductSerializer
    queryset = Product.objects.all()

    lookup_field = 'pk'

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ('product_admin', )


class CategoryAPiview(generics.ListAPIView):
    serializer_class = serializer.CategorySerializer
    queryset = Category.objects.all()

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ('category_admin',)


class UpdateCategory(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializer.CategorySerializer
    queryset = Category.objects.all()

    permission_classes = (permissions.IsAuthenticated, HasRolePermission)
    required_roles = ('category_admin', )
