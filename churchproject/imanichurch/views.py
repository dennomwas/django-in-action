import requests
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes

from rest_framework import viewsets
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from imanichurch.models import (User, Event, Department,
                                Designation, Sermon,
                                EventCategory, SermonCategory)
from imanichurch.serializers import (UserSerializer, DesignationSerializer,
                                     EventSerializer, SermonSerializer, DepartmentSerializer,
                                     EventCategorySerializer, SermonCategorySerializer)


# class UserListView(APIView):
#     """
#     View to get all users and register new ones
#     """

# def get(self, request, format=None):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)

# def post(self, request, format=None):
#     serializer = UserSerializer(data=request.data)
#     if serializer.is_valid():

#         subject = 'Email Confirmation'
#         message = ''
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [request.data['email']]

#         send_mail(subject, message, from_email, recipient_list, fail_silently=True)

#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UserDetailView(APIView):
#     """
#     Retrieve, update or delete a user.
#     """
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         user = self.get_object(pk)
#         user.request.data['is_active'] = False
#         user.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            instance = serializer.save()
            instance.set_password(instance.password)
            instance.save()

            # send email confirmation and or phone_number activation
            subject = 'Email Confirmation'
            message = 'Url link here or template'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [request.data['email']]

            send_mail(subject, message, from_email,
                      recipient_list, fail_silently=True)

            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    permission_classes = (IsAuthenticated,)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    # TODO filter the query by event_date>today()


class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()
    serializer_class = SermonSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LeadershipViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # TODO filter the query by category=officials


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SermonCategoryViewSet(viewsets.ModelViewSet):
    queryset = SermonCategory.objects.all()
    serializer_class = SermonCategorySerializer


class EventCategoryViewSet(viewsets.ModelViewSet):
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer
