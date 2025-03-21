from django.urls import path,include
from pages import ViewsCategories, viewsProduct,viewsFavorate,viewsCart,viewsCoupon,ViewsOrder,ViewsOffer,AddsView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView


router=DefaultRouter()
# router.register('product',views.viewsets_products)
router.register('fav',viewsFavorate.viewsets_fav)


urlpatterns = [
    path("categoties/",ViewsCategories.Cat_list.as_view()),
    path("categoties/<int:pk>/",ViewsCategories.Cat_pk.as_view()),


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
    path("cartdelete/<int:cartId>/",viewsCart.cartdelete),
    path("cartinsert/",viewsCart.cartinsert),
    path("update/<int:cart_id>/",viewsCart.updatequantity),
    path("cartupdate/<int:cart_id>/",viewsCart.updatecart),
    path("cartdeleteall/<int:user_id>/",viewsCart.cartdeleteall),


    # url coupon 
    path("checkcoupon/",viewsCoupon.checCoupon),
    path("coupon/",viewsCoupon.couponList.as_view()),
    path("coupon/<int:pk>/",viewsCoupon.coupon_pk.as_view()),


    # url order
    path("order/",ViewsOrder.OrderCreateList.as_view()),
    path("order/<int:pk>/",ViewsOrder.OrderRetrieveUpdateDestroy.as_view()),
    path("orderitemlist/<int:orderId>/",ViewsOrder.getOrderItem),
    path("orderitem/",ViewsOrder.addorderItem),

    path("orderitem/<int:pk>/",ViewsOrder.OrderItemRetrieveUpdateDestroy.as_view()),

    # offer product
    path("offer/",ViewsOffer.OfferCreateList.as_view()),
    path("offer/<int:pk>/",ViewsOffer.OfferRetrieveUpdateDestroy.as_view()),

    path('adds/', AddsView.adsView),
    path('adds/<int:pk>/', AddsView.adsViewPk),
    # path('createadds/', AddsView.createAdds),



]