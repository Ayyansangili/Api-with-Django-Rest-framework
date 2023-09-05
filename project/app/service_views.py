import json

from .models import *
from django.core.exceptions import ValidationError
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import APIException
import datetime

from .collection_querry import exec_raw_sql
def create_user(**data):
    try:
        user = User(firstname=data.get('firstname'),username = data.get('user_name'),lastname=data.get('lastname'),password = data.get('password'),
                  email = data.get('email'))
        user.save()
        return user.username


    except Exception as e:
        raise APIException(e)
    
def fetch_user_list():
    try:
        roles_list = exec_raw_sql('D_USER_LIST', {})
        return roles_list

    except Exception as e:
        raise APIException(str(e))
    
def get_user_detail(id):
    try:
        roles = exec_raw_sql('D_USER_DETAIL',{'id': id})
        return roles
    
    except Exception as e:
        raise APIException(str(e))


def update_user_details(**data):
    try:
        chk_dupe_codes = User.objects.exclude(id=data.get('id')).filter(email=data.get('email'))
        print(chk_dupe_codes)
        if chk_dupe_codes.exists():
            raise APIException("Duplicate Role Code.")
        
        user = User.objects.filter(id=data.get('id')).first()
        user.email = data.get('email')
        user.password = data.get('password')
       
        user.save()

        return user.email

    except Exception as e:
        raise APIException(str(e))
    

def remove_user(**data):
    try:
        us = None
        if data.get('id', None) is not None:
            us = User.objects.filter(id=data.get('id')).first()

        if not us:
            raise ValidationError("User Id is not defined.")
        us.delete()
        return "Successfully Deleted"

    except Exception as e:
        raise APIException(e)
    
def create_collection_query(**data):
    try:
        collection_query = CollectionQuery()
        collection_query.key =data.get('key')
        collection_query.query = data.get('query')
        collection_query.save()
    except Exception as e:
        raise APIException(e)
