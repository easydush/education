from rest_framework import serializers

from core.models import Course, Lesson

from account.serializers import UserInfoSerializer

from studying.serializers import CourseListenerSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class CourseWithListenersSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()
    listeners = serializers.SerializerMethodField('get_listeners')

    def get_listeners(self, obj):
        return ','.join(list(map(lambda a: a.listener.name, (list(obj.listeners.all())))))

    class Meta:
        model = Course
        fields = '__all__'
        include = ['listeners']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
