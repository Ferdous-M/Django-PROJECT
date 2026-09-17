from django.http import HttpResponse

def home_page(request):
    print("home page requested")
    return HttpResponse("<h1>This is a home page</h1>")


# from django.http import JsonResponse


# def home_page(request):
#     print("home page requested")

#     return JsonResponse({
#         "message": "This is our company API"
#     })