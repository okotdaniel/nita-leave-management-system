from django import forms 
from django.forms import  ClearableFileInput
from adminDashboard.models import *
from employeeDashboard.models import *



class TimeInput(forms.TimeInput):
    input_type = "time"


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%dT%H:%M"
        super().__init__(**kwargs)


class LeaveForm(forms.ModelForm):

    OutstandingLeaveDays = forms.IntegerField(widget=forms.TextInput(
        attrs={'readonly': 'readonly', 'placeholder': '26'})) #26 is a random number chosen for placeholder feature to work

    NumberOfDaystaken = forms.IntegerField(widget=forms.TextInput(
        attrs={'readonly': 'readonly', 'placeholder': '0'})) 
        
    name = forms.CharField(widget=forms.TextInput(
        attrs={'readonly': 'readonly'}))
    
    file_upload = forms.CharField(widget=ClearableFileInput(attrs={'multiple': True}), label="Upload your support files",
                                 help_text="Attach any files here (10mb max per file)", required=False)

    class Meta:
        model = Leaves
        
        fields = ['name', 'StartDate',
                  'EndDate', 'OutstandingLeaveDays', 'NumberOfDaystaken',
                  'LeaveType', 'empDirector',
                  'empDirectorate', 'empDepartment', 'file_upload']

        # added labels for each field above except name and outstandingLeaveDays since they're re-defined on line 27 and 30
        # crispy_forms library expects a 'labels' dictionary mapping each field to its preferred label
        labels = {
            'StartDate': 'Start Date',
            'EndDate': 'End Date',
            'NumberOfDaystaken': 'Days Taken',
            'LeaveType': 'Type of Leave',
            'empDirector': 'Director',
            'empDirectorate': 'Directorate',
            'empDepartment': 'Department',
            'file_upload': 'Upload any support files'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["StartDate"].widget = DateInput()
        self.fields["EndDate"].widget = DateInput()

        # added two labels here because they wont work in the labels dict
        self.fields["name"].label = "Applicant Name"
        self.fields["OutstandingLeaveDays"].label = "Leave Days"
        self.fields["NumberOfDaystaken"].label = "Days Taken"

