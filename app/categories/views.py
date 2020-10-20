from rest_framework.views import APIView

from .models import ProductCategoriesModels, SubProductCategoriesModels
from .serializers import ProductCategoriesSerializer, SubProductCategoriesSerializer
from rest_framework.response import Response


class CategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def get(self, request):
        category = ProductCategoriesModels.objects.all()
        return Response(ProductCategoriesSerializer(category, many=True).data)

    def post(self, request):
        serializer = ProductCategoriesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response({"msg": "Category is add"})


class SubCategoriesView(APIView):
    serializer_class = SubProductCategoriesSerializer

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        subcategory = SubProductCategoriesModels.objects.filter(categories_id=pk)
        return Response(SubProductCategoriesSerializer(subcategory, many=True).data)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = SubProductCategoriesSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save(categories_id=pk)
        return Response(serializer.data)
