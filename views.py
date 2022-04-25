def my_view(request):
    if request.method == 'POST':
        import Butler1.py
        #Do your stuff ,calling whatever you want from set_gpio.py

    return #Something, normally a HTTPResponse, using django