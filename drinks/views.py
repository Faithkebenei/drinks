# This is where we create all endpoints (a url to access data from)
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#We can make this function to do all the CRUD
#To do this, we are going to use a decorator, which is a design pattern that we put above our fuction to describe our function
@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    if request.method == 'GET':        
        #get all drinks
        drinks = Drink.objects.all()

        #serialize them
        serializer = DrinkSerializer(drinks, many=True)
    
        #return json
        return Response(serializer.data)
    
    
    if request.method == 'POST':
        #Take data they give us, deserialize and then create a drink object
        serializer = DrinkSerializer(data=request.data)
        #check if data they give us is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

#To get one drink based on ID, go to urls.py and create another path
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    #Get the id passed and check if it is valid
    try:
        drink = Drink.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#Now we have to say what url is going to hit this view. We do this inside urls.py
#Next instructions are here, urls.py