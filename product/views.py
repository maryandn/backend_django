from rest_framework.views import APIView

from rest_framework.response import Response

from .models import ProductModel
from .serializers import ProductSerializer


class ProductView(APIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"msg": "Product is add"})

    def get(self, request):
        product = ProductModel.objects.all()
        return Response(ProductSerializer(product, many=True).data)
