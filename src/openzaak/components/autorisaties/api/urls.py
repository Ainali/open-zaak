from django.conf import settings
from django.conf.urls import url
from django.urls import include, path

from vng_api_common import routers
from vng_api_common.schema import SchemaView as _SchemaView

from ..api.schema import info
from .viewsets import ApplicatieViewSet

router = routers.DefaultRouter()
router.register("applicaties", ApplicatieViewSet)


# set the path to schema file
class SchemaView(_SchemaView):
    schema_path = settings.SPEC_URL["autorisaties"]
    info = info


urlpatterns = [
    url(
        r"^v(?P<version>\d+)/",
        include(
            [
                # API documentation
                url(
                    r"^schema/openapi(?P<format>\.json|\.yaml)$",
                    SchemaView.without_ui(cache_timeout=settings.SPEC_CACHE_TIMEOUT),
                    name="schema-json-autorisaties",
                ),
                url(
                    r"^schema/$",
                    SchemaView.with_ui(
                        "redoc", cache_timeout=settings.SPEC_CACHE_TIMEOUT
                    ),
                    name="schema-redoc-autorisaties",
                ),
                # actual API
                url(r"^", include(router.urls)),
                # should not be picked up by drf-yasg
                path("", router.APIRootView.as_view(), name="api-root-autorisaties"),
                path("", include("vng_api_common.api.urls")),
            ]
        ),
    )
]
