from .models import *
from django.shortcuts import render, get_object_or_404


def global_variables(request):
    # ---------------gaming peripherals sub categories--------------------
    # Gpsub_categories = Sub_Category.objects.filter(main_category__name = "Gaming Peripherals")
    
    homebody_paths = [
        '/',
        '/pc-builds/',
        '/reviews/',
        '/buying-guide/',
        '/knowledge-base/',
        '/coming-soon/',
        '/reviews/gaming-peripherals/',
        '/reviews/pc-components/',
        '/knowledge-base/pc-building-tips/',
        '/knowledge-base/pc-knowledge/',
        '/knowledge-base/gaming-knowledge/',
        '/buying-guide/gaming-peripherals/',
        '/buying-guide/pc-components/',
        '/buying-guide/gaming-laptops/',
        '/reviews/gaming-peripherals/mouse/',
        '/reviews/gaming-peripherals/keyboards/',
        '/reviews/gaming-peripherals/monitors/',
        '/reviews/gaming-peripherals/mouse-pads/',
        '/reviews/gaming-peripherals/gaming-chairs/',
        '/reviews/gaming-peripherals/headsets/',
        '/reviews/pc-components/cpu/',
        '/reviews/pc-components/cpu-coolers/',
        '/reviews/pc-components/gpu/',
        '/reviews/pc-components/motherboards/',
        '/reviews/pc-components/ram/',
        '/reviews/pc-components/ssd/',
        '/reviews/pc-components/psu/',
        '/reviews/pc-components/cases/'
    ]
    
    #get the latest reviews------------------
    latest_reviews = Review.objects.order_by('-date_created')[:8]
    
    
    current_slug = request.path.split('/')[-2]# Assuming the slug is the second-to-last part of the URL
    # print(current_slug)
    you_may_like_before = Review.objects.order_by('?').exclude(slug=current_slug) # before slicicng to only 10 review
    you_may_like = you_may_like_before[:25] # for the right widget in all reviews
    try:
        review = Review.objects.get(slug = current_slug) # get which review for each page
    except:
        review = None
        
    pc_builds_related_before = Review.objects.filter(main_category__name = 'PC Builds').order_by('?').exclude(slug=current_slug)
    pc_builds_related = pc_builds_related_before[:8]
    try:
        main_page = Category.objects.get( slug=request.path.split('/')[1])
        
    except:
        main_page = None
        
    try:
        sub_main_page = Sub_Category.objects.get(path=request.path.split('/')[2])
    except:
        sub_main_page = None
        
    try:
        sub_sub_main_page = Sub_SubCategory.objects.get(path=request.path.split('/')[3])
    except:
        sub_sub_main_page = None
        
    return{'latest_reviews' : latest_reviews , 'you_may_like' : you_may_like , 'review' : review ,'pc_builds_related' : pc_builds_related , 'main_page' : main_page , 'sub_main_page' : sub_main_page , 'homebody_paths' : homebody_paths , 'sub_sub_main_page' : sub_sub_main_page}