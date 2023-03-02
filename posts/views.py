from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
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
    posts = Post.objects.filter(status=True)
    context = {
        "title": "Main page",
        "posts": posts,
    }
    return render(request, "posts/index.html", context=context)
    # # print(request, headers)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("Не тот метод запроса")


def get_contacts(request):
    return render(request, "posts/contacts.html", context=None)

def get_about(request):
    context = {
        "title": "Страница о нас",
    }

    return render(request, "posts/about.html", context=None)




