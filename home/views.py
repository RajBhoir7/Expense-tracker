from django.shortcuts import render,redirect
from .models import Expense
# Create your views here.
from django.db.models import Sum
import datetime
def home(request):
    expense = Expense.objects.all()
    total_expense = expense.aggregate(Sum('amount'))
    #for i in (expense):
    #   total_expense = total_expense + i.amount
    #print(total_expense['amount__sum'])



    # Logic To Calculate 365 days expenses
    last_year = datetime.date.today() - datetime.timedelta(days=365) #Current Date-days Ago
    data = Expense.objects.filter(date__gt=last_year)  #Date greter Than last year
    yearly_sum = data.aggregate(Sum('amount'))

    # Last 30 Days
    last_month = datetime.date.today() - datetime.timedelta(days=30)
    data = Expense.objects.filter(date__gt=last_month)
    monthly_sum = data.aggregate(Sum('amount'))
    
    # last 7 Days
    last_week = datetime.date.today() - datetime.timedelta(days=7)
    data = Expense.objects.filter(date__gt=last_week)
    weekly_sum = data.aggregate(Sum('amount'))

    # Calculating Expense Accordint to date
    daily_expense = Expense.objects.filter().values('date').order_by('date').annotate(sum=Sum('amount'))
   

    #for i in daily_expense:
     #   print(i['date'],i['sum'])
        
    return render(request,'home\index.html',{'Expenses':expense,
                                             'Total_expense':total_expense['amount__sum'],
                                             'yearly_sum' : yearly_sum['amount__sum'],
                                             'monthly_sum':monthly_sum['amount__sum'],
                                             'last_week':weekly_sum['amount__sum'],
                                             'daily_expense':daily_expense 
                                             })


def add_expense(request):
    if request.method == 'POST':
        ExpenseName = request.POST.get('Expense Name')
        Amount = request.POST.get('Amount')
        Category = request.POST.get('Category')

        form_obj = Expense.objects.create(
            name = ExpenseName,
            amount = Amount,
            category = Category
        )
        form_obj.save()
        return redirect('/')
    return render(request,'home/addexpense.html')


def update_Expense(request,id):
    data = Expense.objects.get(id=id)
    if request.method == 'POST':
        ExpenseName = request.POST.get('Expense Name')
        Amount = request.POST.get('Amount')
        Category = request.POST.get('Category')

        data.name = ExpenseName
        data.amount = Amount
        data.category = Category
        data.save()
        return redirect("home")
    
    #addexpense.html is reused for update expense
    return render(request,'home/addexpense.html',{'data':data})


def delete_expense(request,id):
    Expense.objects.get(id=id).delete()
    
    return redirect('home')