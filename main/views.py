from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework import mixins, viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import User, Likes
from .serializers import UsersRegisterSerializer, MatchSerializer, UsersListSerializer
from django_filters import rest_framework as filters


class UsersRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = UsersRegisterSerializer


class LikesAPIView(generics.ListCreateAPIView):
    queryset = Likes.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MatchSerializer


class DistanceFilter(filters.FilterSet):
    distance = filters.CharFilter(method='ids__in', label="Дистанция")

    def ids__in(self, queryset, value, *args, **kwargs):
        try:
            if args:
                distance = args[0].split(',')
                distance = [int(_uid) for _uid in distance]
                queryset = queryset.filter(uid__in=distance)
        except ValueError:
            pass
        return queryset

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'gender']


class UsersListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UsersListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DistanceFilter
