from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('item/<int:pk>', ShowItemView.as_view(), name='show-item'),
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy-item'),
    path('success/',SuccessView.as_view(),name='success'),
    path('cancel/',CancelView.as_view(),name='cancel'),
]