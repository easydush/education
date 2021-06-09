from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from core.models import Course
from studying.models import CourseListener
from studying.serializers import CourseListenerSerializer


class CourseListenerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CourseListener.objects.filter(course=request.GET.get('courseId'))
        serializer = CourseListenerSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = CourseListener.objects.all()
        listener = get_object_or_404(queryset, pk=pk)
        serializer = CourseListenerSerializer(listener, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        if not request.user.is_teacher:
            course = Course.objects.get(pk=request.data.get('courseId'))
            listener = CourseListener.objects.create(listener=request.user,
                                                     course=course)
            serializer = CourseListenerSerializer(listener, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            response = {'message': 'Function is allowed for teachers only.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)

    def update(self, request, pk=None):
        pass
