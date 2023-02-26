from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    #my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    #  <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Geek Test</title>
    #         </head>
    #         <body>
    #
    #             <h1>Заголовок первого уровня</h1>
    #             <p>Параграф</p>
    #
    #         </body>
    #     </html>
    # """
    headers = {"name": "Alex",}
               # "Content-Type": "application/vnd.ms-excel",
               # "content-Disposition": "attachment; filename=file.xls"}

    return HttpResponse(body, headers=headers, status=500)

def get_index(request):
    # print(request, headers)
    if request.method == "GET":
        return HttpResponse("Главная страница")
    else:
        return HttpResponse("Не тот метод запроса")

def get_contacts(request):
    return HttpResponse("contacts")

def get_about(request):
    return HttpResponse("about")




