from django.urls import path

from .views import ProductList,ProductDetail,CommentCreate

urlpatterns = [
    path('', ProductList.as_view(), name = 'pro_list'),
    path('<int:pk>', ProductDetail.as_view(), name = 'pro_detail'),
    path('comment/<int:pk>', CommentCreate.as_view(), name= 'comment_create'),
]