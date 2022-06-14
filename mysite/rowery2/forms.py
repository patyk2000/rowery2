from django import forms

#fomularz

VOTE = [('1', 'super'),('2', 'Dobry'),('3','Średnio'),('4','Słabo'),('5','Dramat')]

class Form(forms.Form):
 vote = forms.CharField(widget=forms.RadioSelect(choices=VOTE))