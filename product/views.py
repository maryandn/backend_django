from rest_framework.views import APIView

from rest_framework.response import Response

from .models import ProductModel
from .serializers import ProductSerializer, ProductChangeSerializer, ImgSerializer


class ImgView(APIView):
    serializer_class = ImgSerializer

    def post(self, *args, **kwargs):
        serializer = ImgSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"msg": "Img is add"})


class ProductView(APIView):
    serializer_class = ProductSerializer

    def post(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        serializer = ProductSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        img_id = data.get('img')
        color_id = data.get('color')
        brand_id = data.get('brand')
        serializer.save(sub_category_id=pk, img_id=img_id, color_id=color_id, brand_id=brand_id)
        return Response(serializer.data)

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.filter(sub_category_id=pk)
        return Response(ProductSerializer(product, many=True).data)


class ChangeProductView(APIView):
    serializer_class = ProductSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        product = ProductModel.objects.get(pk=pk)
        serializer = ProductChangeSerializer(product, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        img_id = data.get('img')
        color_id = data.get('color')
        brand_id = data.get('brand')
        serializer.save(img_id=img_id, color_id=color_id, brand_id=brand_id)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        product = ProductModel.objects.get(pk=pk)
        product.delete()
        return Response({'msg': 'product deleted'})
