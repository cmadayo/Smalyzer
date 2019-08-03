from django.shortcuts import render
from django.views.generic import TemplateView
from .models import UploadFile
from .forms import SingleUploadModelForm


class AnalyzeView(TemplateView):
    template_name = "analyze.html"
    model = UploadFile
    form = SingleUploadModelForm

    def get(self, request, *args, **kwargs):
        context = super(AnalyzeView, self).get_context_data(**kwargs)
        context['form'] = self.form
        return render(self.request, self.template_name, context)
