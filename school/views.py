from django.views.generic import ListView
from django.shortcuts import render
from .models import Student, Teacher


def lists(request):
    template = 'school/students_list.html'
    context = {
        'student_list': Student.objects.prefetch_related('teachers').order_by('group'),
        'teacher_list': Teacher.objects.prefetch_related('students')
    }
    return render(request, template, context)


# та же функциональность с использованием ListView
class Lists(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'student_list'
    ordering = 'group'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teacher_list'] = Teacher.objects.prefetch_related('students')
        return context
