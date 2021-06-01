from django.conf.urls import url
from django.urls import path
from .views import DetailProduct, ListProducView, ProducView, RegisterView, TestAPIView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.documentation import include_docs_urls


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Contact List API",
        default_version='v1',
        description="An api for contacts",
        terms_of_service="https://devblock.net/",
        contact=openapi.Contact(email="trieudc@devblock.net"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('info/', TestAPIView.as_view()),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('add-product/', ProducView.as_view(), name='add_product'),
    path('list-product/', ListProducView.as_view(), name='list_product'),
    path('products/<int:pk>/', DetailProduct.as_view(), name='singleproduct'),
    url(r'^docs/$', include_docs_urls(title='My API title')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),
    path("redoc", schema_view.with_ui('redoc',
                                      cache_timeout=0), name='schema-redoc'),

]