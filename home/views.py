from django.shortcuts import render,redirect
from .models import Expense
# Create your views here.
from django.db.models import Sum

def home(request):
    expense = Expense.objects.all()
    total_expense = expense.aggregate(Sum('amount'))
    #for i in (expense):
    #   total_expense = total_expense + i.amount
    #print(total_expense['amount__sum'])

    
    return render(request,'home\index.html',{'Expenses':expense,
                                             'Total_expense':total_expense['amount__sum']})


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