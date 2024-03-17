/*!
* Start Bootstrap - Blog Home v5.0.9 (https://startbootstrap.com/template/blog-home)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-blog-home/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


let prevScrollPos = window.pageYOffset;
let isScrollingUp = false;
const offset = 100; // Adjust this value to set the offset
const buffer = -30; // Adjust this value to set the buffer distance

window.onscroll = function() {
    const currentScrollPos = window.pageYOffset;
    const navbar = document.getElementById("navbar");
    const toc = document.getElementById("toc");

    // Check if the "toc" element exists on the page
    if (toc) {
        const sticky = toc.offsetTop + navbar.offsetHeight - offset;
        const topBuffer = toc.offsetTop - buffer;
        // toc.style.marginTop = "0px";

        if (prevScrollPos > currentScrollPos) {
            isScrollingUp = true;
            navbar.style.top = "0";
            toc.style.marginTop = "93px";
        } else {
            isScrollingUp = false;
            navbar.style.top = `-${navbar.offsetHeight}px`;
            toc.style.marginTop = "1px";
        }

        if (currentScrollPos >= sticky) {
            toc.classList.add("sticky");
        } else {
            if (!isScrollingUp && currentScrollPos > topBuffer) {
                // Remove "sticky" class only when scrolling up and within buffer distance from the top
                toc.style.marginTop = "-300px";
                toc.classList.remove("sticky");
                
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
    img.style.transform = 'scale(1.05)';
}

function unzoomImage(card) {
    var img = card.querySelector('.card-img-top');
    img.style.transform = 'scale(1)';
}

