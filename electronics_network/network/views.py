from rest_framework import mixins
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg

from network.serializers import NetworkElementSerializer
from network.models import NetworkElement
from employees.permissions import IsActiveEmployee


class NetworkElementViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    permission_classes = (IsAuthenticated, IsActiveEmployee,)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @action(detail=False, methods=['get'])
    def by_country(self, request):
        country = request.query_params.get('country')
        if not country:
            return Response({"detail": "Country query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        elements = NetworkElement.objects.filter(country=country)
        serializer = self.get_serializer(elements, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def above_average_debt(self, request):
        avg_debt = NetworkElement.objects.aggregate(Avg('debt'))['debt__avg']
        elements = NetworkElement.objects.filter(debt__gt=avg_debt)
        serializer = self.get_serializer(elements, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def by_product(self, request):
        product_id = request.query_params.get('product_id')
        if not product_id:
            return Response({"detail": "Product ID query parameter is required."}, status=status.HTTP_400_BAD_REQUEST)
        elements = NetworkElement.objects.filter(products__id=product_id)
        serializer = self.get_serializer(elements, many=True)
        return Response(serializer.data)
    
