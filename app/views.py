from django.shortcuts import render
from django.http import Http404


from app.models import Car
# Create your views here.

def cars_list_view(request):
	# получите список авто

	cars = Car.objects.all()

	context = {'cars': cars}
	#print(context) # {'cars': <QuerySet [<Car: Mercedes-Benz S-classe 2023>, <Car: Lada Vesta Cross 2022>, <Car: Toyota Camry 2019>]>}
	template_name = 'main/list.html'
	return render(request, template_name, context)  # передайте необходимый контекст

def car_details_view(request, car_id):
	# получите авто, если же его нет, выбросьте ошибку 404
	try:
		car = Car.objects.get(pk=car_id)
		context = {'car': car}
		template_name = 'main/details.html'
		return render(request, template_name, context)  # передайте необходимый контекст
	except Car.DoesNotExist:
		raise Http404('Car not found')


def sales_by_car(request, car_id):
	try:
		# получите авто и его продажи
		car = Car.objects.get(pk=car_id)
		sales = car.sale_set.all()
		context = {'car': car, 'sales': sales}
		template_name = 'main/sales.html'
		return render(request, template_name, context)  # передайте необходимый контекст
	except Car.DoesNotExist:
		raise Http404('Car not found')