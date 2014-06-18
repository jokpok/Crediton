from django.shortcuts import render, render_to_response, RequestContext, Http404, HttpResponse, HttpResponseRedirect

from .models import Credit
from .forms import CreditForm

from decimal import *

def unsecured_credits(request):
    context = RequestContext(request)
    
    if request.method == "POST":
        total = int(request.POST['total'])
        term = int(request.POST['term'])
        currency = request.POST['currency']
        
        credits = Credit.objects.filter(max_sum__gte=total, term__gte=term, currency=currency)
        max_monthly = Decimal('-Infinity')
        max_over = Decimal('-Infinity')
        for credit in credits:
            sm_p, over = overpayment(credit.percent_years, term, total)
            credit.monthly, credit.overpayment = sm_p, over
            if credit.monthly > max_monthly:
                max_monthly = credit.monthly
            if credit.overpayment > max_over:
                max_over = credit.overpayment 
        for credit in credits:
            credit.monthly_percent = visual_percent(max_monthly, credit.monthly, 25)
            credit.overpayment_percent = visual_percent(max_over, credit.overpayment, 90)
    
    return render_to_response('loans/unsecured_credits.html', locals(), context)


def overpayment(p, n, c):
    a = 1 + p/1200
    k = ( (a**n)*(a - 1) )/( (a**n) - 1 )
    s_m = k*c
    over = s_m*n - c
    return s_m.quantize(Decimal('1.'), rounding=ROUND_UP), over.quantize(Decimal('1.'), rounding=ROUND_UP)

def visual_percent(max_value, current_value, init_percent):
    return int(init_percent*(current_value/max_value))
    
    
def test(request):
    context = RequestContext(request)
    
    return render_to_response('loans/test.html', locals(), context)