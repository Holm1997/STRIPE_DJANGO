import stripe
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import JsonResponse
from .models import *


# Представление,отображающее страницу со всеми товарами
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})

# Stripe test secret API key.
stripe.api_key = 'sk_test_51McOLgLrJ9oUl0viQwHg3i5Ivi2U9BCfVFkR0xp2JbgROB8K7mXKf0z8tFo2d35lnh3XDkYkGy3ABMasWAXYts5h00zpHUpSol'


# Представление, отображающее выбранный товар с главной страницы
class ShowItemView(TemplateView):
    template_name = 'show.html'

    def get_context_data(self, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        context = super(ShowItemView, self).get_context_data(**kwargs)
        context.update({
            'item': item
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]
        item = Item.objects.get(id=item_id)
        if not item.description:
            item.description = item.name
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount_decimal': item.price,
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({
            'id': checkout_session.id,
        })


class SuccessView(TemplateView):
    template_name='success.html'


class CancelView(TemplateView):
    template_name='cancel.html'


