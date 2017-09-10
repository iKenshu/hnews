from django.conf.urls import url, include

from .views import NewList, NewAdd, NewEdit, NewDetail, VoteView, CommentView, NewDelete

app_name = 'New'
urlpatterns = [
    url(r'^$', NewList.as_view(), name='list'),
    url(r'^add/', NewAdd.as_view(), name='add'),
    url(r'^edit/(?P<pk>\d+)/$', NewEdit.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', NewDelete.as_view(), name='delete'),
    url(r'^detail/(?P<pk>\d+)/$', NewDetail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/comment$', CommentView.as_view(), name='comment'),
    url(r'^vote/(?P<pk>\d+)/$', VoteView.as_view(), name='vote'),
]   