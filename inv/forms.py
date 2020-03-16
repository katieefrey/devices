from django import forms
#from uploads.core.models import Document
from .models import Component, Item, Cleaning, Checking

from django.forms.models import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class BarcodeForm(forms.Form):
    inputBarcode = forms.CharField(label='Check Item & Proceedures', max_length=100)


class ModifyDevice(ModelForm):
    
    class Meta:
        model = Item
        fields = ("components","cleaning","checking","location")
             
    def __init__(self, *args, **kwargs):
        
        super(ModifyDevice, self).__init__(*args, **kwargs)
        
        self.fields["components"].widget = CheckboxSelectMultiple()
        self.fields["components"].queryset = Component.objects.all()
        self.fields["cleaning"].widget = CheckboxSelectMultiple()
        self.fields["cleaning"].queryset = Cleaning.objects.all()
        self.fields["checking"].widget = CheckboxSelectMultiple()
        self.fields["checking"].queryset = Checking.objects.all()
    





# class ModifyDevice(forms.Form):
#     class Meta:
#         model = Item
#     components = forms.ModelMultipleChoiceField(queryset=Component.objects.all())



# class DocumentForm(forms.ModelForm):
#     class Meta:
#         model = Document
#         fields = ('description', 'document', )


# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()


# class UploadImageForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     img = forms.ImageField()