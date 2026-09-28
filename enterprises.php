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
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

    <!-- ========== Favicon Icon ========== -->
    <link rel="shortcut icon" href="assets/img/sln-img/logo2.png" type="image/x-icon">

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
        .en-ca{
            background-color: #0b57e3;
            color: #fff;
            padding: 10px;
            width: 23%;
            border-radius: 5px;
        }
        .ca-en{
            background-color: #0b57e3;
            color: #fff;
            padding: 10px;
            width: 19%;
            border-radius: 5px;
        }
        ul.check-list5 {
            padding-left: 0;
            list-style: none;
            display: grid;
            grid-template-columns: 1fr 1fr 1fr;
            grid-column-gap: 60px;
            grid-row-gap: 30px;
            margin-top: 50px;
            margin-bottom: 0;
        }
        ul.check-list8 {
            padding-left: 0;
            list-style: none;
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-column-gap: 60px;
            grid-row-gap: 25px;
            margin-top: 55px;
            margin-bottom: 0;
        }
        ul.check-list8 li::after {
            position: absolute;
            left: 0;
            content: "\f058";
            top: 0;
            font-family: "Font Awesome 5 Pro";
            font-size: 20px;
            color: var(--color-primary);
            font-weight: 600;
        }
        ul.check-list8 li {
            position: relative;
            z-index: 1;
            padding-left: 35px;
        }
        ul.check-list5 li {
            z-index: 1;
            padding-left: 35px;
            position: relative;
        }
        ul.check-list5 li::after {
            left: 0;
            top: 0;
            content: "\f058";
            font-family: "Font Awesome 5 Pro";
            font-size: 20px;
            color: var(--color-primary);
            font-weight: 600;
            position: absolute;
        }
        .cyber{
            text-align:center;
            margin-bottom: 70px;
            color: #fff;
        }

        .inner-page-padding {
            padding: 125px 0px;
        }
        .arck-service-content-2 {
            padding-top: 40px;
        }
        .arck-service-item-2 {
            border-radius:10px;
            margin-bottom: 30px;
            background-color: #fff;
            padding: 50px 35px 45px;
            -webkit-transition: var(--transition);
            transition: var(--transition);
            -webkit-box-shadow: 0px 0px 50px 0px rgba(35, 31, 32, 0.1);
            box-shadow: 0px 0px 50px 0px rgba(35, 31, 32, 0.1);
            overflow: hidden;
        }
        .arck-service-item-2 .inner-icon {
            width: 80px;
            height: 70px;
            margin-bottom: 40px;
            border: 5px solid #D7F1FA;
            -webkit-transition: var(--transition);
            transition: var(--transition);
            z-index: 1;
        }
        .arck-service-item-2 .inner-icon:before {
            left: 0;
            right: 0;
            top: -5px;
            content: "";
            z-index: -1;
            width: 28px;
            height: 116%;
            margin: 0 auto;
            position: absolute;
            -webkit-transition: var(--transition);
            transition: var(--transition);
            background-color: #fff;
        }
        .arck-service-item-2 .inner-icon:after {
            top: 50%;
            left: -5px;
            content: "";
            z-index: -1;
            width: 116%;
            height: 28px;
            position: absolute;
            -webkit-transform: translateY(-50%);
            transform: translateY(-50%);
            -webkit-transition: var(--transition);
            transition: var(--transition);
            background-color: #fff;
        }
        .feature-list-item1 li {
            position: relative;
            z-index: 1;
            /* padding-left: 45px; */
            margin-top: 30px;
            font-weight: 500;
        }
        /* .feature-list-item1 li::after {
            position: absolute;
            left: 0;
            top: 1px;
            content: "\f00c";
            font-family: "Font Awesome 5 Pro";
            color: #1b0ee4;
            font-weight: 500;
            font-size: 18px;
            background-color: #fff;
            padding: 6px;
            border-radius: 5px;
        } */
        .feature-list-item1 li h4{
            background-color: #0058ff;
            padding: 15px 10px;
            border-radius: 10px;
            color:#fff;
        }
        .feature-list-item2 li {
            position: relative;
            z-index: 1;
            padding-left: 45px;
            margin-top: 30px;
            font-weight: 500;
        }
        /* .feature-list-item2 li::after {
            position: absolute;
            left: 0;
            top: 8px;
            content: "\f00c";
            font-family: "Font Awesome 5 Pro";
            color: #fff;
            font-weight: 500;
            font-size: 18px;
            background-color: #0058ff;
            padding: 6px;
            border-radius: 5px;
        } */
        .feature-list-item2 li h4{
            background-color: #0058ff;
            padding: 15px 10px;
            border-radius: 10px;
            color:#fff;
        }
        .default-padding1 {
    padding-top: 40px;
    padding-bottom: 80px;
}
        .progress-item-two.style-two {
    border: none;
    margin-top: -65px;
    padding: 0 15px 30px;
}
.progress-item-two {
    z-index: 1;
    position: relative;
    text-align: center;
    padding: 0 40px 60px;
    border-right: 1px solid #e6e8eb;
}
.progress-item-two.style-two .progress-step {
    left: 0;
    top: 55px;
    z-index: 1;
    color: #fff;
    font-weight: 400;
    position: relative;
}
.progress-item-two .progress-step {
    position: absolute;
    font-size: 125px;
    font-weight: 900;
    opacity: 0.06;
    left: 50%;
    z-index: -1;
    bottom: 5px;
    line-height: 1;
    color: #104cba;
    font-family: "Nunito", sans-serif;
    -webkit-transform: translate(-50%);
    -ms-transform: translate(-50%);
    transform: translate(-50%);
}
.progress-item-two.style-two .icon {
    background: white;
    margin-bottom: 25px;
    -webkit-transform: translateY(0);
    -ms-transform: translateY(0);
    transform: translateY(0);
}

.progress-item-two .icon {
    color: white;
    font-size: 60px;
    padding-top: 8px;
    margin: 0 auto -35px;
    -webkit-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    transform: translateY(-50%);
    width: 125px;
    height: 125px;
    background: #104cba;
    line-height: 125px;
    border-radius: 50%;
    text-align: center;
}
.w-col{
    color:#fff
}
.icon img{
    width: 50px;
}
#back-col1{
    background-color: #104CBA;
}
.progress-item-two i{
    font-size:17px;
}
.s-text h3{
    color: #fff;
    margin-top: 15px;
    margin-left: 10px;
}
.s-text i{
    font-size:23px;
}
.s-text{
    display: flex;
    justify-content: center;
    align-items: center;
    margin-top: 40px;
}
@media (max-width: 767px) {
    .feature-list-item2 li{
        padding-left:0px;
    }
    ul.check-list8{
        display: block;
    }
}
        /* .feature-list-item{
            display: grid;
            grid-template-columns: 1fr 1fr;
        } */
    </style>
</head>

<body>

    <?php include 'header.php'; ?>

    <!-- Star Services Details Area
    ============================================= -->
    <div id="back-col1" class="services-details-area overflow-hidden default-padding mtop">
        <div class="container">
            <div class="work-progress-inner-three">
                <div class="row justify-content-center">
                    <h1 class="cyber">Training</h1>
                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">01</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon1.png" alt="">
                                        </div>
                                        <h3 class="w-col">Cybersecurity<i class="fa-solid fa-star" style="color: #FFD43B;"></i><i class="fa-solid fa-star" style="color: #FFD43B;"></i></h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">02</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon2.png" alt="">
                                        </div>
                                        <h3 class="w-col">Data Sciences</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">03</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon3.png" alt="">
                                        </div>
                                        <h3 class="w-col">Cloud Computing</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">04</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon4.png" alt="">
                                        </div>
                                        <h3 class="w-col">Network Management</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">05</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon5.png" alt="">
                                        </div>
                                        <h3 class="w-col">Artificial Intelligence</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">06</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon6.png" alt="">
                                        </div>
                                        <h3 class="w-col">Machine Language</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">07</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon7.png" alt="">
                                        </div>
                                        <h3 class="w-col">Soft Skills</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">08</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon8.png" alt="">
                                        </div>
                                        <h3 class="w-col">Soft Management Skills</h3>
                                    </div>
                    </div>

                    <div class="col-lg-4 col-sm-6">
                                    <div class="progress-item-two style-two wow fadeInUp delay-0-2s animated" style="visibility: visible; animation-name: fadeInUp;">
                                        <span class="progress-step">09</span>
                                        <div class="icon d-flex justify-content-center align-items-center position-relative">
                                            <img src="assets/img/sln-img/icon9.png" alt="">
                                        </div>
                                        <h3 class="w-col">Leadership</h3>
                                    </div>
                    </div> 
                    
                    <div class="s-text">
                        <i class="fa-solid fa-star" style="color: #FFD43B;"></i>
                        <i class="fa-solid fa-star" style="color: #FFD43B;"></i>
                        <h3>All Cybersecurity training leads to attempting global certifications - ISACA, ISC2, EC-Council etc</h3>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="back-col" class="services-details-area overflow-hidden default-padding">
        <div class="container">
            <div class="services-details-items">
                <div class="row">
                    <div  class="col-xl-12 col-lg-12 order-lg-last pl-50 pl-md-15 pl-xs-15">
                            <h2>Workshops & webinars for Mid & Senior Managers</h2>
                            <div class="features mt-40 mt-xs-30 mb-30 mb-xs-20">
                                <div class="row">
                                    <div class="col-lg-6 col-md-6">
                                        <div class="content">
                                            <ul class="feature-list-item1">
                                                <li><h4>Executive Session on Cybersecurity for C-Suite Leaders</h4></li>
                                                <li><h4>Cybersecurity Risks for Financial Organizations</h4></li>
                                                <li><h4>Cybersecurity Enterprise Awareness: Empowering Vigilance</h4></li>
                                                <li><h4>Critical IT & Cybersecurity Infrastructure Review</h4></li>
                                                <li><h4>Artificial Intelligence (Ai) for Information Security Audit</h4></li>
                                                <li><h4>Threats and Vulnerability Management</h4></li>
                                                <li><h4>Data Security: Addressing Enterprise Concerns</h4></li>
                                                <li><h4>Cybersecurity in the Cloud: Ensuring Visibility & Control</h4></li>
                                            </ul>
                                        </div>
                                    </div>

                                    <div class="col-lg-6 col-md-6">
                                        <div class="content">
                                            <ul class="feature-list-item2">
                                                <li><h4>Zero Trust: Disrupt, Destroy, Steal</h4></li>
                                                <li><h4>Blockchain Operational and Deployment Insights</h4></li>
                                                <li><h4>Metaverse Technologies and Enterprise Adoption</h4></li>
                                                <li><h4>Security Challenges: Disrupting Disruptors</h4></li>
                                                <li><h4>Blockchain: Transforming Business Processes</h4></li>
                                                <li><h4>Cybersecurity for Oil & Gas: Redefining the Landscape</h4></li>
                                                <li><h4>Leadership Excellence: Mid & Senior managers</h4></li>
                                                <li><h4>Resilience & Building trusted security workforce</h4></li>
                                            </ul>
                                        </div>
                                    </div>
                                </div>
                            </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div id="back-col" class="services-details-area overflow-hidden default-padding1">
        <div class="container">
            <div class="services-details-items">
                <div class="row">
                    <div class="col-xl-12 col-lg-12 pr-35 pr-md-15 pr-xs-15 left-info mt-md-10">
                        <h2>Workshop in Cyber security for freshers</h2>
                        <ul class="check-list8">
                                    <li>
                                        <h4>Cybersecurity awareness - essentials workshop.</h4>
                                        <p>
                                            Introduction to the key architectural and technological concepts of cybersecurity.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Security monitoring & management</h4>
                                        <p>
                                            Tools, concepts and methods used to monitor and manage the network security infrastructure.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Network security concepts & methodologies</h4>
                                        <p>
                                            Key cyber security threats, attack patterns and risks in the cyber world.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Essential tools for cyber investigation</h4>
                                        <p>
                                            Professional tools to investigate an accident, collect initial evidence and extract the required information for use by the incident response team.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Incident response principal tactics</h4>
                                        <p>
                                            Tools, skills and work methods utilised by an incident response team
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Cyber crisis management</h4>
                                        <p>
                                            Skills and concepts required for successful management of a major cyber incident, based on best practices and actual case studies.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Ethical hacking & penetration testing principles</h4>
                                        <p>
                                            Principles, methodologies and tools for ethical hacking and penetration testing.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Secure software development a basic introduction</h4>
                                        <p>
                                            Principles for designing secure software architecture and developing secure code, utilising known practices and techniques.
                                        </p>
                                    </li>
                                    <li>
                                        <h4>Overview of cyber basics</h4>
                                        <p>
                                        I   nternal processes, mechanisms and stages of malware execution; hands-on experience in collecting evidence and performing a forensic investigation
                                        </p>
                                    </li>
                        </ul>
                    </div>
                </div>
                            <div class="connect-btn">
                                <button><a href="form.php">Let’s discuss</a></button>
                            </div>
            </div>
        </div>
    </div>
    
    <!-- <section class="work-progress-three text-white pb-85 rpb-65" style="background-image: url(assets/images/background/progress.png); background-color:#0058ff;">
            
        </section> -->


    
    <!-- End Services Details Area -->

    <?php include 'footer.php'; ?>
    
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

</body>
</html>