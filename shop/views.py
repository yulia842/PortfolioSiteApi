from .models import Product, Cart
from .serializers import ProductSerializer, CartSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )

    # Add to cart
    @action(methods=['POST'], detail=True)
    def add_to_cart(self, request,pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        product = Product.objects.get(id=pk)
        user = request.user
        quantity = int(request.data.get('quantity', 1))
        
        cart_item, created = Cart.objects.get_or_create(user=user, product=product, defaults={'quantity': quantity})
        if not created :
            cart_item.quantity += quantity
            cart_item.save()
        serializer = CartSerializer(cart_item, many=False)
        return Response({"detail": "Product added to cart", 'data' : serializer.data}, status=status.HTTP_200_OK)
    
    # Add product
    @action(methods=['POST'], detail=False)
    def add_product(self, request):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Product created", 'data' : serializer.data}, status=status.HTTP_201_CREATED)

    # Remove product
    @action(methods=['DELETE'], detail=True)
    def remove_product(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({"detail": "Product removed"}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)

    # Update product
    @action(methods=['PUT'], detail=True)
    def update_product(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, data=request.data, partial = True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"detail": "Product updated", 'data' : serializer.data}, status=status.HTTP_201_CREATED)


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated]
  
    @action(methods=['DELETE'], detail=True)
    def remove_product_from_cart(self, request, pk=None):
        if not request.user.is_authenticated:
            return Response({"detail": "Authentication credentials were not provided."}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            cart_item = Cart.objects.get(id=pk, user=request.user)
            cart_item.delete()
            return Response({"detail": "Product removed from cart"}, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"detail": "Product not found in cart."}, status=status.HTTP_404_NOT_FOUND)
