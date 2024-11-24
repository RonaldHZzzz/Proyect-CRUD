
from django.contrib import admin
from django.urls import include, path
from api.views import createUserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

#rutas
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/register/",createUserView.as_view(),name="register"),
    path("api/token/",TokenObtainPairView.as_view(),name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(),name="fresh"),
    path("api-auth/",include("rest_framework.urls")),
    
]
