from django.conf.urls import url, include

from docs.views import DocsView

urlpatterns = [
    url(
        r"^doc$", DocsView.as_view(), name="docs"
    ),
]