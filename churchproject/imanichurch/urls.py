from rest_framework import routers

from imanichurch import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'sermons', views.SermonViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'departments', views.DepartmentViewSet)
router.register(r'leadership', views.UserViewSet)

urlpatterns = router.urls
