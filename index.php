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

    .slider, .mySwiper, .swiper, swiper-container {
        width: 100%;
        height: 100%;
        position: relative;
        overflow: hidden;
    }

    .swiper-slide, swiper-slide {
        text-align: center;
        font-size: 18px;
        background-color: #fff !important;
        display: flex;
        justify-content: center;
        align-items: center;
        overflow: hidden;
    }

    .swiper-slide img, swiper-slide img {
        display: block;
        width: 100%;
        height: 100vh;
        object-fit: cover;
        cursor: pointer;
    }

    /* Swiper Navigation & Pagination Controls */
    .mySwiper .swiper-button-prev,
    .mySwiper .swiper-button-next {
        color: #ffffff;
        background: rgba(0, 0, 0, 0.4);
        width: 44px;
        height: 44px;
        border-radius: 50%;
        transition: all 0.3s ease;
        z-index: 10;
    }

    .mySwiper .swiper-button-prev:after,
    .mySwiper .swiper-button-next:after {
        font-size: 18px;
        font-weight: bold;
    }

    .mySwiper .swiper-button-prev:hover,
    .mySwiper .swiper-button-next:hover {
        background: #013df5;
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

    @media screen and (max-width: 1024px) {
        .swiper-slide img, swiper-slide img {
            height: 73vh;
        }
    }

    @media screen and (max-width: 768px) {
        .swiper-slide img, swiper-slide img {
            height: 38vh;
        }
        .mySwiper .swiper-button-prev,
        .mySwiper .swiper-button-next {
            width: 32px;
            height: 32px;
        }
        .mySwiper .swiper-button-prev:after,
        .mySwiper .swiper-button-next:after {
            font-size: 13px;
        }
    }

    @media screen and (max-width: 820px) {
        .swiper-slide img, swiper-slide img {
            height: 35vh;
        }
    }

    @media only screen and (max-width: 600px) {
        .swiper-slide img, swiper-slide img {
            display: block;
            width: 100%;
            height: 24vh;
            object-fit: cover;
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


    <br>


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
                    <div class="swiper-slide">
                        <img id="banner-vapt" src="./assets/img/sln-img/vapt-banner.jpg" alt="Vulnerability Assessment &amp; Penetration Testing (VAPT)" data-href="./vapt.php">
                    </div>

                    <!-- 7. Internship -->
                    <div class="swiper-slide">
                        <img id="banner-cybersecurity-internship" src="./assets/img/sln-img/cybersecurity-internship-3-month.png" alt="Cybersecurity Internship" data-href="./cybersecurity-internship.php">
                    </div>

                    <!-- 8. Skilling Solution -->
                    <div class="swiper-slide">
                        <img id="banner5" src="./assets/img/sln-img/slk-banner5.jpg" alt="Skilling Solution" data-href="./enterprises.php">
                    </div>
                </div>

                <!-- Swiper Navigation Controls -->
                <div class="swiper-button-prev" aria-label="Previous slide"></div>
                <div class="swiper-button-next" aria-label="Next slide"></div>

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
                delay: 4500, // 4.5 seconds per slide (Requirement: 4-5 seconds)
                disableOnInteraction: false,
                pauseOnMouseEnter: true
            };
        } else {
            swiperOptions.autoplay = false;
        }

        function initHeroSwiper() {
            if (typeof Swiper === 'undefined') {
                setTimeout(initHeroSwiper, 50);
                return;
            }

            // Prevent multiple initializations
            if (window.slnHeroSwiper && typeof window.slnHeroSwiper.destroy === 'function') {
                window.slnHeroSwiper.destroy(true, true);
            }

            var heroSwiper = new Swiper('.mySwiper', swiperOptions);
            window.slnHeroSwiper = heroSwiper;

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