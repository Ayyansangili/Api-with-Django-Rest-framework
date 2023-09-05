
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework.response import Response
from rest_framework import status
from .service_views import *

from .models import *


class AddUser(APIView):
    class InputSerializer(serializers.Serializer):
        
        user_name = serializers.CharField(required = True)
        email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
        
        firstname = serializers.CharField(required = True)
        lastname = serializers.CharField(required = False)
        #mobile = serializers.CharField(allow_null=True)
        #user_type = serializers.CharField()
        #client_id = serializers.IntegerField(required=False, allow_null=True)
        #client_account_ids = serializers.ListField(child=serializers.IntegerField(), required=False, allow_null=True)
        password  = serializers.CharField(required = True)

    def post(self, request):
        
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usr = create_user(**serializer.validated_data)
        #log_api_history.delay(request.data, {'user': usr.id}, 'AddUser', request.user.id)
        #return Response({'data': {'user': usr.id}}, status=status.HTTP_201_CREATED)
        return Response(usr,status = status.HTTP_201_CREATED)
    
class AddCollectionQuery(APIView):
    class InputSerializer(serializers.Serializer):
        key = serializers.CharField()
        query = serializers.CharField()
    
    def post(self,request):
      
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        Cq = create_collection_query(**serializer.validated_data)
        return Response({'data': {'key':"success"}},status=status.HTTP_201_CREATED)
    
class FetchUserList(APIView):
    def post(self, request):
       
        roles_list = fetch_user_list()

        return Response({'data': {'roles_list': roles_list}}, status=status.HTTP_200_OK)
    
class GetUserDetail(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)

    def post(self, request):
        
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role = get_user_detail(serializer.validated_data.get('id'))

        return Response({'data': {'role': role}}, status=status.HTTP_200_OK)
    
class UpdateUserDetails(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)
        email = serializers.EmailField(required=True)
        
        password = serializers.CharField(required=True)

    def post(self, request):
        
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        role_code = update_user_details(**serializer.validated_data)

        #log_api_history.delay(request.data, {'role_code': role_code}, 'UpdateRoleDetails', request.user.id)
        return Response({'data': {'role_code': role_code}}, status=status.HTTP_200_OK)
    
class RemoveUser(APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=True)

    def post(self,request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_details = remove_user(**serializer.validated_data)
        return Response({'data': {'user_details': user_details}}, status=status.HTTP_200_OK)

    


# Create your views here.
