from django.shortcuts import render
from rest_framework import viewsets

from imanichurch.models import User, Sermon, Event, Department


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    # TODO filter the query by event_date>today()

class SermonViewSet(viewsets.ModelViewSet):
    queryset = Sermon.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()

class LeadershipViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all();
    # TODO filter the query by category=officials
