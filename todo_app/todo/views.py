from django.shortcuts import render
from django.http import HttpResponseRedirect
#import TodoItem class from the same folder as the current file
from .models import TodoItem 
# Create your views here.

def todoView(request):
    #store all TodoItem objects that are created in all_todo_items
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html', 
                 {'all_items': all_todo_items})


#function to process request to add todo item to list
def addTodo(request):
    #in the post request received, find the attribute with the name 'content'
    c = request.POST['content']
    #create a new todo object with the specified content
    new_item = TodoItem(content = c)
    #Note: can combine first two steps -> new_item = TodoItem(content = request.POST['content])
    #save
    new_item.save()
    #redirect the browser back to the original page '/todo/'
    return HttpResponseRedirect('/todo/') #must import this function

def deleteTodo(request, todo_id):
    #the TodoItem object was assigned the name todo_id in urls.py
    #we can make use of that feature
    delete_this = TodoItem.objects.get(id=todo_id)
    delete_this.delete()
    #redirect the browser back to the original page '/todo/'
    return HttpResponseRedirect('/todo/')