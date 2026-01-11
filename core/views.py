from django.http import HttpRequest, HttpResponse

def home_view(r):
    return HttpResponse('Hello World')

def get_user_by_id_view(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f'Hello World by {id}')

def get_user_by_uuid_view(request: HttpRequest, uuid_t: str) -> HttpResponse:
    return HttpResponse(f'Hello World by {uuid_t}')

def get_user_by_id_view(request: HttpRequest, id: int) -> HttpResponse:
    return HttpResponse(f'Hello World by {id}')

def get_post_by_title_view(request: HttpRequest, title: str) -> HttpResponse:
    return HttpResponse(f'Hello World by {title}')

def get_sub_news_path_view(request: HttpRequest, path: str) -> HttpResponse:
    return HttpResponse(f'Hello World by {path}')