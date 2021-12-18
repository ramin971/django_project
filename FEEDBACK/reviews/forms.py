from django import forms
from .models import Review
#
# class ReviewForm(forms.Form):
#     user_name=forms.CharField(label='Your name',max_length=10,error_messages={
#         'max_length':'oh it is very long'
#     })
#     review_text=forms.CharField(label='Your Feedback',widget=forms.Textarea,max_length=200)
#     rating=forms.IntegerField(label='Your Rating',min_value=1,max_value=5)
#

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        labels={
            "user_name":"Your Name",
            "review_text":"Your Feedback",
            "rating":"Your rating"
        }
        error_messages={
            "user_name":{
                "max_length":"that's  very long"
            },
            "review_text":{
                "max_length":"that's  very long"
            },
            "rating":{
                "min_value":"must be gt 0",
                "max_value":"must be lt 6"
            }
        }