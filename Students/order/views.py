from django.shortcuts import render

# Create your views here.

from .forms import OrderForm
from .models import Order


def order_view(request):
    prices = {
        'laptop': 5000000,
        'phone': 3000000,
        'headphones': 200000,
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            product_price = prices[data['product']]
            delivery_price = 30000 if data['delivery'] == 'courier' else 0

            total = product_price * data['quantity'] + delivery_price

            order = Order.objects.create(
                name=data['name'],
                phone=data['phone'],
                product=data['product'],
                quantity=data['quantity'],
                delivery=data['delivery'],
                address=data['address'],
                total_price=total
            )

            return render(request, 'order_result.html', {
                'order': order
            })

    else:
        form = OrderForm()

    return render(request, 'order_result.html', {
        'order': Order.objects.get(id=Order.objects.latest('id').id)
    })
