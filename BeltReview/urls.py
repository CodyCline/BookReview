from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.login.urls', namespace='login')),
    url(r'^books/', include('apps.review.urls', namespace='review')),
]
