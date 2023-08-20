from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r"csrf_token", views.CSRFViewSet, basename='csrf_token')
router.register(r"login", views.LoginViewSet, basename='login')
router.register(r"logout", views.LogoutViewSet, basename='logout')
router.register(r"token_authenticate", views.TokenAuthenticateViewSet, basename='auth_token')
router.register(r"recover_password", views.RecoverPasswordViewSet, basename='recover_password')
router.register(r"sender", views.SenderViewSet, basename='sender')
router.register(r'abouts', views.AboutViewSet, basename='abouts')
router.register(r'articles', views.ArticleViewSet, basename='articles')
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'contacts', views.ContactViewSet, basename='contact')
router.register(r'client', views.ClientViewSet, basename='client')
router.register(r'services', views.ServiceViewSet, basename='services')
router.register(r'help_text', views.HelpTextViewSet, basename='help_text')


urlpatterns = [
    path("register/", views.RegisterView.as_view()),
    path("", include(router.urls)),
]

