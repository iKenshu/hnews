from django.conf.urls import url

from .views import SignUpView, SignInView, SignOutView

app_name = 'Profile'
urlpatterns = [
    url(r'^signup/$', SignUpView.as_view(), name='sign_up'),
    url(r'^signin/$', SignInView.as_view(), name='sign_in'),   
    url(r'^signout/$', SignOutView.as_view(), name='sign_out'),
]