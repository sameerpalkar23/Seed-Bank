from tokenize import Name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


STATE_CHOICES = (
    ('Andhra Pradesh','Andhra Pradesh'), 	
 	('Arunachal Pradesh','Arunachal Pradesh'), 	
 	('Assam','Assam'), 	
 	('Bihar','Bihar'),	
 	('Chhattisgarh','Chhattisgarh'), 	
 	('Goa','Goa'),
 	('Gujarat','Gujarat'), 	
 	('Haryana','Haryana'), 	
 	('Himachal Pradesh','Himachal Pradesh'), 
 	('Jammu Kashmir','Jammu Kashmir'), 	
 	('Jharkhand','Jharkhand'), 	
 	('Karnataka', 'Karnataka'), 
 	('Kerala','Kerala'), 	
 	('Madhya Pradesh','Madhya Pradesh'), 	
 	('Maharashtra','Maharashtra'), 	
	('Manipur','Manipur'), 	
	('Meghalaya','Meghalaya'), 	
 	('Mizoram','Mizoram'), 	
 	('Nagaland','Nagaland'), 	
 	('Odisha','Odisha'), 	
 	('Punjab','Punjab'), 	
 	('Rajasthan','Rajasthan'), 	
 	('Sikkim','Sikkim'), 	
 	('Tamil Nadu','Tamil Nadu'), 
 	('Telangana','Telangana'), 	
 	('Tripura','Tripura'), 	
 	('Uttar Pradesh','Uttar Pradesh'), 	
 	('Uttarakhand','Uttarakhand'), 	
 	('West Bengal','West Bengal')
)

class Customer(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 state = models.CharField(choices=STATE_CHOICES, max_length=150)
 city = models.CharField( max_length=50)
 locality = models.CharField(max_length=200)
 zipcode = models.IntegerField()

 def _str_(self):
  return str(self.id)

CATAGORY_CHOICES =(
    ('CP','C.P SEEDS'),
    ('ES','EAGLE SEEDES'),
    ('GH','GOODWILL HEALTH'),
    ('BS','BAYERN SEEDS'),
    ('N','NATURALS'),
    ('MH','Maharashta'),
    ('KL','Kerala'),
    ('UP','Utter Pradesh'),
    ('BR','Bihar'),
    ('RS','Rajasthan'),

) 
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 catagory = models.CharField(choices=CATAGORY_CHOICES,max_length=3)
 product_image = models.ImageField(upload_to='productimg')

 def __str__(self):
    return str(self.id)

class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveBigIntegerField(default=1)

 def _str_(self):
    return str(self.id)  

 @property
 def total_cost(self):
	 return self.quantity * self.product.discounted_price	

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packes'),
    ('On THe Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
) 

class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveBigIntegerField(default=1)
 order_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

 @property
 def total_cost(self):
	 return self.quantity * self.product.discounted_price	




CHO_CHOICES=(
	('Maharashtra', 'Maharashtra')
)
DISTRICTNAME_CHOICES=(
	('AHMEDNAGAR','AHMEDNAGAR'),
	('AKOLA','AKOLA'),
	('AMRAVATI','AMRAVATI'),
	('AURANGABAD','AURANGABAD'),
	('BEED','BEED'),
	('BHANDARA','BHANDARA'),
	('BULDHANA','BULDHANA'),
	('CHANDRAPUR','CHANDRAPUR'),
	('DHULE','DHULE'),
	('GADCHIROLI','GADCHIROLI'),
	('GONDIA','GONDIA'),
	('HINGOLI','HINGOLI'),
	('JALGAON','JALGAON'),
	('JALNA','JALNA'),
	('KOLHAPUR','KOLHAPUR'),
	('LATUR','LATUR'),
	('NAGPUR','NAGPUR'),
	('NANDED','NANDED'),
	('NANDURBAR','NANDURBAR'),
	('NASHIK','NASHIK'),
	('PARBHANI','PARBHANI'),
	('PUNE','PUNE'),
	('RAIGAD','RAIGAD'),
	('RATNAGIRI','RATNAGIRI'),
	('SANGLI','SANGLI'),
	('SATARA','SATARA'),
	('SINDHUDURG','SINDHUDURG'),
	('SOLAPUR','SOLAPUR'),
	('THANE','THANE'),
	('WASHIM','WASHIM'),
	('YAVATMAL','YAVATMAL')
 )
SEASON_CHOICES=(
	('Autumn','Autumn'),
	('Kharif','Kharif'),
	('Rabi','Rabi'),
	('Summer','Summer'),
	('Whole Year','Whole Year'),

 )
SOILTYPE_CHOICES=(
	('loamy','loamy'),
	('sandy','sandy'),
	('clay','clay'),
	('chalky','chalky'),
	('peaty','peaty'),
	('silty','silty'),
	
)
 

class cropprediction(models.Model):
		state = models.CharField(max_length=15)
		district = models.CharField(choices=DISTRICTNAME_CHOICES,max_length=15)
		year = models.IntegerField()
		season = models.CharField(choices=SEASON_CHOICES,max_length=15)
		crop = models.CharField(max_length=100)
		area = models.CharField(choices=DISTRICTNAME_CHOICES,max_length=15)
		temperature = models.FloatField()
		windspeed = models.FloatField()
		pressure = models.FloatField()
		humidity = models.FloatField()
		soiltype = models.CharField(choices=SOILTYPE_CHOICES,max_length=15)
		n = models.FloatField()
		p = models.FloatField()
		k = models.FloatField()
		production = models.IntegerField()
		

def _str_(self):
  return str(self.id)	


    
    
    

