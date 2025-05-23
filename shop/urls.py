from django.urls import path
from .views import index,product_detail,order_detail



urlpatterns = [
    path('',index,name='index'),
    path('category/<int:category_id>/',index, name='products_by_category'),
    path('detail/<int:product_id>/',product_detail,name='product_detail'),
    path('order/detail/<int:pk>/',order_detail,name='order_detail')
]