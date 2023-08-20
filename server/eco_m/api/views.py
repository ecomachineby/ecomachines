import jwt
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.middleware import csrf
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import (
    ReadOnlyModelViewSet, ViewSet, GenericViewSet,
)

from about.models import About, HelpText, Step
from about.serializers import AboutSerializer, HelpTextSerializer, StepSerializer
from api.serializers import UserSerializer, LoginSerializer, SenderSerializer, RecoverPasswordSerializer
from api.utils import (
    MessageHandler,
    email_common, decode_jwt, create_jwt,
)
from article.models import Article
from article.serializers import ArticleSerializer
from client.models import Client
from client.serializers import ClientSerializer, CommentSerializer, CommentCreateSerializer
from contact.models import Contact
from contact.serializers import ContactSerializer
from product.models import Product
from product.serializers import ProductSerializer
from service.models import Service
from service.serializers import ServiceSerializer
from api.tasks import email_task


class CSRFViewSet(GenericViewSet):
    def list(self, request) -> Response:
        csrf_token = csrf.get_token(request)
        return Response({"csrfToken": csrf_token}, status=status.HTTP_200_OK)


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginViewSet(GenericViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context=self.get_serializer_context()
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        token = create_jwt(user)

        response = Response(status=status.HTTP_200_OK)
        response.data = {
            "message": "Login was success",
            "jwt": str(token),
        }

        return response


class TokenAuthenticateViewSet(ViewSet):

    def list(self, request):
        bearer_token = request.META.get('HTTP_AUTHORIZATION')
        token = bearer_token.split("Bearer ")[1]
        try:
            data = decode_jwt(token)

            user = User.objects.get(id=data["id"])
            login(request, user)

            return Response({"message": f"User {user.username} authorize"})

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("JWT token has expired.")

        except jwt.InvalidTokenError:
            raise AuthenticationFailed(f"Invalid JWT token.Token {token}")

        except Exception as e:
            raise AuthenticationFailed(f"{e}")


class LogoutViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        logout(request)
        response = Response()
        response.data = {"message": "User logout"}
        response.status_code = status.HTTP_200_OK
        response.delete_cookie(key="jwt")

        return response


class AboutViewSet(ReadOnlyModelViewSet):
    queryset = About.objects.prefetch_related(
        "steps",
    ).all()
    serializer_class = AboutSerializer

    def get_queryset(self):
        if self.action == "retrieve":
            queryset = Step.objects.all()
            return queryset
        return super().get_queryset()

    def get_serializer_class(self):
        if self.get_object() and self.action == "retrieve":
            return StepSerializer

        return super().get_serializer_class()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ArticleViewSet(ReadOnlyModelViewSet):
    queryset = Article.objects.prefetch_related(
    ).all()
    serializer_class = ArticleSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.prefetch_related(
        "images",
    ).filter(published=True).all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContactViewSet(ReadOnlyModelViewSet):
    queryset = Contact.objects.select_related(
    ).prefetch_related(
        "messanger",
        "detail_info",
    ).all()
    serializer_class = ContactSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class HelpTextViewSet(ReadOnlyModelViewSet):
    queryset = HelpText.objects.all()
    serializer_class = HelpTextSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ServiceViewSet(ReadOnlyModelViewSet):
    queryset = Service.objects.prefetch_related(
        "stages",
    ).all()
    serializer_class = ServiceSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            self.queryset,
            many=True,
            context=self.get_serializer_context(),
        )
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientViewSet(GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Client.objects.prefetch_related(
        "files",
        "comments",
        "products__product",
        "products__files",
    ).all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CommentCreateSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        bearer_token = request.META.get('HTTP_AUTHORIZATION')
        if bearer_token:
            try:
                token = bearer_token.split("Bearer ")[1]
                data = decode_jwt(token)

                user = User.objects.get(id=data["id"])
                client = Client.objects.get(user=user)

                serializer = ClientSerializer(
                    client,
                    context=self.get_serializer_context()
                )

                return Response(serializer.data, status=status.HTTP_200_OK)

            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed("JWT token has expired.")
            except jwt.InvalidTokenError:
                raise AuthenticationFailed(
                    f"Invalid JWT token."
                )
            except Exception as e:
                raise AuthenticationFailed(f"{e}")

        raise AuthenticationFailed("Unauthenticated")

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        bearer_token = request.META.get('HTTP_AUTHORIZATION')

        if bearer_token:
            token = bearer_token.split("Bearer ")[1]

            data = decode_jwt(token)
            user = User.objects.get(id=data["id"])
            client = Client.objects.get(user=user)

            if serializer.is_valid():
                try:
                    serializer.validated_data["profile"] = client

                    comment = serializer.save()

                    body = MessageHandler(
                        validated_data=serializer.validated_data,
                    ).main()
                    subject = serializer.validated_data["message"]

                    client.comments.add(
                        comment
                    )
                    # email_common(
                    #     subject=subject,
                    #     body=body,
                    # )
                    email_task.delay(
                        subject=subject,
                        message=body,
                    )

                    return Response({"message": f"New review from {client.user}"}, status=status.HTTP_201_CREATED)

                except Exception as e:
                    return Response(
                        {"data": serializer.data, "error": str(e)},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response(
                {"data": str(serializer), "error": serializer.error_messages},
                status=status.HTTP_400_BAD_REQUEST,
            )

        raise AuthenticationFailed("Unauthenticated")


class SenderViewSet(GenericViewSet):
    serializer_class = SenderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                body = MessageHandler(
                    validated_data=serializer.validated_data,
                ).main()
                subject = serializer.validated_data["message"]

                email_task.delay(
                    subject=subject,
                    message=body,
                )

                # result = email_common(
                #     subject=subject,
                #     body=body,
                # )

                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"data": serializer.data},
            status=status.HTTP_400_BAD_REQUEST,
        )


class RecoverPasswordViewSet(GenericViewSet):
    serializer_class = RecoverPasswordSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            try:
                body = MessageHandler(
                    validated_data=serializer.validated_data,
                ).main()
                subject = serializer.validated_data["message"]

                email_task.delay(
                    subject=subject,
                    message=body,
                )
                # email_common(
                #     subject=subject,
                #     body=body,
                # )

                return Response({"message": "Success"}, status=status.HTTP_201_CREATED)

            except Exception as e:
                return Response(
                    {"error": str(e)},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        return Response(
            {"data": serializer.data, "error": serializer.error_messages},
            status=status.HTTP_400_BAD_REQUEST,
        )
