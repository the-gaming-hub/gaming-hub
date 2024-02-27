from .models import *
from django.shortcuts import render, get_object_or_404


def global_variables(request):
    # ---------------gaming peripherals sub categories--------------------
    # Gpsub_categories = Sub_Category.objects.filter(main_category__name = "Gaming Peripherals")
    
    #get the latest reviews------------------
    latest_reviews = Review.objects.order_by('-date_created')[:8]
    
    
    current_slug = request.path.split('/')[-2]# Assuming the slug is the second-to-last part of the URL
    print(current_slug)
    you_may_like_before = Review.objects.order_by('?').exclude(slug=current_slug) # before slicicng to only 10 review
    you_may_like = you_may_like_before[:20] # for the right widget in all reviews
    try:
        review = Review.objects.get(slug = current_slug) # get which review for each page
    except:
        review = None
        
    pc_builds_related_before = Review.objects.filter(main_category__name = 'PC Builds').order_by('?').exclude(slug=current_slug)
    pc_builds_related = pc_builds_related_before[:8]
    try:
        current_page = Category.objects.get(slug=current_slug)
    except:
        current_page = None
    
    return{'latest_reviews' : latest_reviews , 'you_may_like' : you_may_like , 'review' : review ,'pc_builds_related' : pc_builds_related , 'current_page' : current_page}