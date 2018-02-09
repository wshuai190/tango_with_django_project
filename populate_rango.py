import os
os.environ.setdefault('DJANGO_SETTINGs_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
         "url" : "http://docs.python.org/2/tutorial/",
         "views" : 123},
        {"title": "How to Think like a Computer Scentist",
         "url" : "http://www.greenteapress.com/thinkpython/",
         "views" : 113},
        {"title": "Learn Python in 10 Minutes",
         "url" : "http://www.korokithkis.net/tutorials/python/",
         "views" : 100}]
    
    django_pages = [
        {"title": "Official Django Tutorial",
         "url" : "http://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "views" : 55},
        {"title": "Django Rocks",
         "url" : "http://www.djangorocks.com/",
         "views" : 65},
        {"title": "How to Tango with Django",
         "url" : "http://www.tangowithdjango.com/",
         "views" : 99}]

    other_pages = [
        {"title": "Bottle",
         "url" : "http://bottlepy.org/docs/dev/",
         "views" : 34},
        {"title": "Flask",
         "url" : "http://flask.pocoo.org",
         "views" : 103}]
        

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "Other Frameworks" : {"pages": other_pages, "views": 32, "likes": 16} }
                      
        
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data["views"], cat_data["likes"])  
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
        
        
        
    for c in Category.objects.all():
         for p in Page.objects.filter(category=c):
                print ("- {0} - {1}".format(str(c), str(p)))

    

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


if __name__ == '__main__':
    print ("Starting Rango population script...")
    populate()
































   
