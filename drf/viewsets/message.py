from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from drf.serializers.message import MessageSerializer
from my_project.models import Message


class MessageViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    @action(detail=True, methods=["get"], url_path="mark-as-read", url_name="mark-as-read")
    def mark_as_read(self, *args, **kwargs):
        instance: Message = self.get_object()
        instance.is_read = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(data=serializer.data)

    @action(detail=False, methods=["get"], url_path="get-unread/(?P<user_id>\w+)", url_name="get-unread")
    def get_unread(self, *args, user_id=None, **kwargs):
        if not user_id.isdigit():
            return Response(data={"detail": "Please provide valid user id"}, status=status.HTTP_400_BAD_REQUEST)

        count_of_unread_messages = len(self.get_queryset().filter(thread__user=user_id,
                                                                  is_read=False))
        return Response(data={"unread_messages": count_of_unread_messages})
