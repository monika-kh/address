from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Block, District, State
from .serializers import (BlockSerializer, DistrictSerializer, StateSerializer,
                          WardSerializer)
from .services import (BlockDetailService, BlockListService,
                       CreateBlockService, CreateWardService,
                       DeleteBlockService, DeleteDistrictService,
                       DistrictDetailService, GetDisrtictService,
                       PostDistrictService, UpdateBlockService,
                       UpdateDistService, UpdateWardService, WardDetailService,
                       WardListService)

# Create your views here.


class StateListView(APIView):
    """
    List all State, or create a new state.
    """

    def get(self, request):
        state = State.objects.all()
        serializer = StateSerializer(state, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StateDetailView(APIView):
    """
    Retrieve, update or delete a state instance.
    """

    def get_object(self, state_id):
        try:
            return State.objects.get(pk=state_id)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, state_id):
        state = self.get_object(state_id)
        serializer = StateSerializer(state)
        return Response(serializer.data)

    def put(self, request, state_id):
        state = self.get_object(state_id)
        serializer = StateSerializer(state, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_id):
        state = self.get_object(state_id)
        state.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DistrictListView(APIView):
    """
    List all district, or create a new district.
    """

    def get(self, request, state_id):
        try:
            state = GetDisrtictService.execute({"state_id": state_id})
            serializer = DistrictSerializer(state, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except State.DoesNotExist:
            return Response(
                {"ERROR": "Invalid state_id -{}".format(state_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, state_id):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            dist = PostDistrictService.execute(
                {"state_id": state_id, "data": request.data}
            )
            serialize = DistrictSerializer(dist)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DistrictDetailView(APIView):
    def get(self, request, state_id, dist_id):
        try:
            dist = DistrictDetailService.execute(
                {"state_id": state_id, "dist_id": dist_id}
            )
            serializer = DistrictSerializer(dist)
            return Response(serializer.data)
        except District.DoesNotExist:
            return Response(
                {"ERROR": "Invalid dist_id- {}".format(dist_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except State.DoesNotExist:
            return Response(
                {"ERROR": "Invalid state_id -{}".format(state_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, state_id, dist_id):
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            dist = UpdateDistService.execute(
                {"state_id": state_id, "dist_id": dist_id, "data": request.data}
            )
            serialize = DistrictSerializer(dist)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_id, dist_id):
        DeleteDistrictService.execute({"state_id": state_id, "dist_id": dist_id})
        return Response({"message": "Deleted"}, status=200)


class BlockListView(APIView):
    def get(self, request, state_id, dist_id):
        try:
            block = BlockListService.execute({"state_id": state_id, "dist_id": dist_id})
            serializer = BlockSerializer(block, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except State.DoesNotExist:
            return Response(
                {"ERROR": "Invalid dist_id -{}".format(dist_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, state_id, dist_id):
        serializer = BlockSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            block = CreateBlockService.execute(
                {"state_id": state_id, "dist_id": dist_id, "data": request.data}
            )
            serialize = BlockSerializer(block)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlockDetailView(APIView):
    def get(self, request, state_id, dist_id, block_id):
        try:
            block = BlockDetailService.execute(
                {"state_id": state_id, "dist_id": dist_id, "block_id": block_id}
            )
            serializer = BlockSerializer(block)
            return Response(serializer.data)
        except District.DoesNotExist:
            return Response(
                {"ERROR": "Invalid dist_id- {}".format(dist_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except Block.DoesNotExist:
            return Response(
                {"ERROR": "Invalid block_id -{}".format(block_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, state_id, dist_id, block_id):
        serializer = BlockSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            update_block = UpdateBlockService.execute(
                {
                    "state_id": state_id,
                    "dist_id": dist_id,
                    "block_id": block_id,
                    "data": request.data,
                }
            )
            serialize = BlockSerializer(update_block)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_id, dist_id, block_id):
        DeleteBlockService.execute(
            {"state_id": state_id, "dist_id": dist_id, "block_id": block_id}
        )
        return Response({"message": "Deleted"}, status=200)


class WardListView(APIView):
    def get(self, request, state_id, dist_id, block_id):
        try:
            ward = WardListService.execute(
                {"state_id": state_id, "dist_id": dist_id, "block_id": block_id}
            )
            serializer = WardSerializer(ward, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Block.DoesNotExist:
            return Response(
                {"ERROR": "Invalid block_id -{}".format(block_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def post(self, request, state_id, dist_id, block_id):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            ward = CreateWardService.execute(
                {
                    "state_id": state_id,
                    "dist_id": dist_id,
                    "block_id": block_id,
                    "data": request.data,
                }
            )
            serialize = WardSerializer(ward)
            return Response(serialize.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WardDetailView(APIView):
    def get(self, request, state_id, dist_id, block_id, ward_id):
        try:
            ward = WardDetailService.execute(
                {
                    "state_id": state_id,
                    "dist_id": dist_id,
                    "block_id": block_id,
                    "ward_id": ward_id,
                }
            )
            serializer = WardSerializer(ward)
            return Response(serializer.data)
        except District.DoesNotExist:
            return Response(
                {"ERROR": "Invalid ward_id- {}".format(ward_id)},
                status.HTTP_404_NOT_FOUND,
            )
        except Block.DoesNotExist:
            return Response(
                {"ERROR": "Invalid block_id -{}".format(block_id)},
                status.HTTP_404_NOT_FOUND,
            )

    def put(self, request, state_id, dist_id, block_id, ward_id):
        serializer = WardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            ward = UpdateWardService.execute(
                {
                    "state_id": state_id,
                    "dist_id": dist_id,
                    "block_id": block_id,
                    "ward_id": ward_id,
                    "data": request.data,
                }
            )
            serialize = WardSerializer(ward)
            return Response(serialize.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, state_id, dist_id, block_id, ward_id):
        DeleteBlockService.execute(
            {
                "state_id": state_id,
                "dist_id": dist_id,
                "block_id": block_id,
                "ward_id": ward_id,
            }
        )
        return Response({"message": "Deleted"}, status=200)
