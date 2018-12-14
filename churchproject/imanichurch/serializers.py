from django.core.mail import send_mail
from django.conf import settings
from rest_framework import serializers

from imanichurch.models import (
    User, Designation, Sermon, Department,
    Event, EventCategory, SermonCategory)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'member_type', 'image',
                  'username', 'phone_number', 'email', 'is_active',
                  'password', 'description', 'is_active')


    #     member_type = serializers.PrimaryKeyRelatedField(
    #         queryset=Designation.objects.all())

    # def create(self, validated_data):
    #     user = User.objects.create(
    #         username=validated_data['username'],
    #         first_name=validated_data['first_name'],
    #         last_name=validated_data['last_name'],
    #         email=validated_data['email'],
    #         phone_number=validated_data['phone_number'],
    #         description=validated_data['description'],
    #         # image = validated_data['image'],
    #         is_active=validated_data['is_active'],
    #     )
    #     user.member_type = validated_data['member_type']
    #     user.set_password(validated_data['password'])

    #     user.save()

    #     subject = 'Email Confirmation'
    #     message = 'Url link here'
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [user.email]

    #     send_mail(subject, message, from_email,
    #               recipient_list, fail_silently=True)
    #     return user


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class SermonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sermon
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'


class SermonCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SermonCategory
        fields = '__all__'
