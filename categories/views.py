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


class EditCategoriesView(APIView):
    serializer_class = ProductCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        category = ProductCategoriesModels.objects.filter(id=pk).first()
        if not category:
            return Response({'msg': 'Category not found'})
        serializer = ProductCategoriesSerializer(category, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        category = ProductCategoriesModels.objects.get(pk=pk)
        if not category:
            return Response({'msg': 'Category not found'})
        category.delete()
        return Response({'msg': 'Category deleted'})


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


class EditSubCategoriesView(APIView):
    serializer_class = SubProductCategoriesSerializer

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        subcategory = SubProductCategoriesModels.objects.filter(id=pk).first()
        if not subcategory:
            return Response({'msg': 'SubCategory not found'})
        serializer = SubProductCategoriesSerializer(subcategory, data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        name = data.get('name')
        serializer.save(name=name)
        return Response(serializer.data)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        subcategory = SubProductCategoriesModels.objects.filter(id=pk).first()
        if not subcategory:
            return Response({'msg': 'SubCategory not found'})
        subcategory.delete()
        return Response({'msg': 'SubCategory deleted'})
