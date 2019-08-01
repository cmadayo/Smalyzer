from django.shortcuts import render
from django.views.generic import TemplateView


class AnalyzeView(TemplateView):
    template_name = "analyze.html"

    def get(self, request, *args, **kwargs):
        context = super(AnalyzeView, self).get_context_data(**kwargs)
        return render(self.request, self.template_name, context)
