from django.urls import path,include
from . import views
from rest_framework import routers

from rest_framework_simplejwt import views as jwt_views





urlpatterns = [
    path('',views.searchfunction,name='search'),
	path('signup/',views.register,name="register"),
	path('login/',views.login,name="login"),
  
    path('<slug:doj>',views.specificapilist),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    #path('', include(router.urls)),
]
