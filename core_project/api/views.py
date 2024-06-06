from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *

from rest_framework.views import APIView


class Std_Api(APIView):
    def get(self , request, id):
        std_obj = Student.objects.all()
        serializer_var = stu_serilizer(std_obj, many = True)
        return Response({
            'status':200,
            'payload': serializer_var.data
        })


    def post(self, request, id):
        data = request.data 
        serializers_var = stu_serilizer(data=data)
        if serializers_var.is_valid():
            serializers_var.save()
            return Response({ 'payload': serializers_var.data }, status=200)
        return Response({ 'payload': serializers_var.data, 'error': serializers_var.errors }, status=403)
    
    def put(self, request, id):
        data = request.data 
        std_obj = Student.objects.get(id= id)
        serializers_var = stu_serilizer(std_obj, data=data)
        if serializers_var.is_valid():
            serializers_var.save()
            return Response({ 'payload': serializers_var.data }, status=200)
        return Response({ 'payload': serializers_var.data, 'error': serializers_var.errors }, status=403)
    
    def patch(self, request, id):
        data = request.data 
        std_obj = Student.objects.get(id= id)
        serializers_var = stu_serilizer(std_obj, data=data, partial = True)
        if serializers_var.is_valid():
            serializers_var.save()
            return Response({ 'payload': serializers_var.data }, status=200)
        return Response({ 'payload': serializers_var.data, 'error': serializers_var.errors }, status=403)
    
    def delete(self, request, id):
        try:
            data = request.data     
            Student.objects.get(id= id).delete()  
            return Response({ 'Message':f"Deleted user of id {id}" }, status=200)
        
        except Student.DoesNotExist:
            return Response({'error_reason': 'Student not found', 'message': 'Hint: ID is not valid'}, status=404)
        except Exception as e:
           return Response({ 'payload': data, 'error': e }, status=403)


# @api_view(['GET'])
# def home(request):
#     # std_obj = Student.objects.all()
#     std_obj = StudentMark.objects.all()
#     serializer_var = std_mark_serializers(std_obj, many = True)

#     return Response({
#         'status':200,
#         'payload': serializer_var.data
#     })

# @api_view(['post'])
# def post_std(request):
#     data = request.data
#     serializer_var= stu_serilizer(data=data)

#     # if data['age']<18: # we dont use this here instead in srylizer
#         # return Response({'status':403,'payload': data, 'error_data' : data['age'],'message': 'Age Must me greater then 18' })

#     if serializer_var.is_valid():
#         serializer_var.save()
#         return Response({'status':200,'payload': data,'message': 'post student success' })
#     else:
#         return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })

# #update using put 
# @api_view(['put'])
# def put_std(request, id):
#     data = request.data
#     try:
#         student = Student.objects.get(id= id)
#         serializer_var= stu_serilizer(student, data=data)
#         if serializer_var.is_valid():
#             serializer_var.save()
#             return Response({'status':200,'payload': data,'message': 'post student success' })
#         else:
#             return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })
#         pass
#     except Exception as e:
#         return Response({'status':403,'error reason' : f'{e}' , 'message': 'hint: ID is not valid' })

# @api_view(['patch'])
# def patch_std(request, id):
#     # try:
#         data = request.data
#         student = Student.objects.get(id= id)
#         serializer_var= stu_serilizer(student, data=data, partial =True)
#         if serializer_var.is_valid():
#             serializer_var.save()
#             return Response({'status':200,'payload': data,'message': 'post student success' })
#         else:
#             return Response({'status':403,'payload': data,'error reason' : serializer_var.errors , 'message': 'Bad request here' })
#         pass
#     # except Exception as e:
#     #     return Response({'status':403,'error reason' : f'{e}' , 'message': 'hint: ID is not valid' })

# # ?id=1
# @api_view(['delete'])
# def delete_std(request):
#     id = request.GET.get('id')
#     try:
#         std_obj = Student.objects.get(id=id)
#         std_obj.delete()
#         return Response({'status': 200,'message': f'Deleted  id number: {id}'}, status=200)
#     except Student.DoesNotExist:
#         return Response({'status': 404, 'error_reason': 'Student not found', 'message': 'Hint: ID is not valid'}, status=404)
#     except Exception as e:
#         return Response({'status':403,'error reason' : f'{e}' , 'message': 'hint: ID is not valid' })



