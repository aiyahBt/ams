from django import forms
from .models import ApplicationFormModel, ApplicationRound


class ApplicationForm(forms.ModelForm):
    """Form for the image model"""

    # widget=forms.Select(attrs={'title':'คำนำหน้าชื่อ'})
    # prefix = forms.TypedChoiceField(required=True, choices=prefix_choices)
    class Meta:
        prefix_choices = [
            ('นาย', 'นาย'),
            ('นาง', 'นาง'),
            ('นางสาว', 'นางสาว'),
            ('ไม่ระบุ', 'ไม่ระบุ')
        ]

        model = ApplicationFormModel
        # fields = ('prefix', 'firstname', 'doc')

        exclude = ('application_round', 'user')
        # attrs = {'title', 'คำนำหน้าชื่อ'}

        birth_date_input = forms.DateInput(attrs={'required': True})
        birth_date_input.input_type = 'date'

        labels = {
            'prefix' : 'คำนำหน้าชื่อ',
            'firstname' : 'ชื่อ',
            'middlename': 'ชื่อกลาง',
            'lastname': 'ชื่อสกุล',
            'birthdate': 'วันเดือนปีเกิด',
            'email': 'อีเมล',
            'phonenumber': 'หมายเลขโทรศัพท์',
            'gpax': 'เกรดเฉลี่ยสะสม',
            'student_image': 'ภาพถ่ายในชุดนักเรียน',
            'transcript' : 'ใบแสดงผลการศึกษา',
            'optional_work' : 'ผลงานอื่น ๆ'
        }
        widgets = {
            'prefix' : forms.Select(choices=prefix_choices),
            'firstname': forms.TextInput(attrs={'title': 'ชื่อ', 'required' : True, 'max_length' : 40}),
            'middlename': forms.TextInput(attrs={'title': 'ชื่อกลาง', 'required' : False, 'max_length' : 40}),
            'lastname': forms.TextInput(attrs={'title': 'ชื่อสกุล', 'required' : False, 'max_length' : 40}),
            'birthdate' : birth_date_input,
            'email'  : forms.EmailInput(attrs={'title': 'อีเมล', 'required': True}),
            'phonenumber' : forms.TextInput(attrs={'title': 'หมายเลขโทรศัพท์', 'required' : True, 'min_length':10, 'max_length' : 10}),
            'gpax' : forms.NumberInput(attrs={'title': 'เกรดเฉลี่ยสะสม', 'required' : False, 'min': 0.0001, 'max': 4})

            # 'visible': forms.CheckboxInput(),
            # 'active': forms.CheckboxInput(),

        }
    # prefix = models.CharField(max_length=20, null=False)
    # firstname = models.CharField(max_length=40, null=False)
    # middlename = models.CharField(max_length=40, null=True)
    # lastname = models.CharField(max_length=40, null=False)
    # birthdate = models.DateField(null=False)
    # email = models.EmailField(null=True)
    # phonenumber = models.IntegerField(null=False)
    # gpax = models.FloatField(null=False)
    #
    # student_image = models.ImageField(null=False)
    # transcript = models.FileField(null=True)
    # optional_work = models.FileField(null=True)

class ApplicationRoundForm(forms.ModelForm):

    class Meta:
        model = ApplicationRound
        fields = ('title', 'start_date', 'end_date', 'visible', 'active')

        start_date_input = forms.DateInput(attrs={'title' : 'วันที่เริ่มรับสมัคร', 'required' : True})
        start_date_input.input_type = 'date'

        end_date_input = forms.DateInput(attrs={'title': 'วันสิ้นสุดการรับสมัคร', 'required': True})
        end_date_input.input_type = 'date'

        widgets = {
            'title' : forms.TextInput(attrs={'title' : 'ชื่อโครงการ'}),
            'start_date': start_date_input,
            'end_date' : end_date_input,
            'visible' : forms.CheckboxInput(),
            'active' : forms.CheckboxInput(),

        }

