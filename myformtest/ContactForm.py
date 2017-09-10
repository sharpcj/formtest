# encoding = utf-8
from django import forms

class ContactForm(forms.Form):
    CITY = [
        ['SZ','深圳'],
        ['BJ','北京'],
        ['SH','上海'],
    ]
    user_name = forms.CharField(label='您的姓名',max_length=50,initial='张三')
    user_city = forms.ChoiceField(label='居住城市',choices=CITY)
    user_message = forms.CharField(label='您的意见',widget=forms.Textarea)