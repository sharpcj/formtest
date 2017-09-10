# encoding = utf-8
from django import forms

from myformtest import models

from captcha.fields import CaptchaField


class StudentForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Student
        fields = ['name','gender']

    # 下面是为了设置默认值为中文，可以不要
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = '学生姓名'
        self.fields['gender'].label = '学生性别'
        self.fields['captcha'].label = '确定您不是机器人'

