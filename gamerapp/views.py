from django.shortcuts import render
from .models import *
# from django.db.models.functions import Random
from random import sample
from django.db.models import Count
from .utils import *
from random import shuffle
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):    
    total_reviews = Review.objects.count()
    # this function get in the one_review only 1 review and in the trending_reviews 8 reviews 
    # and in the you_may_like_reviews 3 reviews and popular_reviews the rest and no any reviews are overlaping
    
    # If there are reviews available, retrieve up to two random reviews
    if total_reviews > 0:
    # Retrieve up to two random reviews for one_review
        one_review = Review.objects.order_by('?').first()
                
        all_review_ids = list(Review.objects.exclude(id=one_review.id).values_list('id', flat=True))

        # Shuffle the review IDs and split them into trending_eight_ids, you_may_like_eight_ids, and remaining_ids
        shuffled_review_ids = sample(all_review_ids, len(all_review_ids))
        trending_ids = shuffled_review_ids[:min(8, total_reviews - 1)]
        
        # Retrieve only 3 reviews for you_may_like_eight_reviews
        you_may_like_ids = shuffled_review_ids[min(8, total_reviews - 1):min(11, total_reviews - 1)]

        remaining_ids = shuffled_review_ids[min(11, total_reviews - 1):]

        # Retrieve reviews for trending_eight_reviews, you_may_like_eight_reviews, and remaining_reviews
        trending_reviews = Review.objects.filter(id__in=trending_ids)
        you_may_like_reviews = Review.objects.filter(id__in=you_may_like_ids)
        remaining_reviews = Review.objects.filter(id__in=remaining_ids)

        # Add popular_posts containing all remaining reviews
        popular_posts = remaining_reviews
    else:
        # Handle the case where there are no reviews
        one_review = []
        trending_reviews = []
        you_may_like_reviews = []
        popular_posts = []
        

    
    
    
    context={'one_review' : one_review , 'trending_reviews' : trending_reviews , 'you_may_like_reviews' : you_may_like_reviews , 'popular_posts' : popular_posts}
    return render(request, 'home.html' , context)

def search(request , search):
    if search:
        # Split the search string into words
        search_words = search.split()
        
        # Initialize an empty list to store query results
        results = []

        # Iterate over each word and perform the search
        for word in search_words:
            # Filter based on each word separately
            word_results = Review.objects.filter(topic__icontains=word)
            
            # Extend the results list with the current word's results
            results.extend(word_results)
    else:
        results = []
    
    context = {'results': results , 'search' : search}
    return render(request, 'search_results.html', context)


def coming_soon(request):
    
    context = {}
    return render(request, 'coming_soon.html', context)



def reviews(request):
    
    all_reviews = Review.objects.filter(main_category__name = 'Reviews').order_by('?')
    context={'all_reviews' : all_reviews}
    return render(request, 'reviews/reviews.html' , context)
# ----------------------------------------GAMING PERIPHERALS---------------------------------------------------------
#----------------category---------------
def gaming_peripherals_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/gaming_peripherals.html' , context)
#------------sub categories--------------
def mouse_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse.html' , context)

def keyboard_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/keyboard.html' , context)

def monitor_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/monitor.html' , context)

def chair_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/chair.html' , context)

def mouse_pad_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_pad.html' , context)

def headset_reviews(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/headset.html' , context)

# ----------------reviews----------------


def logitech_g402_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/logitech_g402_review.html' , context)

def logitech_g502_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/logitech_g502_review.html' , context)

def finalmouse_ultralightx_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/finalmouse_ultralightx_review.html' , context)




# -------------------------------------------------------------------KNOWLEDGE BASE--------------------------------------------
def knowledge_base(request):
    all_knowledge = Review.objects.filter(main_category__name = 'Knowledge Base').order_by('?')
    
    context={"all_knowledge" : all_knowledge}
    return render(request, 'knowledge_base/knowledge_base.html' , context)


def pc_building_tips(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_building_tips.html' , context)


def pc_knowledge(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_knowledge.html' , context)


def gaming_knowledge(request):
    
    
    context={}
    return render(request, 'knowledge_base/gaming_knowledge.html' , context)


def mistakes_new_pc_builder_make(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_building_tips/top_15_mistakes_new_pc_builder_make.html' , context)

def common_asked_questions_about_pc_building(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_building_tips/common_asked_questions_about_pc_building.html' , context)

def prebuilt_vs_custom_pc(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_knowledge/prebuilt_vs_custom_pc.html' , context)


def custom_pc_builder_websites(request):
    
    
    context={}
    return render(request, 'knowledge_base/pc_building_tips/custom_pc_builder_websites.html' , context)


def what_is_a_good_fps_for_gaming(request):
    
    
    context={}
    return render(request, 'knowledge_base/gaming_knowledge/what-is-a-good-fps-for-gaming.html' , context)


# -------------------------------------------------------------------------NEWS----------------------------------------------------
def news(request):
    
    
    context={}
    return render(request, 'news/news.html' , context)

#--------------------------------------------------------------------------laptops---------------------------------------------------
def laptops(request):
    
    
    context={}
    return render(request, 'laptops/laptops.html' , context)

#-------------------------------------------------------------------PC BUILDS------------------------------------------------------
#-------------------------category--------------------------------
def pc_builds(request):
    pc_builds = Review.objects.filter(main_category__name = 'PC Builds').order_by('?')
    
    context={'pc_builds' : pc_builds}
    return render(request, 'pc_builds/pc_builds.html' , context)
#------------------------sub categories---------------------------
def budget_pc_builds(request):
    
    
    context={}
    return render(request, 'pc_builds/budget_pc_builds.html' , context)

def mid_range_pc_builds(request):
    
    
    context={}
    return render(request, 'pc_builds/mid_range_pc_builds.html' , context)

def high_end_pc_builds(request):
    
    
    context={}
    return render(request, 'pc_builds/high_end_pc_builds.html' , context)
#----------------------reviews-----------------------------------
def pc_under_300(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_300.html' , context)

def pc_under_400(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_400.html' , context)

def pc_under_500(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_500.html' , context)

def pc_under_600(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_600.html' , context)

# ------------------------

def pc_under_700(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_700.html' , context)

def pc_under_800(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_800.html' , context)

def pc_under_1000(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_1000.html' , context)

def pc_under_1200(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_1200.html' , context)


# ------------------------

def pc_under_1500(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_1500.html' , context)


def pc_under_2000(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_2000.html' , context)

def pc_under_3000(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_3000.html' , context)

def pc_under_4000(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_4000.html' , context)

def pc_under_5000(request):
    
    
    context={}
    return render(request, 'pc_builds/pc_under_5000.html' , context)



# -------------------------------------------buying guides---------------------------------------------

def buying_guide(request):
    all_guides = Review.objects.filter(main_category__name = 'Buying Guide').order_by('?')
    
    context={'all_guides' : all_guides}
    return render(request, 'buying_guides/buying_guide.html' , context)

# -------------------------gaming peripherals--------------------------------

def gaming_peripherals_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/gaming_peripherals.html' , context)
#------------sub categories--------------
def mouse_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse.html' , context)

def keyboard_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/keyboard.html' , context)

def monitor_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/monitor.html' , context)

def chair_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/chair.html' , context)

def mouse_pad_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse_pad.html' , context)

def headset_buying_guide(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/headset.html' , context)




def top_10_logitech_mouse(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse_guides/top_10_logitech_mouse.html' , context)

def top_10_razer_mouse(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse_guides/top_10_razer_mouse.html' , context)