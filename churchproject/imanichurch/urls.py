from rest_framework import routers
from rest_framework.authtoken import views
from django.urls import path, include

from imanichurch.views import (
    # UserListView, UserDetailView,
    DepartmentViewSet, UserViewSet,
    DesignationViewSet, SermonViewSet, EventViewSet, 
    SermonCategoryViewSet, EventCategoryViewSet)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'member-type', DesignationViewSet)
router.register(r'sermons', SermonViewSet)
router.register(r'sermon-category', SermonCategoryViewSet)
router.register(r'events', EventViewSet)
router.register(r'event-category', EventCategoryViewSet)
router.register(r'departments', DepartmentViewSet)
# router.register(r'leadership', UserViewSet)

urlpatterns = [
    path('login/', views.obtain_auth_token)
#     path('users/', UserListView.as_view()),
#     path('users/<int:pk>', UserDetailView.as_view())
]

urlpatterns += router.urls
