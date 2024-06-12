from pprint import pprint
from django.http import JsonResponse
from django.shortcuts import render
from .logic import (
    answer_query,
    build_database,
)  # Import your logic functions here
import threading


def index(request):
    if request.method == "POST":
        query = request.POST.get("query")
        result = answer_query(query)
        print(f"result:")
        pprint(result)
        result = result.get("content", "no result returned")
        print(result)
        return JsonResponse(result, safe=False)  # Set safe to False here
    return render(request, "base/index.html")


def db_status(request):
    status = {
        "exists": True,
        "message": ("Database exists"),
    }
    return JsonResponse(status)


def build_db(request):
    # Use threading to build the database asynchronously
    thread = threading.Thread(target=build_database)
    thread.start()
    return JsonResponse({"status": "Building database..."})
