from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsListView, NewCarsCreateView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import LoginLoginView, LogoutLogoutView, RegisterFormView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginLoginView.as_view(), name='login'),
    path('logout/', LogoutLogoutView.as_view(), name='logout'),
    path('cars/', CarsListView.as_view(), name='cars_list'),
    path('new_car/', NewCarsCreateView.as_view(), name='new_car'),
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
