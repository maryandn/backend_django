from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import ProductModel, ColorModel, BrandModel
from .serializers import ProductSerializer, ProductChangeSerializer, ColorSerializer, BrandSerializer


class ColorView(APIView):
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self, request):
        color = ColorModel.objects.all()
        return Response(ColorSerializer(color, many=True).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = ColorSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"msg": "Color is add"}, status.HTTP_201_CREATED)


class EditColorView(APIView):
    serializer_class = ColorSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        color = ColorModel.objects.filter(id=pk).first()
        if not color:
            return Response({'msg': 'Color not found'})
        serializer = ColorSerializer(color, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        color = ColorModel.objects.filter(id=pk).first()
        if not color:
            return Response({'msg': 'Color not found'})
        color.delete()
        return Response({'msg': 'Color delete'})


class BrandView(APIView):
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

    def get(self, request):
        brand = BrandModel.objects.all()
        return Response(BrandSerializer(brand, many=True).data, status.HTTP_200_OK)

    def post(self, request):
        serializer = BrandSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"msg": "Brand is add"}, status.HTTP_201_CREATED)


class EditBrandView(APIView):
    serializer_class = BrandSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        brand = BrandModel.objects.filter(id=pk).first()
        if not brand:
            return Response({'msg': 'Brand not found'})
        serializer = BrandSerializer(brand, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        brand = BrandModel.objects.filter(id=pk).first()
        if not brand:
            return Response({'msg': 'Brand not found'})
        brand.delete()
        return Response({'msg': 'Brand delete'})


class ProductView(APIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return super().get_permissions()

    def post(self, *args, **kwargs):
        print('***********', self.request.user)
        pk = kwargs.get('pk')
        data = self.request.data
        print('&&&&&&&&&&&', data)
        serializer = ProductSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        color_id = data.get('color')
        brand_id = data.get('brand')
        serializer.save(sub_category_id=pk, color_id=color_id, brand_id=brand_id)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.filter(sub_category_id=pk)
        return Response(ProductSerializer(product, many=True).data, status.HTTP_200_OK)


class ChangeProductView(APIView):
    serializer_class = ProductSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        product = ProductModel.objects.get(pk=pk)
        serializer = ProductChangeSerializer(product, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.get(pk=pk)
        product.delete()
        return Response({'msg': 'product deleted'})


class GetProductView(APIView):
    serializer_class = ProductSerializer

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.filter(id=pk)
        return Response(ProductSerializer(product, many=True).data, status.HTTP_200_OK)
