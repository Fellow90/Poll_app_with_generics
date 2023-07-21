
from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice


class QuestionAdmin(admin.ModelAdmin):
    # fields = ["pub_date","question_text"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date Information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin )
