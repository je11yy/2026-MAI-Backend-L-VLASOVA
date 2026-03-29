from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods


# -------------------------
# WEB VIEWS
# -------------------------

@require_http_methods(["GET"])
def web_home(request):
    html = """
    <h1>Каталог книг</h1>
    <ul>
        <li><a href="/web/profile/">Профиль</a></li>
        <li><a href="/web/books/">Все книги</a></li>
        <li><a href="/web/category/fiction/">Категория: fiction</a></li>
        <li><a href="/web/books/1/">Книга #1</a></li>
        <li><a href="/web/favorites/">Избранное</a></li>
    </ul>
    """
    return HttpResponse(html)


@require_http_methods(["GET"])
def web_profile(request):
    html = """
    <h1>Профиль пользователя</h1>
    <p>Здесь будет личный кабинет пользователя.</p>
    <a href="/web/">Назад</a>
    """
    return HttpResponse(html)


@require_http_methods(["GET"])
def web_books(request):
    html = """
    <h1>Список книг</h1>
    <ul>
        <li><a href="/web/books/1/">1984</a></li>
        <li><a href="/web/books/2/">Мастер и Маргарита</a></li>
        <li><a href="/web/books/3/">Норвежский лес</a></li>
    </ul>
    <a href="/web/">Назад</a>
    """
    return HttpResponse(html)


@require_http_methods(["GET"])
def web_category(request, slug):
    html = f"""
    <h1>Категория: {slug}</h1>
    <p>Здесь будет список книг категории "{slug}".</p>
    <a href="/web/">Назад</a>
    """
    return HttpResponse(html)


@require_http_methods(["GET"])
def web_book_detail(request, book_id):
    html = f"""
    <h1>Страница книги #{book_id}</h1>
    <p>Здесь будет полная информация о книге.</p>
    <a href="/web/">Назад</a>
    """
    return HttpResponse(html)


@require_http_methods(["GET"])
def web_favorites(request):
    html = """
    <h1>Избранные книги</h1>
    <p>Здесь будет список избранного пользователя.</p>
    <a href="/web/">Назад</a>
    """
    return HttpResponse(html)


# -------------------------
# API VIEWS
# -------------------------

@require_http_methods(["GET"])
def api_profile(request):
    return JsonResponse({
        "status": "ok",
        "data": {
            "id": 1,
            "username": "lada",
            "favorite_books_count": 2,
        }
    })


@require_http_methods(["GET"])
def api_books(request):
    return JsonResponse({
        "status": "ok",
        "data": [
            {
                "id": 1,
                "title": "1984",
                "author": "George Orwell",
                "category": "fiction",
            },
            {
                "id": 2,
                "title": "Мастер и Маргарита",
                "author": "Михаил Булгаков",
                "category": "classic",
            },
            {
                "id": 3,
                "title": "Норвежский лес",
                "author": "Харуки Мураками",
                "category": "japanese-literature",
            },
        ]
    })


@require_http_methods(["GET"])
def api_category(request, slug):
    return JsonResponse({
        "status": "ok",
        "category": {
            "slug": slug,
            "title": slug.capitalize(),
        },
        "books": [
            {
                "id": 1,
                "title": "Пример книги 1",
                "author": "Автор 1",
            },
            {
                "id": 2,
                "title": "Пример книги 2",
                "author": "Автор 2",
            },
        ]
    })


@require_http_methods(["GET"])
def api_book_detail(request, book_id):
    return JsonResponse({
        "status": "ok",
        "data": {
            "id": book_id,
            "title": f"Книга #{book_id}",
            "author": "Неизвестный автор",
            "description": "Здесь будет полное описание книги.",
            "category": "fiction",
            "is_favorite": False,
        }
    })


@require_http_methods(["GET"])
def api_favorites(request):
    return JsonResponse({
        "status": "ok",
        "data": [
            {
                "id": 1,
                "title": "1984",
                "author": "George Orwell",
            },
            {
                "id": 3,
                "title": "Норвежский лес",
                "author": "Харуки Мураками",
            },
        ]
    })


@require_http_methods(["POST"])
def api_add_favorite(request):
    return JsonResponse({
        "status": "ok",
        "message": "Книга добавлена в избранное"
    })


@require_http_methods(["POST"])
def api_remove_favorite(request):
    return JsonResponse({
        "status": "ok",
        "message": "Книга удалена из избранного"
    })