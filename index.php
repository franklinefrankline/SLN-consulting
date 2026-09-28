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

    swiper-container {
        width: 100%;
        height: 100%;
    }

    swiper-slide {
        text-align: center;
        font-size: 18px;
        background-color: #fff !important;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    swiper-slide img {
        display: block;
        width: 100%;
        height: 100%;
        object-fit: cover;
    }

    .autoplay-progress {
        position: absolute;
        right: 16px;
        bottom: 16px;
        z-index: 10;
        width: 48px;
        height: 48px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: var(--swiper-theme-color);
    }

    .autoplay-progress svg {
        --progress: 0;
        position: absolute;
        left: 0;
        top: 0px;
        z-index: 10;
        width: 100%;
        height: 100%;
        stroke-width: 4px;
        stroke: var(--swiper-theme-color);
        fill: none;
        stroke-dashoffset: calc(125.6px * (1 - var(--progress)));
        stroke-dasharray: 125.6;
        transform: rotate(-90deg);
    }

    .mySwiper {
        width: 100%;
        height: 100%;
    }

    .swiper-slide img {
        width: 100%;
        height: auto;
    }

    .autoplay-progress {
        position: absolute;
        bottom: 10px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        align-items: center;
    }

    .autoplay-progress svg {
        width: 48px;
        height: 48px;
    }

    .autoplay-progress span {
        margin-left: 10px;
        font-size: 16px;
    }

    swiper-slide img {
        height: 100vh;
    }

    @media screen and (max-width: 1300px) {}



    @media screen and (max-width: 1024px) {
        swiper-slide img {
            height: 73vh;
        }
    }

    @media screen and (max-width: 768px) {
        swiper-slide img {
            height: 38vh;
        }



    }

    @media screen and (max-width: 820px) {
        swiper-slide img {
            height: 35vh;
        }
    }

    @media only screen and (max-width: 600px) {
        swiper-slide img {
            display: block;
            width: 100%;
            height: 100%;
            object-fit: cover;
        }

        swiper-slide img {
            height: 24vh;
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
            <swiper-container class="mySwiper " pagination="true" pagination-clickable="true" navigation="true"
                space-between="30" centered-slides="true" autoplay-delay="3500" autoplay-disable-on-interaction="false">
                                      <swiper-slide>                    <img id="banner1" src="./assets/img/sln-img/slk-banner7.jpg" alt="">                </swiper-slide>  <swiper-slide>
                    <img id="banner1" src="./assets/img/sln-img/slk-banner11.jpg" alt="">
                </swiper-slide>

                <swiper-slide>
                    <img id="banner1" src="./assets/img/sln-img/slk-banner1.jpg" alt="">
                </swiper-slide>
                <swiper-slide>
                    <img id="banner6" src="./assets/img/sln-img/slk-banner6.jpg" alt="">
                </swiper-slide>
                <swiper-slide>
                    <img id="banner2" src="./assets/img/sln-img/slk-banner2.jpg" alt="">
                </swiper-slide>

                <swiper-slide>
                    <img id="banner4" src="./assets/img/sln-img/slk-banner4.jpg" alt="">
                </swiper-slide>
                <swiper-slide>
                    <img id="banner-cybersecurity-internship" src="assets/img/sln-img/cybersecurity-internship-3-month.png" alt="Cybersecurity Internship">
                </swiper-slide>
                <swiper-slide>
                    <img id="banner5" src="./assets/img/sln-img/slk-banner5.jpg" alt="">
                </swiper-slide>


                <div class="autoplay-progress" slot="container-end">
                    <svg viewBox="0 0 48 48">
                        <circle cx="24" cy="24" r="20"></circle>
                    </svg>
                    <span></span>
                </div>
            </swiper-container>

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
                    <h4 style="font-size: 24px; color:blue;">BCBUZZ Technologies &mdash; Technical Partner</h4><br>
                    <h4>Internship | VAPT | SOC</h4>
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






    <!-- Swiper JS -->
    <script src="https://cdn.jsdelivr.net/npm/swiper@11/swiper-element-bundle.min.js"></script>

    <!-- Initialize Swiper -->
    <script>
    const swiper = new Swiper('.mySwiper', {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        pagination: {
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            320: {
                slidesPerView: 1,
                spaceBetween: 10,
            },
            480: {
                slidesPerView: 1,
                spaceBetween: 20,
            },
            640: {
                slidesPerView: 1,
                spaceBetween: 30,
            }
        }
    });
    </script>



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

    <!-- slider  -->
    <script>
    document.getElementById('banner1').addEventListener('click', function() {
        window.location.href = './index.php';
    });

    document.getElementById('banner2').addEventListener('click', function() {
        window.location.href = './cambridge.php';
    });

    var banner3 = document.getElementById('banner3');
    if (banner3) {
        banner3.addEventListener('click', function() {
            window.location.href = './campus.php';
        });
    }

    document.getElementById('banner4').addEventListener('click', function() {
        window.location.href = './it-service.php';
    });

    document.getElementById('banner5').addEventListener('click', function() {
        window.location.href = './enterprises.php';
    });

    document.getElementById('banner6').addEventListener('click', function() {
        window.location.href = './isc2.php';
    });


    var bannerInternship = document.getElementById('banner-cybersecurity-internship');
    if (bannerInternship) {
        bannerInternship.style.cursor = 'pointer';
        bannerInternship.addEventListener('click', function() {
            window.location.href = './cybersecurity-internship.php';
        });
    }
    </script>
</body>



</html>