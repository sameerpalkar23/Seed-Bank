from cgitb import text
import imp
import json
from itertools import product
from math import prod
from multiprocessing import context
from pyexpat import model
from turtle import pd
from unittest import result
from django import views
from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product,Cart, OrderPlaced, cropprediction
from .forms import CustomerRegistrationForm, CustomerProfileForm, CropPredictionForm
from django.contrib import messages
import joblib
import pandas as pd
import os
import numpy as np
import pickle

from joblib import load
from app.constants import *
import pandas as pd   
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import datasets, linear_model, metrics








# Create your views here.

class ProductView(View):
 def get(self, request):
     cpseeds = Product.objects.filter(catagory='CP')
     eagleseeds = Product.objects.filter(catagory='ES')
     goodwillhealth = Product.objects.filter(catagory='GH')
     bayernseeds = Product.objects.filter(catagory='BS')
     naturals = Product.objects.filter(catagory='N')
     maharashtra = Product.objects.filter(catagory='MH')
     kerala = Product.objects.filter(catagory='kL')
     return render(request, 'app/home.html', {'cpseeds':cpseeds, 'eagleseeds':eagleseeds, 'goodwillhealth':goodwillhealth, 'bayernseeds':bayernseeds, 'naturals':naturals, 'maharashtra':maharashtra, 'kerala':kerala})


class ProductDetailView(View):
   def get(self, request, pk):
     product = Product.objects.get(pk=pk)
     return render(request, 'app/productdetail.html', {'product':product})   

def add_to_cart(request):
 user=request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id=product_id)
 Cart(user=user, product=product).save()
 return redirect('/cart')

def show_cart(request):
   if request.user.is_authenticated:
      user = request.user
      cart = Cart.objects.filter(user=user)
      print(cart)
      amount = 0.0
      total_amount = 0.0
      cart_product = [p for p in Cart.objects.all() if p.user ==user]

      if cart_product:
         for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
            totalamount = amount
      return render(request, 'app/addtocart.html', {'carts':cart, 'totalamount':totalamount, 'amount':amount})
   else:
      return render(request, 'app/emptycart.html')




def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
 add = Customer.objects.filter(user=request.user)  
 return render(request, 'app/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 op = OrderPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html', {'order_placed':op})


def cpseeds(request):
 return render(request, 'app/cp seeds.html')

def eagleseeds(request):
 return render(request, 'app/eagle seeds.html') 

def goodwillhealth(request):
 return render(request, 'app/goodwill health.html')

def bayernseeds(request):
 return render(request, 'app/bayern seeds.html') 

def naturals(request):
 return render(request, 'app/naturals.html')  

def maharashtra(request):
   return render(request, 'app/maharashtra.html') 


def kerala(request):
   return render(request, 'app/kerala.html')   

def uttarpradesh(request):
   return render(request, 'app/uttarpradesh.html')      


class CustomerRegistrationView(View):
  def get(self, request): 
     form = CustomerRegistrationForm()
     return render(request, 'app/customerregistration.html', {'form':form}) 

  def post(self, request):
          form = CustomerRegistrationForm(request.POST)
          if form.is_valid():
           messages.success(request, 'Registered Successfully')    
           form.save()
          return render(request, 'app/customerregistration.html',{'form':form})   

def checkout(request):
  user = request.user
  add = Customer.objects.filter(user=user) 
  cart_items = Cart.objects.filter(user=user)
  amount = 0.0
  shipping_amount = 70.0
  total_amount = 0.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  if cart_product:
      for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
      totalamount = amount + shipping_amount      
      return render(request, 'app/checkout.html',{'add':add, 'totalamount':totalamount, 'cart_items':cart_items})

def payment_done(request):
   user = request.user
   custid = request.GET.get('custid') 
   customer = Customer.objects.get(id=custid)
   cart = Cart.objects.filter(user=user)
   for c in cart:
      OrderPlaced(user=user, customer=customer, product=c.product, quantity=c.quantity).save()
      c.delete()
      return redirect("orders")

class ProfileView(View):
   def get(self, request):
      form = CustomerProfileForm()
      return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})

   def post(self, request):
      form = CustomerProfileForm(request.POST)
      if form.is_valid():
         usr = request.user
         name = form.cleaned_data['name']
         locality = form.cleaned_data['locality']   
         city = form.cleaned_data['city']      
         state = form.cleaned_data['state']   
         zipcode = form.cleaned_data['zipcode']  
         reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
         reg.save() 
         messages.success(request, 'Congratulations!! Profile Updated Successfully')
      return render(request, 'app/profile.html', {'form':form, 'active':'btn-primary'})


def index(request):
    return render(request, 'app/index.html')
def analyze(request):
    crop = pd.read_csv("dataset/Crop_recommendation.csv")
    from sklearn.model_selection import train_test_split

    crop.drop_duplicates()

   
    attr=["N","P","K","temperature","humidity","rainfall","label"]
    if crop.isna().any().sum() !=0:
        for i in range(len(attr)):
            crop[attr[i]].fillna(0.0, inplace = True)

    
    crop.columns = crop.columns.str.replace(' ', '') 

   
    features = crop[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]

    
    target = crop['label']

    x_train, x_test, y_train, y_test = train_test_split(features,target,test_size = 0.2,random_state =2)
    
    
    
    RF = RandomForestClassifier(n_estimators=20, random_state=0)

   
    RF.fit(x_train,y_train)
   
    N = request.POST.get('nitrogen', 'default')
    P = request.POST.get('phosphorous', 'default')
    K = request.POST.get('potassium', 'default')
    temp = request.POST.get('temperature', 'default')
    humidity = request.POST.get('humidity', 'default')
    ph =request.POST.get('ph', 'default')
    rainfall = request.POST.get('rainfall', 'default')


   # LinearRegression Implementation




    userInput = [N, P, K, temp, humidity, ph, rainfall]

    
   
    result1 = RF.predict([userInput])[0]
   
   



   
    params = {'purpose':'Predicted Crop: ', 'analyzed_text': result1.upper()}
    return render(request, 'app/analyze.html', params)    


    
             





