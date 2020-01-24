from django.views.generic import ListView

from app.models import Mercado


class MercadoList(ListView):
    model = Mercado
    template_name = 'app/mercado_list.html'
