from django.shortcuts import render
from polls.models import Worker

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def polls(request):
    # Создание нового элемента бд
    # new_worker = Worker(name = 'Артур', second_name = 'Акулич', salary = '400')
    # new_worker.save()

    # Изменение
    # worker_to_change = Worker.objects.get(id = 5)
    # worker_to_change.second_name = 'Демко'
    # worker_to_change.save()

    # Удаление
    # Worker.objects.get(id=4).delete()

    all_workers = Worker.objects.all()
    print(all_workers)
    for i in all_workers:
        print(i.id, i.second_name, i.name, i.salary)

    workers_filtered = Worker.objects.filter(salary = 500)
    print(workers_filtered)
    return render(request, 'polls.html')