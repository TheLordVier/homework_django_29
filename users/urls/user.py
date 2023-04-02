from django.urls import path

from users.views.user import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView


urlpatterns = [
    path("", UserListView.as_view(), name="all_users"),
    path("<int:pk>/", UserDetailView.as_view(), name="detail_user"),
    path("create/", UserCreateView.as_view(), name="create_user"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="update_user"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete_user"),
]
