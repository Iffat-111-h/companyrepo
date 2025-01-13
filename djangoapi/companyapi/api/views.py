from rest_framework import viewsets
from api.models import Company, Employee
from api.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# CompanyViewSet for handling Company data
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
           company = self.get_object()  # Get the specific company instance
           emps = Employee.objects.filter(company=company)  # Use the company instance
           emps_serializer = EmployeeSerializer(emps, many=True, context={'request': request})
           return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message' : 'Company might not exist!! Error'
            })

# EmployeeViewSet for handling Employee data
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer