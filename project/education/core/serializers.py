from rest_framework import serializers

from core.models import Course, Lesson, Module, Answer, Question

from account.serializers import UserInfoSerializer

from studying.serializers import CourseListenerSerializer

from studying.models import CourseListener


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserInfoSerializer()
    points = serializers.SerializerMethodField('get_points')

    def get_points(self, obj):
        try:
            points = obj.listeners.get(listener=self.context.get('request').user).points
            return points
        except CourseListener.DoesNotExist:
            return 0

    class Meta:
        model = Course
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, )

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
    points = serializers.SerializerMethodField('get_points')

    def get_points(self, obj):
        try:
            points = obj.listeners.get(listener=self.context.get('request').user).points
            return points
        except CourseListener.DoesNotExist:
            return 0

    def check_joined(self, obj):
        return obj.listeners.filter(listener=self.context.get('request').user).exists()

    def get_listeners(self, obj):
        return ','.join(list(map(lambda a: a.listener.name, (list(obj.listeners.all())))))

    class Meta:
        model = Course
        fields = '__all__'
        include = ['listeners']
