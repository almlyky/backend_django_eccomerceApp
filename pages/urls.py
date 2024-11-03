from django.urls import path,include
from . import ViewsCategories, viewsProduct,viewsFavorate,viewsCart
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView


router=DefaultRouter()
# router.register('product',views.viewsets_products)
router.register('fav',viewsFavorate.viewsets_fav)


urlpatterns = [
    path("categoties/",ViewsCategories.Cat_list.as_view()),
    path("categoties/int:pk/",ViewsCategories.Cat_pk.as_view()),


    # path("categoties/<int:pk>/",ViewsCategories.cat_list.as_view()),    

    # path("product_cat/",viewsProduct.getFilterProduct),

    # path("product/<int:pk>/",viewsProduct.product_pk.as_view()),

    path("product/",viewsProduct.Product_list.as_view()),
    path("product/<int:pk>/",viewsProduct.Product_pk.as_view()),
    path("productAll/<int:user_id>/",viewsFavorate.getAllProduct),



    path("allproduct/<int:cat_fk>/<int:user_id>/",viewsFavorate.getAllProductfav),

    path("searchproduct/<int:user_id>/",viewsFavorate.getSearch2),


    path("addfav/",viewsFavorate.insert),

    path("favorite/<int:userid>/",viewsFavorate.getfavorite),

    path("deletfav/<int:pr_id>/<int:user_id>/",viewsFavorate.deletfav),

    # url get token
    path("gettoken/",TokenObtainPairView.as_view()),    

    # path("favorate/",viewsFavorate.getAllProduct),

    # path("test/",views.pro.as_view()),

    # path("mixin/",views.mixins_list.as_view()),
    # path("mixin/<int:pk>",views.mixins_pk.as_view()),

    # path("generic/",views.generic_list.as_view()),
    # path("generic/<int:pk>/",views.geneeic_pk.as_view()),

    # path("users/",views.users_pk.as_view()),

    path("",include(router.urls)),

    # path("api_token",obtain_auth_token)

    # urls cart
    path("cartlist/<int:userid>/",viewsCart.cartList),
    path("cartdelete/<int:pr_id>/<int:user_id>/",viewsCart.cartdelete),
    path("cartinsert/",viewsCart.cartinsert),
    path("update/<int:cart_id>/",viewsCart.updatequantity)


]