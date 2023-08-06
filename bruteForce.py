from django.views.generic import TemplateView

class MyImageView(TemplateView):
    template_name = 'my_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_url'] = 'https://cdn.discordapp.com/attachments/753316082680594456/1133243828766249131/impact.jpg'
        return context
    
<img src="{{ image_url }}" alt="Imagem Substituída">
