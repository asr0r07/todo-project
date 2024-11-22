from django.shortcuts import HttpResponse

def task_create(request):
    html_response="""
        <h1>Task_Create</h1>
    """
    return HttpResponse(html_response)