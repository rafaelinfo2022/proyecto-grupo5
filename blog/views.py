from django.shortcuts import render

#funcion para mortrar paguina principal archivo html
def index(request):
    return render(request, 'index.html')

def acerca_de(request):
    return render ( request,'acerca_de.html' )

