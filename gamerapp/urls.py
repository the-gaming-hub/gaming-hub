from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('search/<str:search>/', views.search, name='search'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    
    
    
    path('reviews/', views.reviews , name="reviews"),
    #-------------------------------------gaming peripherals------------------------------------------------
    # -----------category-------------------
    path('reviews/gaming-peripherals/', views.gaming_peripherals_reviews , name="gaming-peripherals-reviews"),
    path('reviews/pc-components/', views.pc_components_reviews , name="pc-components-reviews"),
    path('reviews/gaming-laptops/', views.gaming_laptops_reviews , name="gaming-laptops-reviews"),
    # --------------sub categories-----------
    path('reviews/gaming-peripherals/mouse/', views.mouse_reviews , name="mouse-reviews"),
    path('reviews/gaming-peripherals/keyboards/', views.keyboard_reviews , name="keyboards-reviews"),
    path('reviews/gaming-peripherals/headsets/', views.headset_reviews , name="headsets-reviews"),
    path('reviews/gaming-peripherals/mouse-pads/', views.mouse_pad_reviews , name="mouse-pads-reviews"),
    path('reviews/gaming-peripherals/monitors/', views.monitor_reviews , name="monitors-reviews"),
    path('reviews/gaming-peripherals/gaming-chairs/', views.chair_reviews , name="gaming-chairs-reviews"),
    
    
    path('reviews/pc-components/cpu/', views.cpu_reviews , name="cpu-reviews"),
    path('reviews/pc-components/cpu-coolers/', views.cpu_cooler_reviews , name="cpu-coolers-reviews"),
    path('reviews/pc-components/gpu/', views.gpu_reviews , name="gpu-reviews"),
    path('reviews/pc-components/motherboards/', views.motherboard_reviews , name="motherboards-reviews"),
    path('reviews/pc-components/ram/', views.ram_reviews , name="ram-reviews"),
    path('reviews/pc-components/ssd/', views.ssd_reviews , name="ssd-reviews"),
    path('reviews/pc-components/psu/', views.psu_reviews , name="psu-reviews"),
    path('reviews/pc-components/cases/', views.case_reviews , name="cases-reviews"),
    #-----------------reviews------------------
                    # ----gaming peripheralss------------
    path('reviews/gaming-peripherals/mouse/logitech-g402-review-2024/', views.logitech_g402_review , name="logitech-g402-hyperion-fury-review-2024"),
    path('reviews/gaming-peripherals/mouse/logitech-g502-lightspeed-review-2024/', views.logitech_g502_review , name="logitech-g502-lightspeed-review-2024"),
    path('reviews/gaming-peripherals/mouse/finalmouse-ultralightx-mouse-review/', views.finalmouse_ultralightx_review , name="finalmouse-ultralightx-mouse-review"),
                    #-------- pc componentss-------------
    path('reviews/pc-components/cpu/amd-ryzen-9-5900x-review/', views.amd_ryzen_9_5900x_review , name="amd-ryzen-9-5900x-review"),

    
    #-------------------------------------knowledge base------------------------------------------------------
    path('knowledge-base/', views.knowledge_base , name="knowledge-base"),
    path('knowledge-base/pc-building-tips/', views.pc_building_tips , name="pc-building-tips"),
    path('knowledge-base/pc-knowledge/', views.pc_knowledge , name="pc-knowledge"),
    path('knowledge-base/gaming-knowledge/', views.gaming_knowledge , name="gaming-knowledge"),
    path('knowledge-base/pc-building-tips/top-15-mistakes-every-new-pc-builder-makes/', views.mistakes_new_pc_builder_make , name="top-15-mistakes-every-new-pc-builder-makes"),
    path('knowledge-base/pc-building-tips/common-asked-questions-about-pc-building/', views.common_asked_questions_about_pc_building , name="common-asked-questions-about-pc-building"),
    path('knowledge-base/pc-building-tips/prebuilt-vs-custom-pc/', views.prebuilt_vs_custom_pc , name="prebuilt-vs-custom-pc"),
    path('knowledge-base/pc-building-tips/the-12-best-custom-pc-builder-websites/', views.custom_pc_builder_websites , name="the-12-best-custom-pc-builder-websites"),
    path('knowledge-base/gaming-knowledge/what-is-a-good-fps-for-gaming/', views.what_is_a_good_fps_for_gaming , name="what-is-a-good-fps-for-gaming"),
    
    #--------------------------------------------News----------------------------------------------------------
    path('news/', views.news , name="news"),
        
    #-----------------------------------------pc builds--------------------------------------------------------
    #-----------------category---------------------
    path('pc-builds/', views.pc_builds , name="pc-builds"),
    #----------------sub categories-----------------
    path('pc-builds/budget-pc-builds/', views.budget_pc_builds , name="budget-pc-builds"),
    path('pc-builds/mid-range-pc-builds/', views.mid_range_pc_builds , name="mid-range-pc-builds"),
    path('pc-builds/high-end-pc-builds/', views.high_end_pc_builds , name="high-end-pc-builds"),
    #-----------------reviews-----------------------
    path('pc-builds/budget-pc-builds/best-gaming-pc-under-300-usd-in-2024/', views.pc_under_300 , name="best-gaming-pc-under-300-usd-in-2024"),
    path('pc-builds/budget-pc-builds/best-gaming-pc-under-400-usd-in-2024/', views.pc_under_400 , name="best-gaming-pc-under-400-usd-in-2024"),
    path('pc-builds/budget-pc-builds/best-gaming-pc-under-500-usd-in-2024/', views.pc_under_500 , name="best-gaming-pc-under-500-usd-in-2024"),
    path('pc-builds/budget-pc-builds/best-gaming-pc-under-600-usd-in-2024/', views.pc_under_600 , name="best-gaming-pc-under-600-usd-in-2024"),
    
    path('pc-builds/mid-range-pc-builds/best-gaming-pc-under-700-usd-in-2024/', views.pc_under_700 , name="best-gaming-pc-under-700-usd-in-2024"),
    path('pc-builds/mid-range-pc-builds/best-gaming-pc-under-800-usd-in-2024/', views.pc_under_800 , name="best-gaming-pc-under-800-usd-in-2024"),
    path('pc-builds/mid-range-pc-builds/best-gaming-pc-under-1000-usd-in-2024/', views.pc_under_1000 , name="best-gaming-pc-under-1000-usd-in-2024"),
    path('pc-builds/mid-range-pc-builds/best-gaming-pc-under-1200-usd-in-2024/', views.pc_under_1200 , name="best-gaming-pc-under-1200-usd-in-2024"),
    
    path('pc-builds/high-end-pc-builds/best-gaming-pc-under-1500-usd-in-2024/', views.pc_under_1500 , name="best-gaming-pc-under-1500-usd-in-2024"),
    path('pc-builds/high-end-pc-builds/best-gaming-pc-under-2000-usd-in-2024/', views.pc_under_2000 , name="best-gaming-pc-under-2000-usd-in-2024"),
    path('pc-builds/high-end-pc-builds/best-gaming-pc-under-3000-usd-in-2024/', views.pc_under_3000 , name="best-gaming-pc-under-3000-usd-in-2024"),
    path('pc-builds/high-end-pc-builds/best-gaming-pc-under-4000-usd-in-2024/', views.pc_under_4000 , name="best-gaming-pc-under-4000-usd-in-2024"),
    path('pc-builds/high-end-pc-builds/best-gaming-pc-under-5000-usd-in-2024/', views.pc_under_5000 , name="best-gaming-pc-under-5000-usd-in-2024"),



#-----------------------------------------buying guides--------------------------------------------------------

# --------------------------------------category-----------------------------------------
path('buying-guide/', views.buying_guide , name="buying-guide"),

path('buying-guide/gaming-peripherals/', views.gaming_peripherals_buying_guide , name="gaming-peripherals-buying-guide"),
path('buying-guide/pc-components/', views.pc_components_buying_guide , name="pc-components-buying-guide"),
path('buying-guide/gaming-laptops/', views.gaming_laptops_buying_guide , name="gaming-laptops-buying-guide"),

# --------------sub categories-----------
path('buying-guide/gaming-peripherals/mouses/', views.mouse_buying_guide , name="mouse-buying-guide"),
path('buying-guide/gaming-peripherals/keyboards/', views.keyboard_buying_guide , name="keyboards-buying-guide"),
path('buying-guide/gaming-peripherals/headsets/', views.headset_buying_guide , name="headsets-buying-guide"),
path('buying-guide/gaming-peripherals/mouse-pads/', views.mouse_pad_buying_guide , name="mouse-pads-buying-guide"),
path('buying-guide/gaming-peripherals/monitors/', views.monitor_buying_guide , name="monitors-buying-guide"),
path('buying-guide/gaming-peripherals/chairs/', views.chair_buying_guide , name="chairs-buying-guide"),

path('buying-guide/gaming-peripherals/mouse/the-best-gaming-logitech-mouse-in-2024/', views.best_logitech_mouse , name="the-best-gaming-logitech-mouse-in-2024"),
path('buying-guide/gaming-peripherals/mouse/the-best-gaming-razer-mouse-in-2024/', views.best_razer_mouse , name="the-best-gaming-razer-mouse-in-2024"),
]
