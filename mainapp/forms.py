from django import forms
from .models import Course, CourseCategory


class CourseForm(forms.ModelForm):
    slug = forms.SlugField(
        label='Короткий слаг на EN',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите короткое название на английском',
                'class': 'form-control'
            }
        )
    )
    name = forms.CharField(
        label='Название курса',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите название курса',
                'class': 'form-control'
            }
        )
    )

    description = forms.CharField(
        label='Описание курса',
        required=True,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Введите описание курса',
                'class': 'form-control'
            }
        )
    )

    price = forms.DecimalField(
        label='Стоимость',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Введите стоимость',
                'class': 'form-control'

            }
        )
    )

    categories = forms.ModelMultipleChoiceField(
        label='Направления',
        required=True,
        queryset=CourseCategory.objects.all(),
        widget=forms.CheckboxSelectMultiple(
            attrs={
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Course
        fields = "__all__"


class ContactForm(forms.Form):
    email = forms.EmailField(
        label='Ваша почта',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'email@email.com',
                'class': 'form-control'
            }
        ))
    message = forms.CharField(
        label='Сообщение',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст сообщения'
            }
        )
    )
