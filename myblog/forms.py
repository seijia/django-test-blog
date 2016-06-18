from django import forms
from myblog.models import Blog
from pagedown.widgets import AdminPagedownWidget
#coding = 'utf-8'

class Commentform(forms.Form):

    name = forms.CharField(max_length=16,label='名字',error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼太长',
    })
    email = forms.EmailField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确'
    })

    content = forms.CharField(widget=forms.Textarea,label='评论内容', error_messages={
        'required': '请填写您的评论内容',
        'max_length': '评论内容太长'
    })


  #  def clean_content(self):
   #     content = self.clean_data['content']
   #     num_world = len(content.split())
   #     if num_world<4:
   #         raise forms.ValidationError('太短了，多说一下吧')
   #     return  content

class BlogForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Blog
        fields = '__all__'