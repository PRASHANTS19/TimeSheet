# views.py
from rest_framework import viewsets, status, generics
from .models import Employee, Master
from .serializers import EmployeeSerializer, MasterSerializer
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny 

class EmployeeLoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print("This is email and password=>",email, password)
        if email and password:
            try:
                employee = Employee.objects.get(email=email, password=password)
                serializer = EmployeeSerializer(employee, context={'request': request})
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer

    @action(detail=True, methods=['GET'])
    def get_employee_records(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        masters = Master.objects.filter(employee_id=employee)
        serializer = self.get_serializer(masters, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def post_employee_records(self, request, pk=None):
        employee = Employee.objects.get(pk=pk)
        date = request.data.get('date')
        if date is None:
            return Response({'error': 'Date is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if Master.objects.filter(date=date, employee_id=employee).exists():
            return Response({'error': 'This date already has an entry for this employee'}, status=status.HTTP_400_BAD_REQUEST)

        master = Master.objects.create(date=date, employee_id=employee)
        serializer = self.get_serializer(master)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

