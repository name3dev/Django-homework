from django.shortcuts import render, redirect

# Create your views here.

from .forms import StudentForm


def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            request.session['student'] = form.cleaned_data
            return redirect('student_result')
    else:
        form = StudentForm()

    return render(request, 'students/student.html', {'form': form})


def student_result(request):
    student = request.session.get('student')

    if not student:
        return redirect('student_register')

    return render(request, 'students/student_result.html', {'student': student})