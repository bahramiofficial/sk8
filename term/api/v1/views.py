from rest_framework import generics
from rest_framework.response import Response
from term.models import Term as TermModel, Session as SessionModel
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly

from term.api.v1.serializers import TermListSerializer, SessionSerializer,TermCreateRequestSerializer




class TermListAPIView(generics.ListAPIView):
    queryset = TermModel.objects.all()
    serializer_class = TermListSerializer
    # permission_classes = [IsAuthenticated]

class TermCreateAPIView(generics.CreateAPIView):
    queryset = TermModel.objects.all()
    serializer_class = TermCreateRequestSerializer
    # permission_classes = [IsAuthenticated]

class TermRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TermModel.objects.all()
    serializer_class = TermListSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]


class SessionAPIView(generics.ListCreateAPIView):
    queryset = SessionModel.objects.all()
    serializer_class = SessionSerializer
    # permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]



# class TermDestroyAPIView(generics.DestroyAPIView):
#     def delete(self, request, *args, **kwargs):
#         find
#         return self.destroy(request, *args, **kwargs)

# class TermUpdateAPIView(generics.UpdateAPIView):
#     """
#     Concrete view for updating a model instance.
#     """
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

# class TermDeActiveAPIView(generics.UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     def patch(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         instance = self.get_object()
#         instance.active = False
#         instance.save()
#         self.update(request, *args, **kwargs)
#         return Response(status=200)