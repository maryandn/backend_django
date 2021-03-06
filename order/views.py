from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from order.models import CartModel
from product.models import ProductModel
from user_profile.models import UserModel
from order.serializers import CartSerializer, CartProductSerializer


class CartView(APIView):
    serializer_class = CartSerializer, CartProductSerializer

    def post(self, *args, **kwargs):
        id_user = self.request.user.id
        data = self.request.data
        data['id_user'] = id_user
        serializer = CartSerializer(data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        user = self.request.user.id
        cart = CartModel.objects.filter(id_user=user)
        if not cart:
            return Response({'msg': 'user not found'}, status.HTTP_404_NOT_FOUND)
        return Response(CartProductSerializer(cart, many=True).data, status.HTTP_200_OK)


class EditCartView(APIView):
    serializer_class = CartSerializer

    def delete(self, *args, **kwargs):
        id = self.request.user.id
        product_id = kwargs.get('pk')
        product = CartModel.objects.filter(id_product=product_id, id_user=id).first()
        if not product:
            return Response({'msg': 'product not found'}, status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'msg': 'product deleted'}, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        id = self.request.user.id
        product_id = kwargs.get('pk')
        product = CartModel.objects.filter(id_product=product_id, id_user=id).first()
        if not product:
            return Response({'msg': 'product not found'})
        serializer = CartSerializer(product, data=self.request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)


class CleanCartView(APIView):
    def delete(self, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = CartModel.objects.filter(user=user_id)
        if not user:
            return Response({'msg': 'user not found'}, status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({'msg': 'cart deleted'}, status.HTTP_200_OK)
