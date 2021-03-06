from django.core.exceptions import ObjectDoesNotExist
#
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
#
from user_profile.models import ProfileModel
#


class UserCreateView(CreateAPIView):

    def create(self, request, *args, **kwargs):
        if self.has_permission_create():
            return super().create(request, *args, **kwargs)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def has_permission_create(self):
        return True

    def perform_create(self, serializer):
        serializer.save(profile_model=ProfileModel.objects.get(id=self.request.user.id))


class UserCreateOnlyOne(UserCreateView):

    def create(self, request, *args, **kwargs):
        try:
            self.handle_exists(self.get_instance_create())
            return Response(status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return super().create(request, *args, **kwargs)

    def get_instance_create(self):
        pass
        # return self.queryset.get(profile_model=self.request.user.id)

    def handle_exists(self, instance):
        pass


class UserCreateLike(UserCreateOnlyOne):

    def handle_exists(self, instance):
        new_type_like = self.request.data.get('type_like')

        if new_type_like is None or int(new_type_like) == -1:
            instance.delete()
        else:
            instance.type_like = new_type_like
            instance.full_clean()
            instance.save()


class UserCreateShare(UserCreateView):

    def create(self, request, *args, **kwargs):
        if not self.has_permission_create():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            count_user_share = self.get_count_user_share()
        except ObjectDoesNotExist:
            count_user_share = 0

        if count_user_share >= self.get_max_share():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if count_user_share == 0:
            return self.handle_create_share()
        else:
            return self.handle_update_share()

    # limit share
    @staticmethod
    def get_max_share():
        return 0

    # count share of user
    def get_count_user_share(self):
        return self.queryset.get(profile_model=self.request.user.id).count

    # has not share before
    def handle_create_share(self):
        pass

    # has share before
    def handle_update_share(self):
        pass
