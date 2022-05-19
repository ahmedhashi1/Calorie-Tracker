from django.shortcuts import redirect, render
from .models import Food,Consume
# Create your views here.


def index(request):
    
    if request.method=='POST':
        food_consumed = request.POST['food_cosumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        
        consume = Consume(user=user,food_cosume=consume)
        consume.save()
        items = Food.objects.all()
    

    
    else:
   
        items = Food.objects.all()
    foods = Consume.objects.filter(user=request.user)
   



    return render(request,'food/index.html',{'items':items,'foods':foods})

def delete_consume(request,id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/index')


    return render(request,'food/delete.html')