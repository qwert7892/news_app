from django import forms


class NewsForm(forms.Form):
    title = forms.CharField(
        min_length=0,
        max_length=100,
        label="Заголовок",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))

    summary = forms.CharField(
        max_length=200,
        label="Краткое описание",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }))

    content = forms.CharField(label="Текст новости", widget=forms.Textarea(attrs={
        'class': 'form-control',
    }))

    photo = forms.ImageField(
        label="Обложка",
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        })
    )
