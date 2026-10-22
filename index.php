<!DOCTYPE html>
<html lang="en">

<head>
    <!-- ========== Meta Tags ========== -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">

    <!-- ========== Page Title ========== -->
    <title>SLN Consulting Solution For Seamless Growth</title>

    <!-- slider  -->
    <link rel="stylesheet" type="text/css"
        href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css" />
    <link rel="stylesheet" type="text/css"
        href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.min.css" />

    <!-- ========== Favicon Icon ========== -->
    <link rel="shortcut icon" href="assets/img/sln-img/logo2.png" type="image/x-icon">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css"
        integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />

    <!-- ========== Start Stylesheet ========== -->
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/css/font-awesome.min.css" rel="stylesheet">
    <link href="assets/css/themify-icons.css" rel="stylesheet">
    <link href="assets/css/elegant-icons.css" rel="stylesheet">
    <link href="assets/css/flaticon-set.css" rel="stylesheet">
    <link href="assets/css/magnific-popup.css" rel="stylesheet">
    <link href="assets/css/swiper-bundle.min.css" rel="stylesheet">
    <link href="assets/css/animate.css" rel="stylesheet">
    <link href="assets/css/validnavs.css" rel="stylesheet">
    <link href="assets/css/helper.css" rel="stylesheet">
    <link href="assets/css/unit-test.css" rel="stylesheet">
    <link href="assets/css/style.css" rel="stylesheet">
    <link href="style.css" rel="stylesheet">
    <!-- ========== End Stylesheet ========== -->
    <style>
    .slick-dots {
        bottom: 4px;
    }

    .slick-dots li button:before {
        font-size: 15px;
        opacity: 1.25;
        color: #fff;
    }

    .slick-dots li.slick-active button:before {
        opacity: .75;
        color: #0035ff;
    }

    .slick-dotted.slick-slider {
        margin-bottom: 0px;
    }

    .banner-style-four .content {
        cursor: pointer;
    }

    html, body {
        overflow-x: hidden;
    }

    @media screen and (max-width: 1023px) {
        .width-ph {
            max-width: 100% !important;
            width: 100% !important;
        }
    }

    .slider {
        width: 100%;
        position: relative;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #ffffff;
    }

    /* On desktop (>=1024px), navbar is fixed/absolute (~108px height), so provide clean top clearance */
    @media screen and (min-width: 1024px) {
        .slider {
            padding-top: 110px;
        }
    }

    /* On tablet/mobile (<1024px), navbar is relative in document flow, so no top padding needed */
    @media screen and (max-width: 1023px) {
        .slider {
            padding-top: 0;
        }
    }

    .slider .mtop-1 {
        margin-top: 0 !important;
    }

    .mySwiper, .swiper {
        width: 100%;
        position: relative;
        overflow: hidden;
    }

    .mySwiper .swiper-wrapper {
        width: 100%;
        height: auto;
    }

    .mySwiper .swiper-slide {
        width: 100%;
        height: auto;
        display: flex;
        justify-content: center;
        align-items: center;
        background-color: #ffffff !important;
    }

    .mySwiper .swiper-slide img {
        width: 100%;
        height: auto;
        display: block;
        cursor: pointer;
    }

    /* Slide-specific sizing for Images 6 & 7 ONLY (Slides 1-5 and 8 remain 100% full width) */
    .mySwiper .swiper-slide.slide-compact {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        text-align: center !important;
        background-color: #ffffff !important;
        overflow: hidden;
    }

    .mySwiper .swiper-slide.slide-compact img,
    .mySwiper .swiper-slide img.slider-image-compact,
    .mySwiper .swiper-slide #banner-vapt,
    .mySwiper .swiper-slide #banner-cybersecurity-internship {
        width: 76.2% !important;
        max-width: 76.2% !important;
        height: auto !important;
        margin-left: auto !important;
        margin-right: auto !important;
        display: block !important;
        object-fit: contain;
    }

    /* Swiper Navigation Circular Chevron Controls */
    .mySwiper .swiper-button-prev,
    .mySwiper .swiper-button-next {
        position: absolute;
        top: 50% !important;
        transform: translateY(-50%) !important;
        width: 48px !important;
        height: 48px !important;
        background: #ffffff !important;
        color: #013df5 !important;
        border: 1.5px solid rgba(1, 61, 245, 0.25) !important;
        border-radius: 50% !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.22), 0 2px 6px rgba(1, 61, 245, 0.12) !important;
        z-index: 30 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        cursor: pointer !important;
        pointer-events: auto !important;
        outline: none !important;
        padding: 0 !important;
        margin: 0 !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
    }

    /* Suppress default Swiper pseudo-element text */
    .mySwiper .swiper-button-prev:after,
    .mySwiper .swiper-button-next:after {
        display: none !important;
        content: '' !important;
    }

    /* Chevron icon inside button */
    .mySwiper .swiper-button-prev i,
    .mySwiper .swiper-button-next i {
        font-size: 18px !important;
        color: #013df5 !important;
        line-height: 1 !important;
        display: block !important;
        pointer-events: none !important;
        transition: color 0.25s ease, transform 0.25s ease !important;
    }

    /* Optical center adjustment for chevron glyphs */
    .mySwiper .swiper-button-prev i {
        transform: translateX(-1px);
    }

    .mySwiper .swiper-button-next i {
        transform: translateX(1px);
    }

    .mySwiper .swiper-button-prev {
        left: 24px !important;
        right: auto !important;
    }

    .mySwiper .swiper-button-next {
        right: 24px !important;
        left: auto !important;
    }

    /* Hover and focus states with website theme blue */
    .mySwiper .swiper-button-prev:hover,
    .mySwiper .swiper-button-next:hover,
    .mySwiper .swiper-button-prev:focus-visible,
    .mySwiper .swiper-button-next:focus-visible {
        background: #013df5 !important;
        color: #ffffff !important;
        border-color: #013df5 !important;
        box-shadow: 0 6px 22px rgba(1, 61, 245, 0.45), 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        transform: translateY(-50%) scale(1.08) !important;
    }

    .mySwiper .swiper-button-prev:hover i,
    .mySwiper .swiper-button-next:hover i,
    .mySwiper .swiper-button-prev:focus-visible i,
    .mySwiper .swiper-button-next:focus-visible i {
        color: #ffffff !important;
    }

    .mySwiper .swiper-button-prev:active,
    .mySwiper .swiper-button-next:active {
        transform: translateY(-50%) scale(0.96) !important;
    }

    .mySwiper .swiper-pagination {
        bottom: 14px !important;
        z-index: 10;
    }

    .mySwiper .swiper-pagination-bullet {
        width: 12px;
        height: 12px;
        background: #ffffff;
        opacity: 0.75;
        margin: 0 5px !important;
        transition: all 0.3s ease;
    }

    .mySwiper .swiper-pagination-bullet-active {
        background: #013df5 !important;
        opacity: 1 !important;
        width: 28px !important;
        border-radius: 6px !important;
    }

    @media screen and (max-width: 1023px) {
        .mySwiper .swiper-button-prev,
        .mySwiper .swiper-button-next {
            width: 42px !important;
            height: 42px !important;
        }
        .mySwiper .swiper-button-prev {
            left: 16px !important;
        }
        .mySwiper .swiper-button-next {
            right: 16px !important;
        }
        .mySwiper .swiper-button-prev i,
        .mySwiper .swiper-button-next i {
            font-size: 16px !important;
        }
    }

    @media screen and (max-width: 767px) {
        .mySwiper .swiper-button-prev,
        .mySwiper .swiper-button-next {
            width: 36px !important;
            height: 36px !important;
        }
        .mySwiper .swiper-button-prev {
            left: 8px !important;
        }
        .mySwiper .swiper-button-next {
            right: 8px !important;
        }
        .mySwiper .swiper-button-prev i,
        .mySwiper .swiper-button-next i {
            font-size: 14px !important;
        }
        #back-col.about-style-one-area.default-padding-5 {
            padding-top: 40px;
            padding-bottom: 40px;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        .mySwiper .swiper-slide,
        .mySwiper .swiper-wrapper {
            transition-duration: 0ms !important;
        }
    }
    </style>


</head>

<body>


    <!-- Header 
    ============================================= -->
    <?php include 'header.php'; ?>
    <!-- End Header -->

    <div class="slider">
        <div class="mtop-1">
            <div class="swiper mySwiper" id="slnHeroCarousel" aria-label="SLN Consulting Banner Carousel">
                <div class="swiper-wrapper">
                    <!-- 1. Empowering Minds -->
                    <div class="swiper-slide">
                        <img id="banner1" src="./assets/img/sln-img/slk-banner1.jpg" alt="Empowering Minds, Elevating Skills, Innovative Solutions." data-href="./index.php">
                    </div>

                    <!-- 2. Training & Certification -->
                    <div class="swiper-slide">
                        <img id="banner-training" src="./assets/img/sln-img/slk-banner11.jpg" alt="Training &amp; Certification" data-href="./ecc.php">
                    </div>

                    <!-- 3. Certifications (ISC2) -->
                    <div class="swiper-slide">
                        <img id="banner6" src="./assets/img/sln-img/slk-banner6.jpg" alt="Certifications (ISC2)" data-href="./isc2.php">
                    </div>

                    <!-- 4. Cambridge University -->
                    <div class="swiper-slide">
                        <img id="banner2" src="./assets/img/sln-img/slk-banner2.jpg" alt="Cambridge University" data-href="./cambridge.php">
                    </div>

                    <!-- 5. SOC -->
                    <div class="swiper-slide">
                        <img id="banner-soc" src="./assets/img/sln-img/slk-banner7.jpg" alt="Security Operation Center - SOC As A Service" data-href="./soc.php">
                    </div>

                    <!-- 6. VAPT -->
                    <div class="swiper-slide slide-compact slide-vapt">
                        <img id="banner-vapt" class="slider-image-compact" src="./assets/img/sln-img/vapt-banner.jpg" alt="Vulnerability Assessment &amp; Penetration Testing (VAPT)" data-href="./vapt.php">
                    </div>

                    <!-- 7. Internship -->
                    <div class="swiper-slide slide-compact slide-internship">
                        <img id="banner-cybersecurity-internship" class="slider-image-compact" src="./assets/img/sln-img/cybersecurity-internship-3-month.png" alt="Cybersecurity Internship" data-href="./cybersecurity-internship.php">
                    </div>

                    <!-- 8. Skilling Solution -->
                    <div class="swiper-slide">
                        <img id="banner5" src="./assets/img/sln-img/slk-banner5.jpg" alt="Skilling Solution" data-href="./enterprises.php">
                    </div>
                </div>

                <!-- Swiper Navigation Controls (Circular Left & Right Arrow Buttons) -->
                <button type="button" class="swiper-button-prev" id="heroSliderPrev" aria-label="Previous slide">
                    <i class="fa-solid fa-chevron-left" aria-hidden="true"></i>
                </button>
                <button type="button" class="swiper-button-next" id="heroSliderNext" aria-label="Next slide">
                    <i class="fa-solid fa-chevron-right" aria-hidden="true"></i>
                </button>

                <!-- Swiper Pagination -->
                <div class="swiper-pagination"></div>
            </div>
        </div>

    </div>



    <!-- Start About 
    ============================================= -->
    <div id="back-col" class="about-style-one-area default-padding-5">
        <div class="shape-animated-left">
            <!-- <img src="assets/img/shape/anim-1.png" alt="Image Not Found">
            <img src="assets/img/shape/anim-2.png" alt="Image Not Found"> -->
        </div>
        <div class="container">
            <div class="row">
                <div class="about-style-one col-xl-6 col-lg-5 col-sm-12">
                    <!-- <div class="h4 sub-heading">ABout SLN Consulting</div> -->
                    <h4 style="font-size: 29px;" class="sub-heading secondary h4-col "> <a href="nure-campus.php">About
                            SLN Consulting</a></h4>
                    <!-- <h2 class="title mb-25">Finance Consulting for Challenging Times</h2> -->
                    <p style="font-size: 19px;     text-align: justify;">
                        Established in 2022, SLN Consulting specializes in seamlessly integrating and optimizing diverse
                        systems and technologies to enhance operatonal efficiency. <br>
                        <br>Founded by few industry veterans, each
                        having minimum of three decades of experience in busiress development, management consulting,
                        technology integration, capacity building, and training. They have played a pivotal role in
                        facilitating
                        the growth of startups, particulary in the learning and development domain, while also
                        spearheading
                        initiatives in cybersecurity, software development, content creation and application testing,
                        workforce
                        training and upskilling.

                    </p>

                    <div class=" width-ph mt-30 ">
                        <div class="default-feature-item5 default-feature-item ">
                            <a href="#">
                                <i class="fa-solid fa-screwdriver-wrench "></i>
                                <h4 style="font-size: 16px;">Customer-centric<br> Solutions</h4>
                            </a>
                        </div>
                        <div class="default-feature-item5 default-feature-item ">
                            <a href="#">
                                <i class="fa-solid fa-person-circle-check"></i>
                                <h4 style="font-size: 16px;">Timely<br>Recommendations</h4>
                            </a>
                        </div>
                        <div class="default-feature-item5 default-feature-item ">
                            <a href="#">
                                <i class="fa-solid fa-handshake"></i>
                                <h4 style="font-size: 16px;">Partnershipes with <br>Leading OEMs</h4>
                            </a>
                        </div>
                    </div>
                    <div class="new-btn">
                        <button><a href="about-us.php"> Read more</a></button>
                    </div>

                </div>
                <div class="about-style-one col-xl-5 offset-xl-1 col-lg-6 col-sm-12 offset-lg-1">
                    <div class="about-thumb">
                        <img class="wow fadeInRight" src="assets/img/sln-img/abt-4.png" alt="Image Not Found"
                            style="visibility: visible; animation-name: fadeInRight;">
                        <!-- <div class="about-card wow fadeInUp" data-wow-delay="500ms" style="visibility: visible; animation-delay: 500ms; animation-name: fadeInUp;">
                            <ul>
                                <li>
                                    <div class="icon">
                                        <i class="flaticon-license"></i>
                                    </div>
                                    <div class="fun-fact">
                                        <div class="counter">
                                            <div class="timer" data-to="98" data-speed="2000">98</div>
                                            <div class="operator">%</div>
                                        </div>
                                        <span class="medium">Consulting Success</span>
                                    </div>
                                </li>
                                <li>
                                    <div class="icon">
                                        <i class="flaticon-global"></i>
                                    </div>
                                    <div class="fun-fact">
                                        <div class="counter">
                                            <div class="timer" data-to="120" data-speed="2000">120</div>
                                            <div class="operator">+</div>
                                        </div>
                                        <span class="medium">Worldwide Clients</span>
                                    </div>
                                </li>
                            </ul>
                        </div> -->
                        <div class="thumb-shape-bottom wow fadeInDown" data-wow-delay="300ms"
                            style="visibility: visible; animation-delay: 300ms; animation-name: fadeInDown;">
                            <!-- <img src="assets/img/shape/anim-3.png" alt="Image Not Found">
                            <img src="assets/img/shape/anim-4.png" alt="Image Not Found"> -->
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <!-- End About -->





    <!-- Start Partner Area  
    ============================================= -->
    <div id="clint-bg" class="partner-style-one-area default-padding">
        <div class="container">

            <div class="col-lg-12">
                <div class="partner-map text-center">
                 <h4 style="font-size: 24px; color:blue;">Authorised Distributor</h4><br>
                    <h4>Cambridge University Press & Assessment</h4><br><br>
                </div>
            </div>

            <div class="col-lg-12 mb-2">
                <div class="partner-map text-center">
                     <h4 style="font-size: 24px; color:blue;">ISC2 Official Training Partner
                    </h4> <br>
                    <h4>CC, CCSP, CISSP, CSSLP</h4><br><br>
                </div>
            </div>

            <div class="col-lg-12 mb-2">
                <div class="partner-map text-center">
                    <h4 style="font-size: 24px; color:blue;">Authorised Training Centre (ATC) of EC-Council</h4><br>
                    <h4>CEH / CND / CHFI / CPENT / CASE / CCSE / CTIA / CSA</h4><br><br>
                </div>
            </div>

            <div class="col-lg-12 mb-2">
                <div class="partner-map text-center">
                    <h4 style="font-size: 24px; color:blue;">Technology Partner—BCBUZZ Technologies</h4><br>
                    <h4>Campus Internship | VAPT | SOC-As-A-Service</h4>
                </div>
            </div>


        </div>
    </div>
    <!-- End Partner Area -->

    <!-- Start Testimonials 
    ============================================= -->
    <!-- <div class="testimonial-style-one-area default-padding">
        <div class="container">
            <div class="row align-center">

                <div class="col-lg-4">
                    <div class="testimonial-thumb">
                        <div class="thumb-item">
                            <img src="assets/img/illustration/5.png" alt="illustration">
                            <div class="mini-shape">
                                <img src="assets/img/shape/19.png" alt="illustration">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-7 offset-lg-1">
                    <div class="testimonial-carousel swiper">
                  
                        <div class="swiper-wrapper">
               
                            <div class="swiper-slide">
                                <div class="testimonial-style-one">

                                    <div class="item">
                                        <div class="content">
                                            <div class="rating">
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                            </div>
                                            <h2>The best service ever</h2>
                                            <p>
                                                “Targetingconsultation discover apartments. ndulgence off under folly death wrote cause her way spite. Plan upon yet way get cold spot its week. Almost do am or limits hearts. Resolve parties but why she shewing. She sang know now always remembering to the point.”
                                            </p>
                                        </div>
                                        <div class="provider">
                                            <i class="flaticon-quote"></i>
                                            <div class="info">
                                                <h4>Matthew J. Wyman</h4>
                                                <span>Senior Consultant</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        
                            <div class="swiper-slide">
                                <div class="testimonial-style-one">
                                    <div class="item">
                                        <div class="content">
                                            <div class="rating">
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                                <i class="fas fa-star"></i>
                                            </div>
                                            <h2>Awesome Business opportunities</h2>
                                            <p>
                                                “Consultation discover apartments. ndulgence off under folly death wrote cause her way spite. Plan upon yet way get cold spot its week. Almost do am or limits hearts. Resolve parties but why she shewing. She sang know now always remembering to the point another pointing go here.”
                                            </p>
                                        </div>
                                        <div class="provider">
                                            <i class="flaticon-quote"></i>
                                            <div class="info">
                                                <h4>Anthom Bu Spar</h4>
                                                <span>Marketing Manager</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                    
                        </div>

                    </div>
                </div>

            </div>
        </div>
    </div> -->
    <!-- End Testimonails  -->








    <?php include "footer.php" ?>









    <!-- jQuery Frameworks
    ============================================= -->
    <script src="assets/js/jquery-3.6.0.min.js"></script>
    <script src="assets/js/bootstrap.bundle.min.js"></script>
    <script src="assets/js/jquery.appear.js"></script>
    <script src="assets/js/jquery.easing.min.js"></script>
    <script src="assets/js/jquery.magnific-popup.min.js"></script>
    <script src="assets/js/modernizr.custom.13711.js"></script>
    <script src="assets/js/swiper-bundle.min.js"></script>
    <script src="assets/js/wow.min.js"></script>
    <script src="assets/js/progress-bar.min.js"></script>
    <script src="assets/js/circle-progress.js"></script>
    <script src="assets/js/isotope.pkgd.min.js"></script>
    <script src="assets/js/imagesloaded.pkgd.min.js"></script>
    <script src="assets/js/jquery.nice-select.min.js"></script>
    <script src="assets/js/count-to.js"></script>
    <script src="assets/js/jquery.scrolla.min.js"></script>
    <script src="assets/js/YTPlayer.min.js"></script>
    <script src="assets/js/TweenMax.min.js"></script>
    <script src="assets/js/rangeSlider.min.js"></script>
    <script src="assets/js/jquery-ui.min.js"></script>
    <script src="assets/js/validnavs.js"></script>
    <script src="assets/js/main.js"></script>

    <!-- Hero Banner Swiper Carousel Initialization -->
    <script>
    (function() {
        var prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        var swiperOptions = {
            loop: true,
            autoHeight: true,
            updateOnImagesReady: true,
            observer: true,
            observeParents: true,
            speed: prefersReducedMotion ? 0 : 800,
            grabCursor: true,
            keyboard: {
                enabled: true
            },
            pagination: {
                el: '.mySwiper .swiper-pagination',
                clickable: true
            },
            navigation: {
                nextEl: '.mySwiper .swiper-button-next',
                prevEl: '.mySwiper .swiper-button-prev'
            },
            breakpoints: {
                320: {
                    slidesPerView: 1,
                    spaceBetween: 0
                },
                768: {
                    slidesPerView: 1,
                    spaceBetween: 0
                },
                1024: {
                    slidesPerView: 1,
                    spaceBetween: 0
                }
            }
        };

        if (!prefersReducedMotion) {
            swiperOptions.autoplay = {
                delay: 4000, // Exactly 4 seconds per slide
                disableOnInteraction: false,
                pauseOnMouseEnter: false,
                waitForTransition: true
            };
        } else {
            swiperOptions.autoplay = false;
        }

        function initHeroSwiper() {
            if (typeof Swiper === 'undefined') {
                setTimeout(initHeroSwiper, 50);
                return;
            }

            // Prevent multiple timers or duplicate initializations
            if (window.slnHeroSwiper && typeof window.slnHeroSwiper.destroy === 'function') {
                window.slnHeroSwiper.destroy(true, true);
            }

            var heroSwiper = new Swiper('.mySwiper', swiperOptions);
            window.slnHeroSwiper = heroSwiper;

            // Direct button listeners for instant, robust navigation and wrapping
            var prevBtn = document.getElementById('heroSliderPrev') || document.querySelector('.mySwiper .swiper-button-prev');
            var nextBtn = document.getElementById('heroSliderNext') || document.querySelector('.mySwiper .swiper-button-next');

            if (prevBtn) {
                prevBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    heroSwiper.slidePrev();
                    if (!prefersReducedMotion && heroSwiper.autoplay && !heroSwiper.autoplay.running) {
                        heroSwiper.autoplay.start();
                    }
                });
            }

            if (nextBtn) {
                nextBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    e.stopPropagation();
                    heroSwiper.slideNext();
                    if (!prefersReducedMotion && heroSwiper.autoplay && !heroSwiper.autoplay.running) {
                        heroSwiper.autoplay.start();
                    }
                });
            }

            // Explicitly start autoplay if enabled
            if (!prefersReducedMotion && heroSwiper.autoplay) {
                heroSwiper.autoplay.start();
            }

            // Ensure autoplay continues smoothly after manual clicks or slide changes
            heroSwiper.on('slideChangeTransitionEnd', function() {
                if (!prefersReducedMotion && heroSwiper.autoplay && !heroSwiper.autoplay.running) {
                    heroSwiper.autoplay.start();
                }
            });

            // Handle tab visibility changes (pause when hidden, resume when visible)
            document.addEventListener('visibilitychange', function() {
                if (!heroSwiper || !heroSwiper.autoplay) return;
                if (document.hidden) {
                    if (heroSwiper.autoplay.running) {
                        heroSwiper.autoplay.stop();
                    }
                } else if (!prefersReducedMotion) {
                    heroSwiper.autoplay.start();
                }
            });

            // Resume autoplay on window focus
            window.addEventListener('focus', function() {
                if (!prefersReducedMotion && heroSwiper && heroSwiper.autoplay && !heroSwiper.autoplay.running) {
                    heroSwiper.autoplay.start();
                }
            });

            // Reduced motion media query change listener
            if (window.matchMedia) {
                var motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
                if (motionQuery.addEventListener) {
                    motionQuery.addEventListener('change', function(e) {
                        prefersReducedMotion = e.matches;
                        if (e.matches) {
                            if (heroSwiper.autoplay && heroSwiper.autoplay.running) {
                                heroSwiper.autoplay.stop();
                            }
                            heroSwiper.params.speed = 0;
                        } else {
                            heroSwiper.params.speed = 800;
                            if (heroSwiper.autoplay) {
                                heroSwiper.autoplay.start();
                            }
                        }
                    });
                }
            }
        }

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', initHeroSwiper);
        } else {
            initHeroSwiper();
        }

        window.addEventListener('load', function() {
            if (window.slnHeroSwiper) {
                if (typeof window.slnHeroSwiper.updateAutoHeight === 'function') {
                    window.slnHeroSwiper.updateAutoHeight(300);
                }
                window.slnHeroSwiper.update();
            }
        });

        // Delegated Banner Click Navigation (works reliably with cloned slides in loop mode)
        var swiperContainer = document.querySelector('.mySwiper');
        if (swiperContainer) {
            swiperContainer.addEventListener('click', function(e) {
                // Ignore clicks on navigation buttons or pagination bullets
                if (e.target.closest('.swiper-button-prev') || e.target.closest('.swiper-button-next') || e.target.closest('.swiper-pagination')) {
                    return;
                }

                var slide = e.target.closest('.swiper-slide');
                if (!slide) return;

                var img = slide.querySelector('img');
                if (!img) return;

                var targetHref = img.getAttribute('data-href');
                if (!targetHref) {
                    var idMap = {
                        'banner1': './index.php',
                        'banner-training': './ecc.php',
                        'banner6': './isc2.php',
                        'banner2': './cambridge.php',
                        'banner-soc': './soc.php',
                        'banner-vapt': './vapt.php',
                        'banner-cybersecurity-internship': './cybersecurity-internship.php',
                        'banner5': './enterprises.php'
                    };
                    targetHref = idMap[img.id];
                }

                if (targetHref) {
                    window.location.href = targetHref;
                }
            });
        }
    })();
    </script>
</body>



</html>