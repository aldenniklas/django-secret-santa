from django import forms

class add_santa(forms.Form):
    santa_name = forms.CharField(required=True, label='Namn')
    santa_email = forms.EmailField(required=True, label='Email')
    santa_wishlist = forms.CharField(
        required=False,
        label='Onskelista',
        widget=forms.Textarea
        )
    santa_restrictions = forms.CharField(required=False,label='Restriktioner')