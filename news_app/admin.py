from django import forms
from django.contrib import admin
from .models import News, NewsImage

class NewsImageForm(forms.ModelForm):
    delete = forms.BooleanField(required=False, initial=False, label='Удалить')

    class Meta:
        model = NewsImage
        fields = ['image', 'delete']

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    verbose_name = "Изображение"  
    verbose_name_plural = "Изображения"
    
    
    def save_new_image(self, form, commit=True):
        if form.cleaned_data.get('delete'):
            form.instance.delete()
        else:
            return super().save_new_image(form, commit=commit)
        
class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['created_at', 'title', 'short_description', 'content', 'video']  
      

    def __init__(self, *args, **kwargs):
        super(NewsAdminForm, self).__init__(*args, **kwargs)
        self.fields['created_at'].help_text = 'Введите дату и время создания.'
        self.fields['title'].help_text = 'Введите заголовок новости.'
        self.fields['short_description'].help_text = 'Введите краткое описание новости.'
        self.fields['content'].help_text = 'Введите полный текст новости.'
        self.fields['video'].help_text = 'Вставьте ссылку на видео.'
    

    
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ['custom_title'] 
    inlines = [NewsImageInline] 
    
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        return ['created_at', 'title', 'short_description', 'content', 'video']
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

    def custom_title(self, obj):
        return obj.title
    custom_title.short_description = 'Новость'
