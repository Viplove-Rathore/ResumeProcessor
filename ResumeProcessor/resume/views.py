from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .utils import extract_resume_data
from .serializers import CandidateSerializer
from .models import Candidate
from django.core.files.storage import default_storage
import os

class ResumeExtractView(APIView):
    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        file_name = default_storage.save(file.name, file)
        file_path = default_storage.path(file_name)

        try:

            resume_data = extract_resume_data(file_path)
            candidate = Candidate.objects.create(**resume_data)
            serializer = CandidateSerializer(candidate)
            os.remove(file_path)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



