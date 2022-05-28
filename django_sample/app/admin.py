from django.contrib import admin

# Register your models here.

from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')

    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
