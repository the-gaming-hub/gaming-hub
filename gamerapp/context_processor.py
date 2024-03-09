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
        '/pc-builds/budget-pc-builds/',
        '/pc-builds/mid-range-pc-builds/',
        '/pc-builds/high-end-pc-builds/',
        '/reviews/gaming-peripherals-reviews/',
        '/reviews/pc-components-reviews/',
        '/reviews/gaming-laptops-reviews/',
        '/knowledge-base/pc-building-tips/',
        '/knowledge-base/pc-knowledge/',
        '/knowledge-base/gaming-knowledge/',
        '/buying-guide/gaming-peripherals-buying-guides/',
        '/buying-guide/pc-components-buying-guides/',
        '/buying-guide/gaming-laptops-buying-guides/',
        '/reviews/gaming-peripherals-reviews/mouse-reviews/',
        '/reviews/gaming-peripherals-reviews/keyboards-reviews/',
        '/reviews/gaming-peripherals-reviews/monitors-reviews/',
        '/reviews/gaming-peripherals-reviews/mouse-pads-reviews/',
        '/reviews/gaming-peripherals-reviews/gaming-chairs-reviews/',
        '/reviews/gaming-peripherals-reviews/headsets-reviews/',
        '/reviews/pc-components-reviews/cpu-reviews/',
        '/reviews/pc-components-reviews/cpu-coolers-reviews/',
        '/reviews/pc-components-reviews/gpu-reviews/',
        '/reviews/pc-components-reviews/motherboards-reviews/',
        '/reviews/pc-components-reviews/ram-reviews/',
        '/reviews/pc-components-reviews/ssd-reviews/',
        '/reviews/pc-components-reviews/psu-reviews/',
        '/reviews/pc-components-reviews/cases-reviews/',
        '/buying-guide/pc-components-buying-guides/cpu-buying-guides/',
        '/buying-guide/pc-components-buying-guides/cpu-coolers-buying-guides/',
        '/buying-guide/pc-components-buying-guides/gpu-buying-guides/',
        '/buying-guide/pc-components-buying-guides/motherboards-buying-guides/',
        '/buying-guide/pc-components-buying-guides/ram-buying-guides/',
        '/buying-guide/pc-components-buying-guides/ssd-buying-guides/',
        '/buying-guide/pc-components-buying-guides/psu-buying-guides/',
        '/buying-guide/pc-components-buying-guides/cases-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/mouse-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/keyboards-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/headsets-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/mouse-pads-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/monitors-buying-guides/',
        '/buying-guide/gaming-peripherals-buying-guides/gaming-chairs-buying-guides/'
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
        sub_main_page = Sub_Category.objects.get(slug=request.path.split('/')[2])
    except:
        sub_main_page = None
        
    try:
        sub_sub_main_page = Sub_SubCategory.objects.get(slug=request.path.split('/')[3])
    except:
        sub_sub_main_page = None
        
    return{'latest_reviews' : latest_reviews , 'you_may_like' : you_may_like , 'review' : review ,'pc_builds_related' : pc_builds_related , 'main_page' : main_page , 'sub_main_page' : sub_main_page , 'homebody_paths' : homebody_paths , 'sub_sub_main_page' : sub_sub_main_page}