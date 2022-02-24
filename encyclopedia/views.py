from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import markdown
import random

from . import util

from . import urls


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def pages(request, title):
    entries = util.list_entries()
    if title in entries:
    #get the entry(in markdown) by its title
        title_page = util.get_entry(title)
        md = markdown.Markdown()
        return render(request, "encyclopedia/pages.html",
        {
        "text": md.convert(title_page),
        "title": title
        })
    else:
        error = "404 Error: The requested URL was not found"
        return render(request,"encyclopedia/error.html",
        {
            "error" : error
        })

    

        

def search(request):
    # get the value of the form
    search_item = request.GET.get("q")
    # check if the value matches the entries in the form
    entries = util.list_entries()
    if search_item in entries:
        return HttpResponseRedirect(f"/wiki/{search_item}")
    else:
        #return a list which have the search value as a substring
        
        substring_list =[]
        for entry in entries:
            if search_item in entry:
                substring_list.append(entry)
        return render(request,"encyclopedia/search.html",
        {
            "substring_list": substring_list
        })
        


def create(request):
    if request.method=="GET":
        return render(request, "encyclopedia/create.html")
    else:
        title = request.POST.get("title")
        description = request.POST.get("description")
        # check if title already exist, render an error message

        entries = util.list_entries()
        if title in entries:
            error = "This page already exists."
            return render(request,"encyclopedia/error.html",
            {
                "error": error
            })
        else:
            # save the entry and redirect user to the new page
            util.save_entry(title, description)
            return HttpResponseRedirect(f"/wiki/{title}")



def edit(request,title):
    # render the page for user to edit the content if user reach route via GET
    if request.method=="GET":
        title_page = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",
        {
        "text": title_page,
        "title": title
        })
    
    # if user reach route via POST(save the edits) 
    else:
        new_description = request.POST.get("new_description")
        # save the user entry and replace the current file
        util.save_entry(title, new_description)
        #redirect user to the new page
        return HttpResponseRedirect(f"/wiki/{title}")




def random_entry(request):
    # get a list of all the entries
    entries = util.list_entries()

    # get a random number bewteen 0 and the length of list
    rand_number = random.randint(0,len(entries)-1)
    page = entries[rand_number]
    return HttpResponseRedirect(f"/wiki/{page}")











    



