from django.contrib import admin
from django.urls import path
from product.views import (products_list_api_view, product_detail,
                           review_list, review_detail, category_list, category_detail)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/categories/', category_list),
    path('api/v1/categories/<int:id>/', category_detail),
    path('api/v1/products/', products_list_api_view),
    path('api/v1/products/<int:id>/', product_detail),
    path('api/v1/reviews/', review_list,),
    path('api/v1/reviews/<int:id>/', review_detail),
]
