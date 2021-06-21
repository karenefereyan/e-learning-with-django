from account.forms import FormSettings
from student.models import *
from staff.models import Staff
from django import forms


class AddCourseForm(FormSettings):
    class Meta:
        model = Course
        fields = "__all__"


class AddDepartmentForm(FormSettings):
    class Meta:
        model = Department
        fields = "__all__"


class AddSessionForm(FormSettings):
    class Meta:
        model = Session
        fields = "__all__"


class AddStudentForm(FormSettings):
    class Meta:
        model = Student
        exclude = ['admin']
        # https://stackoverflow.com/questions/22846048/django-form-as-p-datefield-not-showing-input-type-as-date
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }


class AddStaffForm(FormSettings):
    class Meta:
        model = Staff
        exclude = ['admin']
