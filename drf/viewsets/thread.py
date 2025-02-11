from django.db.models import QuerySet
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf.serializers.thread import ThreadSerializer
from my_project.models import Thread


class ThreadViewSet(CreateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    lookup_field = "user"
    pagination_class = LimitOffsetPagination

    @action(detail=False, methods=["get"], url_path="(?P<user_id>\w+)", url_name="users")
    def get_by_user(self, request, user_id=None):
        instances: QuerySet[Thread] = self.get_queryset().filter(user=user_id)
        page = self.paginate_queryset(instances)
        serializer = self.get_serializer(page if page is not None else instances, many=True)

        return self.get_paginated_response(serializer.data) if page is not None else Response({
            "count": len(instances),
            "next": None,
            "previous": None,
            "results": serializer.data
        })