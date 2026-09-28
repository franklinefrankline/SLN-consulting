<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slider Example</title>
    <!-- Slick Slider CSS -->
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.css" />
    <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick-theme.min.css" />
</head>
<body>
    <div class="banner-style-four-area text-light bg-cover" style="background-image: url(assets/img/sln-img/sln-baner-1.jpeg);">
        <!-- Slider Container -->
        <div class="banner-slider">
            <!-- Slide 1 -->
            <div class="banner-style-four">
                <div class="container">
                    <div class="content">
                        <div class="row align-center">
                            <div class="col-xl-6 col-lg-7 pr-50 pr-md-15 pr-xs-15">
                                <div class="information">
                                    <h2 class="wow fadeInUp" data-wow-delay="500ms" data-wow-duration="400ms">
                                        Empowering Minds, <br>Elevating Skills, <span class="relative"> Innovative solutions. </span>
                                    </h2>
                                    <p class="wow fadeInUp colo-spn" data-wow-delay="900ms" data-wow-duration="400ms">
                                        Campus Solution <span style="color: red;"> | </span>IT Services <span style="color: red;"> | </span>Training & Certification
                                    </p>
                                    <div class="mt-30 wow fadeInUp" data-wow-delay="1200ms" data-wow-duration="400ms">
                                        <a class="btn-animation" href="skilling.php"><i class="fas fa-arrow-right"></i> <span>Our Services</span></a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-5 pl-60 pl-md-15 pl-xs-15">
                                <div class="thumb">
                                    <img src="assets/img/illustration/7.png" alt="Thumb">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Slide 2 (example) -->
            <div class="banner-style-four">
                <div class="container">
                    <div class="content">
                        <div class="row align-center">
                            <div class="col-xl-6 col-lg-7 pr-50 pr-md-15 pr-xs-15">
                                <div class="information">
                                    <h2 class="wow fadeInUp" data-wow-delay="500ms" data-wow-duration="400ms">
                                        Slide 2 Title Here
                                    </h2>
                                    <p class="wow fadeInUp colo-spn" data-wow-delay="900ms" data-wow-duration="400ms">
                                        Description for Slide 2
                                    </p>
                                    <div class="mt-30 wow fadeInUp" data-wow-delay="1200ms" data-wow-duration="400ms">
                                        <a class="btn-animation" href="link2.php"><i class="fas fa-arrow-right"></i> <span>Read More</span></a>
                                    </div>
                                </div>
                            </div>
                            <div class="col-xl-6 col-lg-5 pl-60 pl-md-15 pl-xs-15">
                                <div class="thumb">
                                    <img src="assets/img/illustration/8.png" alt="Thumb">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!-- Add more slides as needed -->
        </div>
        <!-- End Slider Container -->
    </div>


    
    <!-- Slick Slider JS -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.8.1/slick.min.js"></script>
    <script type="text/javascript">
        $(document).ready(function(){
            $('.banner-slider').slick({
                dots: true,
                infinite: true,
                speed: 500,
                fade: true,
                cssEase: 'linear',
                autoplay: true,
                autoplaySpeed: 2000
            });
        });
    </script>
</body>
</html>
