from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=5, required=True,
                            error_messages={
                                'required': '文章标题是必填项',
                                'min_length': '文章标题不能少于5个字'
                            })
    keywords = forms.CharField(min_length=2, required=True,
                              error_messages={
                                  'required': '关键词是必填项',
                                  'min_length': '关键词不能少于2个字'
                              })
    tags = forms.CharField(min_length=2, required=True,
                              error_messages={
                                  'required': '标签是必填项',
                                  'min_length': '标签不能少于2个字'
                              })
    describe= forms.CharField(min_length=10, required=True,
                           error_messages={
                               'required': '文章描述是必填项',
                               'min_length': '文章描述不能少于10个字'
                           })
    content = forms.CharField(required=True,
                              error_messages={
                                  'required': '文章内容是必填项',
                              })
    # icon = forms.ImageField(required=True, error_messages={
    #     'required': '首图必填'
    # })


class RegisterForm(forms.Form):
    truename = forms.CharField(max_length=10, required=True,
                               error_messages={
                                   'required': '姓名是必填项',
                                   'max_length': '姓名不能超过10个字'
                               })
    username = forms.CharField(max_length=20, required=True,
                               error_messages={
                                   'required': '用户名是必填项',
                                   'max_length': '用户名不能超过20个字'
                               })
    tel = forms.CharField(max_length=11, min_length=11, required=False,
                               error_messages={
                                   'max_length': '电话只能为11位',
                                    'min_length': '电话只能为11位',
                               })
    password = forms.CharField(min_length=6, required=True,
                               error_messages={
                                   'required': '密码是必填项',
                                   'max_length': '密码至少6位'
                               })
    new_password = forms.CharField(min_length=6, required=True,
                               error_messages={
                                   'required': '密码是必填项',
                                   'min_length': '密码至少6位'
                               })





