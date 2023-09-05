from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    
    path('add_user',views.AddUser.as_view()),
    path('add_collection_query',views.AddCollectionQuery.as_view()),
    path('fetch_user_list',views.FetchUserList.as_view()),
    path('get_user_detail',views.GetUserDetail.as_view()),
    path('update_user_details',views.UpdateUserDetails.as_view()),
    path('remove_user',views.RemoveUser.as_view())
]