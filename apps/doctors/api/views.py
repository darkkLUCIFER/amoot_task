from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from apps.doctors.api.serializers import GetDoctorTicketSerializer


class CreateDoctorTicketView(CreateAPIView):
    serializer_class = GetDoctorTicketSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        response_data = {
            'message': 'Ticket successfully created.',
            'data': serializer.data
        }
        return Response(
            response_data,
            status=status.HTTP_201_CREATED
        )
