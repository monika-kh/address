from django.urls import path

from .views import (BlockDetailView, BlockListView, DistrictDetailView,
                    DistrictListView, StateDetailView, StateListView,
                    WardDetailView, WardListView)

urlpatterns = [
    path("state/", StateListView.as_view(), name="state_list"),
    path("state/<int:state_id>", StateDetailView.as_view(), name="state_detail"),
    path("state/<int:state_id>/dist/", DistrictListView.as_view(), name="dist_list"),
    path(
        "state/<int:state_id>/dist/<int:dist_id>",
        DistrictDetailView.as_view(),
        name="dist_detail",
    ),
    path(
        "state/<int:state_id>/dist/<int:dist_id>/block/",
        BlockListView.as_view(),
        name="block_list",
    ),
    path(
        "state/<int:state_id>/dist/<int:dist_id>/block/<int:block_id>",
        BlockDetailView.as_view(),
        name="block_detail",
    ),
    path(
        "state/<int:state_id>/dist/<int:dist_id>/block/<int:block_id>/ward/",
        WardListView.as_view(),
        name="ward_list",
    ),
    path(
        "state/<int:state_id>/dist/<int:dist_id>/block/<int:block_id>/ward/<int:ward_id>",
        WardDetailView.as_view(),
        name="ward_detail",
    )
]
