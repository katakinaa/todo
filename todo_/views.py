from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from todo_.models import Task
from todo_.serializers import TaskSerializer


@api_view(http_method_names=['GET', 'POST'])
def task_list_create_api_view(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        data = TaskSerializer(instance=tasks, many=True).data
        return Response(data=data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        completed = request.data.get('completed', False)

        task = Task.objects.create(
            title=title,
            description=description,
            completed=completed
        )
        task.save()

        return Response(status=status.HTTP_201_CREATED,
                        data={'task_id': task.id})


@api_view(http_method_names=['GET'])
def task_detail_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    data = TaskSerializer(instance=task).data
    return Response(data=data)


@api_view(http_method_names=['PUT'])
def task_update_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    task.title = request.data.get('title', task.title)
    task.description = request.data.get('description', task.description)
    task.completed = request.data.get('completed', task.completed)
    task.save()

    return Response(data=TaskSerializer(instance=task).data, status=status.HTTP_200_OK)


@api_view(http_method_names=['DELETE'])
def task_delete_api_view(request, id):
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        return Response(data={"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response(data={"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
