//============= Fixed Header Script ============== //
document.addEventListener("DOMContentLoaded", function () {
    window.addEventListener("scroll", function () {
        const header = document.getElementById("sticky-header");
        if (window.scrollY > 100) {
            header.style.top = "0px";
            header.style.backgroundColor = "#000F24";
        } else {
            header.style.top = "1.5rem";
            header.style.backgroundColor = "transparent";
        }

    });
});


//============= Page Loader Script ============== //
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
        document.getElementById("loader").style.display = "none";
    }, 800);
});


//============= // Scroll to Top Button Script  ============== //

const scrollToTopBtn = document.getElementById("scrollToTopBtn");

window.addEventListener("scroll", () => {
    if (window.scrollY > 200) {
        scrollToTopBtn.classList.remove("opacity-0");
        scrollToTopBtn.classList.add("opacity-100");
    } else {
        scrollToTopBtn.classList.remove("opacity-100");
        scrollToTopBtn.classList.add("opacity-0");
    }
});

scrollToTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});


//============= Checkout  slider Script ============== //
document.addEventListener("DOMContentLoaded", function () {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: "auto",
        spaceBetween: 20,
        centeredSlides: true,
        loop: true,
        effect: "coverflow",
        coverflowEffect: {
            rotate: 0,
            stretch: 0,
            depth: 150,
            modifier: 1.2,
            slideShadows: false,
        },
        navigation: {
            nextEl: ".event-button-next",
            prevEl: ".event-button-prev",
        },
        pagination: {
            el: ".custom-pagination",
            clickable: true,
        },
        breakpoints: {
            640: { slidesPerView: 1, spaceBetween: 15 },
            768: { slidesPerView: 2, spaceBetween: 20 },
            1024: { slidesPerView: 3, spaceBetween: 30 },
        },
    });
});


//============= Testimonial  slider Script ============== //
document.addEventListener("DOMContentLoaded", function () {
    var swiper = new Swiper(".customerSwiper", {
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        autoplay: true,
        pagination: {
            el: ".custom-pagination2",
            clickable: true,
        },
        breakpoints: {
            768: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            }
        }
    });
});


//============= Accordain  Script ============== //
document.querySelectorAll('.toggle-btn').forEach(button => {
    button.addEventListener('click', () => {
        const content = button.nextElementSibling;
        const icon = button.querySelector('span');


        document.querySelectorAll('.accordion-content').forEach(item => {
            if (item !== content) {
                item.style.maxHeight = null;
                item.style.paddingBottom = "0px";
                item.previousElementSibling.querySelector('span').textContent = '+';
            }
        });


        if (content.style.maxHeight) {
            content.style.maxHeight = null;
            content.style.paddingBottom = "0px";
            icon.textContent = '+';
        } else {
            content.style.maxHeight = content.scrollHeight + "px";
            content.style.paddingBottom = "16px";
            icon.textContent = '×';
        }
    });
});