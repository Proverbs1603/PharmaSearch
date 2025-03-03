from .models import *
from django.shortcuts import render

# Create your views here.
def index(request):
    drug_list = Drug.objects.order_by('-ptnt_reg_dt')
    context = {'first_question': drug_list[0]}
    return render(request, 'drugs/index.html', context)