from django import forms
from lolteams.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'winrate']
        labels = {
            'name' : '멤버'
        }

class MemberModify(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name']
        labels = {
            'name' : '멤버'
        }