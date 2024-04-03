/*!
* Start Bootstrap - Blog Home v5.0.9 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


// Function to calculate the bottom boundary based on the position of a common element
function calculateBottomBoundary() {
    const commonElement = document.getElementById("relatedPosts"); // Replace "commonElement" with the actual ID of the common element
    if (!commonElement) {
        // Return a default value if the common element is not found
        return Infinity;
    }
    const rect = commonElement.getBoundingClientRect();
    const bottomBoundary = rect.top + window.pageYOffset - 200;
    return bottomBoundary;
}

let prevScrollPos = window.pageYOffset;
let isScrollingUp = false;
const offset = 100; // Adjust this value to set the offset
const buffer = -30; // Adjust this value to set the buffer distance
const bottomBoundary = 5000; // Adjust this value to set the bottom boundary

window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    const navbar = document.getElementById("navbar");
    const toc = document.getElementById("toc");
    const bottomBoundary = calculateBottomBoundary();
    // Check if the "toc" element exists on the page
    if (toc) {
        const sticky = toc.offsetTop + navbar.offsetHeight - offset;
        const topBuffer = toc.offsetTop - buffer;

        if (prevScrollPos > currentScrollPos) {
            isScrollingUp = true;
            navbar.style.top = "0";
            toc.style.marginTop = "93px";
        } else {
            isScrollingUp = false;
            navbar.style.top = `-${navbar.offsetHeight}px`;
            toc.style.marginTop = "1px";
        }

        if (currentScrollPos >= sticky && currentScrollPos < bottomBoundary) {
            toc.classList.add("sticky");
        } else {
            if (!isScrollingUp && currentScrollPos > topBuffer) {
                // Remove "sticky" class only when scrolling up and within buffer distance from the top
                toc.style.marginTop = "-300px";
                toc.classList.remove("sticky");
            } else if (currentScrollPos >= bottomBoundary && isScrollingUp) {
                // Keep toc sticky at current position when reaching bottom boundary and scrolling up
                toc.classList.add("sticky");
                toc.style.marginTop = `${bottomBoundary - currentScrollPos}px`;
            }
        }

        // Check if the scroll position is at the top (with buffer)
        if (currentScrollPos <= buffer) {
            toc.classList.remove("sticky");
        }
    } else {
        // If "toc" element doesn't exist, only handle the navigation bar scrolling
        if (prevScrollPos > currentScrollPos) {
            isScrollingUp = true;
            navbar.style.top = "0";
        } else {
            isScrollingUp = false;
            navbar.style.top = `-${navbar.offsetHeight}px`;
        }
    }

    prevScrollPos = currentScrollPos;
};



document.addEventListener("DOMContentLoaded", function () {
    // Smooth scrolling for internal links with an offset
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();

            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);

            if (targetElement) {
                const offset = 80; // Adjust this value to set the offset above the target element
                const targetPosition = targetElement.offsetTop - offset;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// serach functionality--------------------

function zoomImage(card) {
    var img = card.querySelector('.card-img-top');
    img.style.transform = 'scale(1.03)';
}

function unzoomImage(card) {
    var img = card.querySelector('.card-img-top');
    img.style.transform = 'scale(1)';
}


// footer   style changer---
function footerForNonPosts() {
    const currentPath = window.location.pathname;
    const specificPaths = [
        '/',
        '/privacy-policy/',
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
    ]; // Replace '/path1', '/path2' with your specific paths
    const element = document.getElementById('footer');
    if (specificPaths.includes(currentPath)) {
         // Replace 'yourElementId' with the actual ID of your element
        if (element) {
            // Apply specific styles to the element
            element.style.marginLeft = '0';
            element.style.marginRight = '0';
            // Add more styles as needed
        }
    }

    if (currentPath === '/contact/'){
        console.log('in')
        if (element) {
            // Apply specific styles to the element
            // element.style.marginLeft = '100px';
            // element.style.marginRight = '200px';
            element.style.marginTop = '350px';
            element.style.marginLeft = '-112px';
            element.style.marginRight = '-110px';
            element.style.left = '110px';
            element.style.right = '115px';
            element.style.position = "absolute";

            // Add more styles as needed
        }
    }
}


