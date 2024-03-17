from django.shortcuts import render, redirect
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
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.http import Http404
from django.conf import settings
import base64


# Create your views here.

def get_referer(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer:
        return None
    return referer


def newsletter_subscriptions(request , email):
    try:
        try:
            new_subscriber = NewsletterSubscription.objects.create(email = email)
        except:
            new_subscriber = NewsletterSubscription.objects.get(email = email,active = False)
        subject = 'Email Confirmation'
        
        with open('static/images/thegaminghub-logo.png', 'rb') as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

        email_confirmation_template = render_to_string('subscription_confirmation/email_confirmation.html',{
            'domain' : get_current_site(request).domain,
            'uid' : urlsafe_base64_encode(force_bytes(new_subscriber.pk)),
            'token' : account_activation_token.make_token(new_subscriber    ),
            'protocol' : 'https' if request.is_secure() else 'http',
            'thegaminghub_logo': encoded_image
            })
        email_confirmation = EmailMessage(
            subject, # mail subject
            email_confirmation_template, # mail content
            settings.EMAIL_HOST_USER,
            [email] # sending to
        )
        email_confirmation.content_subtype = 'html'
        # email_confirmation.send()
        email_confirmation.send()
        response_data = {'success': True}
    except Exception as e:
        print(e)  # Print the exception for debugging
        response_data = {'error': True}
    return JsonResponse(response_data)

def activate(request, uidb64, token):
    try:
        # Decode the UID and retrieve the email from your email model
        uid = force_str(urlsafe_base64_decode(uidb64))
        email_instance = NewsletterSubscription.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, NewsletterSubscription.DoesNotExist):
        email_instance = None

    if email_instance is not None and account_activation_token.check_token(email_instance, token):
        # If the token is valid, set the email as confirmed
        email_instance.confirmed = True
        email_instance.active = True
        email_instance.save()
        return redirect('subscription-confirmed')  # Redirect to your homepage
    else:
        raise Http404

def subscription_confirmed(request):
    
    context={}
    return render(request, 'subscription_confirmation/subscription_confirmed.html' , context)


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

def contact(request):
    
    context = {}
    return render(request, 'contact.html', context)

def privacy_policy(request):
    
    context = {}
    return render(request, 'privacy_policy.html', context)

def about(request):
    
    context = {}
    return render(request, 'about.html', context)



def reviews(request):
    
    all_reviews = Review.objects.filter(main_category__name = 'Reviews').order_by('?')
    context={'all_reviews' : all_reviews}
    return render(request, 'reviews/reviews.html' , context)
# ----------------------------------------GAMING PERIPHERALS---------------------------------------------------------
#----------------category---------------
def gaming_peripherals_reviews(request):

    gaming_peripherals_reviews = Review.objects.filter(sub_category__slug = 'gaming-peripherals-reviews').order_by('?')
    context={'gaming_peripherals_reviews' : gaming_peripherals_reviews}
    return render(request, 'reviews/gaming_peripherals/gaming_peripherals.html' , context)

def pc_components_reviews(request):

    pc_components_reviews = Review.objects.filter(sub_category__slug = 'pc-components-reviews').order_by('?')
    context={'pc_components_reviews' : pc_components_reviews}
    return render(request, 'reviews/pc_components/pc_components.html' , context)

def gaming_laptops_reviews(request):

    gaming_laptops_reviews = Review.objects.filter(sub_category__slug = 'gaming-laptops-reviews').order_by('?')
    context={'gaming_laptops_reviews' : gaming_laptops_reviews}
    return render(request, 'reviews/gaming_laptops/gaming_laptops.html' , context)


#------------sub categories--------------
def mouse_reviews(request):
    
    mouse_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'mouse-reviews').order_by('?')
    context={'mouse_reviews' : mouse_reviews}
    return render(request, 'reviews/gaming_peripherals/mouse.html' , context)

def keyboard_reviews(request):
    
    keyboards_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'keyboards-reviews').order_by('?')
    context={'keyboards_reviews' : keyboards_reviews}
    return render(request, 'reviews/gaming_peripherals/keyboard.html' , context)

def monitor_reviews(request):
    
    monitors_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'monitors-reviews').order_by('?')
    context={'monitors_reviews' : monitors_reviews}
    return render(request, 'reviews/gaming_peripherals/monitor.html' , context)

def chair_reviews(request):
    
    gaming_chairs_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'gaming-chairs-reviews').order_by('?')
    context={'gaming_chairs_reviews' : gaming_chairs_reviews}
    return render(request, 'reviews/gaming_peripherals/chair.html' , context)

def mouse_pad_reviews(request):
    
    mouse_pads_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'mouse-pads-reviews').order_by('?')
    context={'mouse_pads_reviews' : mouse_pads_reviews}
    return render(request, 'reviews/gaming_peripherals/mouse_pad.html' , context)

def headset_reviews(request):
    
    headsets_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'gaming-peripherals-reviews' , sub_subcategory__slug = 'headsets-reviews').order_by('?')
    context={'headsets_reviews' : headsets_reviews}
    return render(request, 'reviews/gaming_peripherals/headset.html' , context)

                #-----------------pc components-----------------

def cpu_reviews(request):
    
    cpu_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'cpu-reviews').order_by('?')
    context={'cpu_reviews' : cpu_reviews}
    return render(request, 'reviews/pc_components/cpu_reviews.html' , context)

def cpu_cooler_reviews(request):
    
    cpu_cooler_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'cpu-cooler-reviews').order_by('?')
    context={'cpu_cooler_reviews' : cpu_cooler_reviews}
    return render(request, 'reviews/pc_components/cpu_coolers_reviews.html' , context)

def gpu_reviews(request):
    
    gpu_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'gpu-reviews').order_by('?')
    context={'gpu_reviews' : gpu_reviews}
    return render(request, 'reviews/pc_components/gpu_reviews.html' , context)

def motherboard_reviews(request):
    
    motherboard_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'motherboard-reviews').order_by('?')
    context={'motherboard_reviews' : motherboard_reviews}
    return render(request, 'reviews/pc_components/motherboards_reviews.html' , context)

def ram_reviews(request):
    
    ram_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'ram-reviews').order_by('?')
    context={'ram_reviews' : ram_reviews}
    return render(request, 'reviews/pc_components/ram_reviews.html' , context)

def ssd_reviews(request):
    
    ssd_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'ssd-reviews').order_by('?')
    context={'ssd_reviews' : ssd_reviews}
    return render(request, 'reviews/pc_components/ssd_reviews.html' , context)

def psu_reviews(request):
    
    psu_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'psu-reviews').order_by('?')
    context={'psu_reviews' : psu_reviews}
    return render(request, 'reviews/pc_components/psu_reviews.html' , context)

def case_reviews(request):
    
    cases_reviews = Review.objects.filter(main_category__name = 'Reviews' , sub_category__slug = 'pc-components-reviews' , sub_subcategory__slug = 'cases-reviews').order_by('?')
    context={'cases_reviews' : cases_reviews}
    return render(request, 'reviews/pc_components/cases_reviews.html' , context)




# ----------------reviews----------------

        #------- gaming peripherals reviewsss-----------
def logitech_g402_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/logitech_g402_review.html' , context)

def logitech_g502_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/logitech_g502_review.html' , context)

def finalmouse_ultralightx_review(request):
    
    
    context={}
    return render(request, 'reviews/gaming_peripherals/mouse_reviews/finalmouse_ultralightx_review.html' , context)

        #--------pc components reviews-------------
        
def amd_ryzen_9_5900x_review(request):
    
    
    context={}
    return render(request, 'reviews/pc_components/cpu_reviews/amd_ryzen_9_5900x_review.html' , context)


# -------------------------------------------------------------------KNOWLEDGE BASE--------------------------------------------
def knowledge_base(request):
    all_knowledge = Review.objects.filter(main_category__name = 'Knowledge Base').order_by('?')
    
    context={"all_knowledge" : all_knowledge}
    return render(request, 'knowledge_base/knowledge_base.html' , context)


def pc_building_tips(request):
    
    pc_building_tips_reviews = Review.objects.filter(sub_category__slug = 'pc-building-tips').order_by('?')
    context={'pc_building_tips_reviews' : pc_building_tips_reviews}
    return render(request, 'knowledge_base/pc_building_tips.html' , context)


def pc_knowledge(request):
    
    pc_knowledge_reviews = Review.objects.filter(sub_category__slug = 'pc-knowledge').order_by('?')
    context={'pc_knowledge_reviews' : pc_knowledge_reviews}
    return render(request, 'knowledge_base/pc_knowledge.html' , context)


def gaming_knowledge(request):
    
    gaming_knowledge_reviews = Review.objects.filter(sub_category__slug = 'gaming-knowledge').order_by('?')
    context={'gaming_knowledge_reviews' : gaming_knowledge_reviews}
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

#-------------------------------------------------------------------PC BUILDS------------------------------------------------------
#-------------------------category--------------------------------
def pc_builds(request):
    pc_builds = Review.objects.filter(main_category__name = 'PC Builds').order_by('?')
    
    context={'pc_builds' : pc_builds}
    return render(request, 'pc_builds/pc_builds.html' , context)
#------------------------sub categories---------------------------
def budget_pc_builds(request):
    
    budget_pc_builds = Review.objects.filter(main_category__name = 'PC Builds' , sub_category__slug = 'budget-pc-builds').order_by('?')
    context={'budget_pc_builds' : budget_pc_builds}
    return render(request, 'pc_builds/budget_pc_builds.html' , context)

def mid_range_pc_builds(request):
    
    mid_range_pc_builds = Review.objects.filter(main_category__name = 'PC Builds' , sub_category__slug = 'mid-range-pc-builds').order_by('?')
    context={'mid_range_pc_builds' : mid_range_pc_builds}
    return render(request, 'pc_builds/mid_range_pc_builds.html' , context)

def high_end_pc_builds(request):
    
    high_end_pc_builds = Review.objects.filter(main_category__name = 'PC Builds' , sub_category__slug = 'high-end-pc-builds').order_by('?')
    context={'high_end_pc_builds' : high_end_pc_builds}
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
    
    gaming_peripherals_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides').order_by('?')
    context={'gaming_peripherals_buying_guides' : gaming_peripherals_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/gaming_peripherals.html' , context)

def pc_components_buying_guide(request):
    
    pc_components_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guide').order_by('?')
    context={'pc_components_buying_guides' : pc_components_buying_guides}
    return render(request, 'buying_guides/pc_components/pc_components.html' , context)

def gaming_laptops_buying_guide(request):
    
    gaming_laptops_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-laptops-buying-guide').order_by('?')
    context={'gaming_laptops_buying_guides' : gaming_laptops_buying_guides}
    return render(request, 'buying_guides/gaming_laptops/gaming_laptops.html' , context)
#------------sub categories--------------
def mouse_buying_guide(request):
    
    mouse_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'mouse-buying-guides').order_by('?')
    context={'mouse_buying_guides' : mouse_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/mouse.html' , context)

def keyboard_buying_guide(request):
    
    keyboard_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'keyboards-buying-guides').order_by('?')
    context={'keyboard_buying_guides' : keyboard_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/keyboard.html' , context)

def monitor_buying_guide(request):
    
    monitor_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'monitors-buying-guides').order_by('?')
    context={'monitor_buying_guides' : monitor_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/monitor.html' , context)

def chair_buying_guide(request):
    
    gaming_chair_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'gaming-chairs-buying-guides').order_by('?')
    context={'gaming_chair_buying_guides' : gaming_chair_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/chair.html' , context)

def mouse_pad_buying_guide(request):
    
    mouse_pad_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'mouse-pads-buying-guides').order_by('?')
    context={'mouse_pad_buying_guides' : mouse_pad_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/mouse_pad.html' , context)

def headset_buying_guide(request):
    
    headset_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'gaming-peripherals-buying-guides' , sub_subcategory__slug = 'headsets-buying-guides').order_by('?')
    context={'headset_buying_guides' : headset_buying_guides}
    return render(request, 'buying_guides/gaming_peripherals/headset.html' , context)

    #----------------pc components buyign guide-----------------------------

def cpu_buying_guide(request):
    
    cpu_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'cpu-buying-guides').order_by('?')
    context={'cpu_buying_guides' : cpu_buying_guides}
    return render(request, 'buying_guides/pc_components/cpu_buying_guide.html' , context)

def cpu_cooler_buying_guide(request):
    
    cpu_cooler_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'cpu-coolers-buying-guides').order_by('?')
    context={'cpu_cooler_buying_guides' : cpu_cooler_buying_guides}
    return render(request, 'buying_guides/pc_components/cpu_coolers_buying_guide.html' , context)

def gpu_buying_guide(request):
    
    gpu_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'gpu-buying-guides').order_by('?')
    context={'gpu_buying_guides' : gpu_buying_guides}
    return render(request, 'buying_guides/pc_components/gpu_buying_guide.html' , context)

def motherboard_buying_guide(request):
    
    motherboard_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'motherboards-buying-guides').order_by('?')
    context={'motherboard_buying_guides' : motherboard_buying_guides}
    return render(request, 'buying_guides/pc_components/motherboards_buying_guide.html' , context)

def ram_buying_guide(request):
    
    ram_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'ram-buying-guides').order_by('?')
    context={'ram_buying_guides' : ram_buying_guides}
    return render(request, 'buying_guides/pc_components/ram_buying_guide.html' , context)

def ssd_buying_guide(request):
    
    ssd_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'ssd-buying-guides').order_by('?')
    context={'ssd_buying_guides' : ssd_buying_guides}
    return render(request, 'buying_guides/pc_components/ssd_buying_guide.html' , context)

def psu_buying_guide(request):
    
    psu_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'psu-buying-guides').order_by('?')
    context={'psu_buying_guides' : psu_buying_guides}
    return render(request, 'buying_guides/pc_components/psu_buying_guide.html' , context)

def case_buying_guide(request):
    
    cases_buying_guides = Review.objects.filter(main_category__name = 'Buying Guide' , sub_category__slug = 'pc-components-buying-guides' , sub_subcategory__slug = 'cases-buying-guides').order_by('?')
    context={'cases_buying_guides' : cases_buying_guides}
    return render(request, 'buying_guides/pc_components/cases_buying_guide.html' , context)



#--------------- buying guide articles-----------------
def best_logitech_mouse(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse_guides/best_logitech_mouse.html' , context)

def best_razer_mouse(request):
    
    
    context={}
    return render(request, 'buying_guides/gaming_peripherals/mouse_guides/best_razer_mouse.html' , context)