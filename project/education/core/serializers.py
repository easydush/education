from rest_framework import serializers

from core.models import Course, Lesson

from account.serializers import UserInfoSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
