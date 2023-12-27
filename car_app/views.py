from django.shortcuts import render
from django.views.generic import DetailView
from .models import Car_Model
from .forms import CommentsModel_Form
from django.contrib.auth.decorators import login_required

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# @login_required
# def car_profile(request):
#     cars = Car_Model.objects.all()
#
#     context = {
#         'manufacturer': cars.first().manufacturer,
#         'model': cars.first().model,
#         'capacity': cars.first().capacity,
#         'shift': cars.first().shift,
#         'fuel': cars.first().fuel,
#         'top_speed': cars.first().top_speed,
#         'price': cars.first().price,
#         'quantity': cars.first().quantity,
#         'image': cars.first().image,
#     }
#
#     return render(request, 'car_app/car_profile.html', context)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# @method_decorator(login_required, name='dispatch')
class Car_Profile(DetailView):
    model = Car_Model
    pk_url_kwarg = 'id'
    template_name = 'car_app/car_profile.html'

    def post(self, request, *args, **kwargs):
        form = CommentsModel_Form(data=self.request.POST)
        car = self.get_object()
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()

        form = CommentsModel_Form()
        context['comments'] = comments
        context['form'] = form
        return context

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
