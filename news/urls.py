from django.conf.urls import url, include

from .views import NewList, NewAdd, NewEdit, NewDetail, VoteView, CommentView, NewDelete

app_name = 'New'
urlpatterns = [
    url(
        regex=r'^$',
        view=NewList.as_view(),
        name='list'
    ),
    url(
        regex=r'^add/',
        view=NewAdd.as_view(),
        name='add'
    ),
    url(
        regex=r'^edit/(?P<pk>\d+)/$',
        view=NewEdit.as_view(),
        name='edit'
    ),
    url(
        regex=r'^delete/(?P<pk>\d+)/$',
        view=NewDelete.as_view(),
        name='delete'
    ),
    url(
        regex=r'^detail/(?P<pk>\d+)/$',
        view=NewDetail.as_view(),
        name='detail'
    ),
    url(
        regex=r'^detail/(?P<pk>\d+)/comment$',
        view=CommentView.as_view(),
        name='comment'
    ),
    url(
        regex=r'^vote/(?P<pk>\d+)/$',
        view=VoteView.as_view(),
        name='vote'
    ),
]
