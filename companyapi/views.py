from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("home page requested")
    friends=['a','b','c']
    return  JsonResponse(friends,safe=False)


# from django.http import JsonResponse


# def home_page(request):
#     print("home page requested")

#     return JsonResponse({
#         "message": "This is our company API"
#     })