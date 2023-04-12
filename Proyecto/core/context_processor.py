def total_carrito(request):
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += float(value["acumulado"])
    return {"total_carrito": total}

def total_carrito_cantidad(request):
    totalc = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                totalc += int(value["cantidad"])
    return {"total_carrito_cantidad": totalc}