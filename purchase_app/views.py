from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .forms import PurchaseModel_Form
from car_app.models import Car_Model


@login_required
def car_purchase(request, car_id):
    selected_car = get_object_or_404(Car_Model, id=car_id)
    user = request.user

    if selected_car.quantity == 0:
        messages.error(request, 'Requested quantity is not available.')
        return redirect('home')
    else:
        if request.method == 'POST':
            form = PurchaseModel_Form(request.POST)
            if form.is_valid():
                # Get the purchase quantity from the form
                selected_quantity = form.cleaned_data['quantity']
                if selected_quantity <= 0:
                    messages.error(request, 'Invalid quantity selected.')
                else:
                    # Check if enough cars are available for purchase
                    if selected_car.quantity >= selected_quantity:
                        purchase = form.save(commit=False)
                        purchase.user = user
                        purchase.car = selected_car
                        purchase.total_price = selected_car.price * selected_quantity

                        # Subtract purchased quantity from car's quantity
                        selected_car.quantity -= selected_quantity
                        # Save the updated car quantity to the database
                        selected_car.save()

                        purchase.save()
                        messages.success(request, 'Your purchase was successfully.')
                        return redirect('profile')
                    else:
                        messages.error(request, 'Requested quantity is not available.')
                        return redirect('car_purchase')
        else:
            form = PurchaseModel_Form(initial={'user': user, 'car': selected_car})
        context = {
            'selected_car': selected_car,
            'form': form,
        }
        return render(request, 'purchase_app/car_purchase.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
