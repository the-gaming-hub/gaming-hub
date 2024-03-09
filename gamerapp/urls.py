from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('search/<str:search>/', views.search, name='search'),
    path('coming-soon/', views.coming_soon, name='coming-soon'),
    
    
    
    path('reviews/', views.reviews , name="reviews"),
    #-------------------------------------gaming peripherals------------------------------------------------
    # -----------category-------------------
    path('reviews/gaming-peripherals-reviews/', views.gaming_peripherals_reviews , name="gaming-peripherals-reviews"),
    path('reviews/pc-components-reviews/', views.pc_components_reviews , name="pc-components-reviews"),
    path('reviews/gaming-laptops-reviews/', views.gaming_laptops_reviews , name="gaming-laptops-reviews"),
    # --------------sub categories-----------
    path('reviews/gaming-peripherals-reviews/mouse-reviews/', views.mouse_reviews , name="mouse-reviews"),
    path('reviews/gaming-peripherals-reviews/keyboards-reviews/', views.keyboard_reviews , name="keyboards-reviews"),
    path('reviews/gaming-peripherals-reviews/headsets-reviews/', views.headset_reviews , name="headsets-reviews"),
    path('reviews/gaming-peripherals-reviews/mouse-pads-reviews/', views.mouse_pad_reviews , name="mouse-pads-reviews"),
    path('reviews/gaming-peripherals-reviews/monitors-reviews/', views.monitor_reviews , name="monitors-reviews"),
    path('reviews/gaming-peripherals-reviews/gaming-chairs-reviews/', views.chair_reviews , name="gaming-chairs-reviews"),
    
    
    path('reviews/pc-components-reviews/cpu-reviews/', views.cpu_reviews , name="cpu-reviews"),
    path('reviews/pc-components-reviews/cpu-coolers-reviews/', views.cpu_cooler_reviews , name="cpu-coolers-reviews"),
    path('reviews/pc-components-reviews/gpu-reviews/', views.gpu_reviews , name="gpu-reviews"),
    path('reviews/pc-components-reviews/motherboards-reviews/', views.motherboard_reviews , name="motherboards-reviews"),
    path('reviews/pc-components-reviews/ram-reviews/', views.ram_reviews , name="ram-reviews"),
    path('reviews/pc-components-reviews/ssd-reviews/', views.ssd_reviews , name="ssd-reviews"),
    path('reviews/pc-components-reviews/psu-reviews/', views.psu_reviews , name="psu-reviews"),
    path('reviews/pc-components-reviews/cases-reviews/', views.case_reviews , name="cases-reviews"),
    #-----------------reviews------------------
                    # ----gaming peripheralss------------
    path('reviews/gaming-peripherals-reviews/mouse-reviews/logitech-g402-review-2024/', views.logitech_g402_review , name="logitech-g402-hyperion-fury-review-2024"),
    path('reviews/gaming-peripherals-reviews/mouse-reviews/logitech-g502-lightspeed-review-2024/', views.logitech_g502_review , name="logitech-g502-lightspeed-review-2024"),
    path('reviews/gaming-peripherals-reviews/mouse-reviews/finalmouse-ultralightx-mouse-review/', views.finalmouse_ultralightx_review , name="finalmouse-ultralightx-mouse-review"),
                    #-------- pc componentss-------------
    path('reviews/pc-components-reviews/cpu-reviews/amd-ryzen-9-5900x-review/', views.amd_ryzen_9_5900x_review , name="amd-ryzen-9-5900x-review"),

    
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

path('buying-guide/gaming-peripherals-buying-guides/', views.gaming_peripherals_buying_guide , name="gaming-peripherals-buying-guides"),
path('buying-guide/pc-components-buying-guides/', views.pc_components_buying_guide , name="pc-components-buying-guides"),
path('buying-guide/gaming-laptops-buying-guides/', views.gaming_laptops_buying_guide , name="gaming-laptops-buying-guides"),

# --------------sub categories-----------
path('buying-guide/gaming-peripherals-buying-guides/mouse-buying-guides/', views.mouse_buying_guide , name="mouse-buying-guides"),
path('buying-guide/gaming-peripherals-buying-guides/keyboards-buying-guides/', views.keyboard_buying_guide , name="keyboards-buying-guides"),
path('buying-guide/gaming-peripherals-buying-guides/headsets-buying-guides/', views.headset_buying_guide , name="headsets-buying-guides"),
path('buying-guide/gaming-peripherals-buying-guides/mouse-pads-buying-guides/', views.mouse_pad_buying_guide , name="mouse-pads-buying-guides"),
path('buying-guide/gaming-peripherals-buying-guides/monitors-buying-guides/', views.monitor_buying_guide , name="monitors-buying-guides"),
path('buying-guide/gaming-peripherals-buying-guides/gaming-chairs-buying-guides/', views.chair_buying_guide , name="gaming-chairs-buying-guides"),


path('buying-guide/pc-components-buying-guides/cpu-buying-guides/', views.cpu_buying_guide , name="cpu-buying-guides"),
path('buying-guide/pc-components-buying-guides/cpu-coolers-buying-guides/', views.cpu_cooler_buying_guide , name="cpu-coolers-buying-guides"),
path('buying-guide/pc-components-buying-guides/gpu-buying-guides/', views.gpu_buying_guide , name="gpu-buying-guides"),
path('buying-guide/pc-components-buying-guides/motherboards-buying-guides/', views.motherboard_buying_guide , name="motherboards-buying-guides"),
path('buying-guide/pc-components-buying-guides/ram-buying-guides/', views.ram_buying_guide , name="ram-buying-guides"),
path('buying-guide/pc-components-buying-guides/ssd-buying-guides/', views.ssd_buying_guide , name="ssd-buying-guides"),
path('buying-guide/pc-components-buying-guides/psu-buying-guides/', views.psu_buying_guide , name="psu-buying-guides"),
path('buying-guide/pc-components-buying-guides/cases-buying-guides/', views.case_buying_guide , name="cases-buying-guides"),

#-----------articles----------------
path('buying-guide/gaming-peripherals-buying-guides/mouse-buying-guides/the-best-gaming-logitech-mouse-in-2024/', views.best_logitech_mouse , name="the-best-gaming-logitech-mouse-in-2024"),
path('buying-guide/gaming-peripherals-buying-guides/mouse-buying-guides/the-best-gaming-razer-mouse-in-2024/', views.best_razer_mouse , name="the-best-gaming-razer-mouse-in-2024"),
]
