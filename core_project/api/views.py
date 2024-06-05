from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *


@api_view(['GET'])
def home(request):
    std_obj = Student.objects.all()
    serializer_var = stu_serilizer(std_obj, many = True)

    return Response({
        'status':200,
        'payload': serializer_var.data
    })

@api_view(['post'])
def post_std(request):
    data = request.data
    serializer_var= stu_serilizer(data=data)

    # if data['age']<18: # we dont use this here instead in srylizer
        # return Response({'status':403,'payload': data, 'error_data' : data['age'],'message': 'Age Must me greater then 18' })

    if serializer_var.is_valid():
        serializer_var.save()
        return Response({'status':200,'payload': data,'message': 'post student success' })
    else:
        return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })

#update using put 
@api_view(['put'])
def put_std(request, id):
    data = request.data
    try:
        student = Student.objects.get(id= id)
        serializer_var= stu_serilizer(student, data=data)
        if serializer_var.is_valid():
            serializer_var.save()
            return Response({'status':200,'payload': data,'message': 'post student success' })
        else:
            return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })
        pass
    except Exception as e:
        return Response({'status':403,'error reason' : f'{e}' , 'message': 'hint: ID is not valid' })

@api_view(['patch'])
def patch_std(request, id):
    data = request.data
    try:
        student = Student.objects.get(id= id)
        serializer_var= stu_serilizer(student, data=data, partial= True)
        if serializer_var.is_valid():
            serializer_var.save()
            return Response({'status':200,'payload': data,'message': 'post student success' })
        else:
            return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })
        pass
    except Exception as e:
        return Response({'status':403,'error reason' : f'{e}' , 'message': 'hint: ID is not valid' })

# ?id=1
def delete_std(request):
    id = request.GET.get('id')
    Student.delete()
    pass