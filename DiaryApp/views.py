from . import services
from django.views import generic
from DiaryApp.models import KvantLesson, KvantHomeTask
from CoreApp.services.access import KvantStudentAccessMixin


class DiaryPageListView(KvantStudentAccessMixin, generic.ListView):
    model               = KvantLesson
    ordering            = ['-date', '-id']
    template_name       = 'DiaryApp/DiaryPage/index.html'
    context_object_name = 'lessons'

    def get_queryset(self):
        return services.getDiaryLessonQuery(self.request.user)


class LessonDetailView(services.LessonAccessMixin, generic.DetailView):
    model               = KvantLesson
    pk_url_kwarg        = 'lesson_identifier'
    context_object_name = 'lesson'
    template_name       = 'DiaryApp/LessonDetailView/index.html'


class TaskDetailView(services.TaskAccessMixin, generic.DetailView):
    model               = KvantHomeTask
    pk_url_kwarg        = 'task_identifier'
    context_object_name = 'task'
    template_name       = 'DiaryApp/TaskDetailView/index.html'
    