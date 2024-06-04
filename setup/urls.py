from django.contrib import admin
from django.urls import path, include

from members.views import (
    MembersListViwe,
    MembersCreateViwe,
    MembersUpdateViwe,
    MembersDeleteViwe,
    NewUser,
    ExcelDownloadView,
    Login,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Login.as_view(), name="login"),
    path("newuser/", NewUser.as_view(), name="newu_user"),
    path("list/", MembersListViwe.as_view(), name="members_list"),
    path("create/", MembersCreateViwe.as_view(), name="members_create"),
    path("update/<int:pk>", MembersUpdateViwe.as_view(), name="members_update"),
    path("delete/<int:pk>", MembersDeleteViwe.as_view(), name="members_delete"),
    path("download-excel/", ExcelDownloadView.as_view(), name="download_excel"),
]
