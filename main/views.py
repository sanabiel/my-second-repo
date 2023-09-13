from django.shortcuts import render

def show_main(request):
    context = {
        'item_inventory' : [
            {
                'name': 'Piring The Flop',
                'description': 'Piring yang lansung dibuat dari Norwegia pembawa kekuatan',
                'amount': '5',
                'promo' : 'FLASH SALE 50%',
                'price': '1000000'  

            },
        ],
    }

    return render(request, "main.html", context)