from rest_framework import mixins, viewsets

class DetailViewSet(
  mixins.CreateModelMixin,
  mixins.RetrieveModelMixin,
  mixins.UpdateModelMixin,
  mixins.DestroyModelMixin,
  viewsets.GenericViewSet,):
    pass

class ReadOnlyDetailViewSet(
  mixins.RetrieveModelMixin,
  viewsets.GenericViewSet):
    pass

class ListViewSet(
  mixins.ListModelMixin,
  viewsets.GenericViewSet):
    pass
