# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from main import models


def home(request):
    return render(request, 'index.html', {
    })


def transactions(request):
    transactions = models.Transaction.objects.all().order_by('-date')
    return render(request, 'transactions.html', {
        'transactions': transactions,
    })


def transaction_view(request, transaction_id):
    transaction = get_object_or_404(models.Transaction, pk=transaction_id)
    transactions = models.Transaction.objects.filter(description__icontains=transaction.description).order_by('-date')
    return render(request, 'transactions.html', {
        'transactions': transactions,
    })
