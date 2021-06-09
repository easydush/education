import json
from django.db.models import Q
from rest_framework import viewsets, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Lesson, Answer
from .serializers import CourseSerializer, LessonSerializer, CourseWithListenersSerializer
from studying.models import ListenerAnswer, CourseListener


class CourseViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Course.objects.none()
        if request.GET.get('view'):
            queryset = Course.objects.all()
        elif request.user.is_teacher:
            queryset = Course.objects.filter(teacher=request.user)
        elif request.user.is_authenticated:
            queryset = Course.objects.filter(listeners__listener=request.user)
        serializer = CourseSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        course = get_object_or_404(queryset, pk=pk)
        serializer = CourseWithListenersSerializer(course, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        if request.user.is_teacher:
            blob = request.data.get('document').read().decode("utf-8")
            blob = json.loads(blob)
            serializer = CourseSerializer(data=blob)
            if serializer.is_valid():
                serializer = serializer.data
                course = Course.objects.create(teacher=request.user,
                                               title=serializer.get('title'),
                                               )
                serializer = CourseSerializer(course, context={'request': request})
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


class LessonViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = None
        if request.user.is_authenticated and request.GET.get('course__id'):
            queryset = Lesson.objects.filter(
                Q(module__course__id=request.GET.get('course_id')) & Q(module__course__listeners__exact=request.user))
        serializer = LessonSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = None
        if request.user.is_teacher:
            queryset = Lesson.objects.filter(module__course__teacher=request.user)
        elif request.user.is_authenticated:
            queryset = Lesson.objects.filter(module__course__listeners__listener=request.user)
        course = get_object_or_404(queryset, pk=pk)
        serializer = LessonSerializer(course, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        if request.user.is_teacher:
            blob = request.data.get('document').read().decode("utf-8")
            blob = json.loads(blob)
            serializer = LessonSerializer(data=blob)
            if serializer.is_valid():
                serializer = serializer.data
                lesson = Lesson.objects.create(teacher=request.user,
                                               title=serializer.get('title'),
                                               )
                serializer = LessonSerializer(lesson, context={'request': request})
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
            serializer = LessonSerializer(data=blob)
            if serializer.is_valid():
                try:
                    lesson = Lesson.objects.get(pk=pk, teacher=request.user)
                    serializer = serializer.data

                    lesson.name = serializer.get('title')
                    lesson.save()
                    serializer = LessonSerializer(Lesson, context={'request': request})
                    return Response(serializer.data, status=status.HTTP_200_OK)
                except Lesson.DoesNotExist:
                    response = {'message': 'Function is allowed for manager only.'}
                    return Response(status=status.HTTP_403_FORBIDDEN)
            else:
                return Response(serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            response = {'message': 'Function is allowed for managers only.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


class AnswerViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def retrieve(self, request, pk=None):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk=None):
        if not request.user.is_teacher:
            listener = CourseListener.objects.get(listener=request.user)
            answer = Answer.objects.get(pk=pk)
            new_answer = ListenerAnswer.objects.create(listener=listener, answer=answer)
            if answer.is_right:
                listener.points += 1
                listener.save()
            return Response(status=status.HTTP_200_OK)
        else:
            response = {'message': 'Function is allowed for students only.'}
            return Response(response, status=status.HTTP_403_FORBIDDEN)


class StaticAuth(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, _):
        return Response()
