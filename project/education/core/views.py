import json
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = None
        if request.GET.get('view'):
            queryset = Course.objects.all()
        elif request.user.is_teacher:
            queryset = Course.objects.filter(teacher=request.user)
        elif request.user.is_authenticated:
            queryset = Course.objects.filter(listeners__exact=request.user)
        serializer = CourseSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = None
        if request.user.is_teacher:
            queryset = Course.objects.filter(teacher=request.user)
        elif request.user.is_authenticated:
            queryset = Course.objects.filter(listeners__exact=request.user)
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(course, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        if request.user.is_teacher:
            blob = request.data.get('document').read().decode("utf-8")
            blob = json.loads(blob)
            serializer = CourseSerializer(data=blob)
            if serializer.is_valid():
                serializer = serializer.data
                syndicate = Course.objects.create(teacher=request.user,
                                                  title=serializer.get('title'),
                                                  )
                serializer = CourseSerializer(syndicate, context={'request': request})

                # files = request.FILES
                # for file in files:
                #     if file != 'document':
                #         document = Document.objects.create(course=course, file=files.get(file),
                #                                            is_presentation=True)

                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'Function is allowed for teachers only.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        if request.user.is_teacher:
            blob = request.data.get('document').read().decode("utf-8")
            blob = json.loads(blob)
            serializer = CourseSerializer(data=blob)
            if serializer.is_valid():
                try:
                    course = Course.objects.get(pk=pk, teacher=request.user)
                    serializer = serializer.data

                    course.name = serializer.get('title')
                    course.save()
                    serializer = CourseSerializer(course, context={'request': request})

                    # files = request.FILES
                    # for file in files:
                    #     if file != 'document':
                    #         document = Document.objects.create(syndicate=syndicate, file=files.get(file),
                    #                                            is_presentation=True)

                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Course.DoesNotExist:
                    response = {'message': 'Function is allowed for manager only.'}
                    return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'Function is allowed for managers only.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


class StaticAuth(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, _):
        return Response()
