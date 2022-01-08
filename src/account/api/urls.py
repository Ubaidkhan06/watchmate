from account.api.views import logout_view, registration_view
from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt.views import (TokenObtainPairView,
#                                             TokenRefreshView)

urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout_view, name='logout'),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
