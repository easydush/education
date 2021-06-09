from rest_framework import serializers

from core.models import Course, Lesson, Module

from account.serializers import UserInfoSerializer

from studying.serializers import CourseListenerSerializer


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()

    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class ModuleSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)

    class Meta:
        model = Module
        fields = '__all__'


class CourseWithListenersSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()
    listeners = serializers.SerializerMethodField('get_listeners')
    is_joined = serializers.SerializerMethodField('check_joined')
    modules = ModuleSerializer(many=True)

    def check_joined(self, obj):
        return obj.listeners.filter(listener=self.context.get('request').user).exists()

    def get_listeners(self, obj):
        return ','.join(list(map(lambda a: a.listener.name, (list(obj.listeners.all())))))

    class Meta:
        model = Course
        fields = '__all__'
        include = ['listeners']
