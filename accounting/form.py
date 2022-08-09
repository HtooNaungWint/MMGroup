from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    
    class Meta:
        fields = ('username', 'password1','password2','email') 
        model = get_user_model()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'Display name'
        self.fields['password1'].label = 'Password'
        self.fields['password2'].label = 'Password Confirmation'
        self.fields['email'].label = 'Email Address'