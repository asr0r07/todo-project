from django.shortcuts import HttpResponse

def task_create(request):
    html_response="""
        ##Task_Create
    """
    return HttpResponse(html_response)