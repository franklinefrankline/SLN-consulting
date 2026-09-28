<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> <!-- jQuery -->


<style>
       nav {
           background-color: white;
       }
       .navbar-nav .nav-link.active {
           color: #013df5 !important;
           font-weight: 600;
       }
       @media (min-width: 1024px) {
           nav.navbar .container {
               max-width: 1320px !important;
               flex-wrap: nowrap !important;
           }
           nav.navbar ul.nav > li > a {
               padding: 30px 10px !important;
               font-size: 15px !important;
           }
           .navbar .attr-right {
               margin-left: 15px !important;
               flex-shrink: 0 !important;
           }
           .navbar .attr-right .attr-nav li.button a {
               padding: 10px 22px !important;
               white-space: nowrap !important;
           }
           .navbar-header {
               flex-shrink: 0 !important;
           }
           .navbar-brand img {
               width: 235px !important;
           }
       }
   </style>
  

   <!-- Header 
    ============================================= -->
   <header>
       <!-- Start Navigation -->
       <nav class="navbar secondary mobile-sidenav navbar-sticky navbar-default validnavs navbar-fixed white no-background">
        <div class="container d-flex justify-content-between align-items-center">

            <!-- Start Header Navigation -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-menu">
                    <i class="fa fa-bars"></i>
                </button>
                <a class="navbar-brand" href="index.php">
                    <img style="width: 270px;" src="assets/img/sln-img/sln-logo.png" class="logo logo-display" alt="Logo">
                    <img style="width: 270px;" src="assets/img/sln-img/sln-logo.png" class="logo logo-scrolled" alt="Logo">
                </a>
            </div>
            <!-- End Header Navigation -->

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="navbar-menu">
                <div class="collapse-header">
                    <img src="assets/img/sln-img/sln-logo-2.png" alt="Logo">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-menu">
                        <i class="fa fa-times"></i>
                    </button>
                </div>

                <ul class="nav navbar-nav navbar-center" data-in="fadeInDown" data-out="fadeOutUp">
                    <li class="dropdown">
                        <a href="index.php" class="nav-link">Home</a>
                    </li>
                    <li class="dropdown">
                        <a href="about-us.php" class="nav-link">About Us</a>
                    </li>
                    <li class="dropdown nonr">
                        <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown">Our Offering <i class="fa-solid fa-angle-down"></i></a>
                        <ul class="dropdown-menu">
                            <li><a href="soc.php" class="nav-link">SOC-As-A-Service</a></li>
                            <li><a href="vapt.php" class="nav-link">VAPT</a></li>
                            <li class="dropdown">
                                <a href="#" class="nav-link dropdown-toggle" data-toggle="">Skilling Solutions</a>
                                <ul class="dropdown-menu">
                                    <li><a href="enterprises.php" class="nav-link">Enterprises</a></li>
                                    <li><a href="campus.php" class="nav-link">Campus</a></li>
                                </ul>
                            </li>
                            <li><a href="cambridge.php" class="nav-link">Cambridge Learning</a></li>
                            <li><a href="isc2.php" class="nav-link">ISC2</a></li>
                            <li><a href="ecc.php" class="nav-link">EC-COUNCIL</a></li>
                            <li><a href="it-service.php" class="nav-link">IT Services</a></li>
                        </ul>
                    </li>
                    <li>
                        <a href="cybersecurity-internship.php" class="nav-link">Internships</a>
                    </li>
                    <li class="dropdown">
                        <a href="gallery.php" class="nav-link" data-toggle="dropdown">Gallery</a>
                    </li>
                    <li><a href="training-schedule.php" class="nav-link">Training Schedule</a></li>
                    <li><a href="contact.php" class="nav-link">Contact</a></li>
                </ul>
            </div><!-- /.navbar-collapse -->

            <div class="attr-right">
                <!-- Start Atribute Navigation -->
                <div class="attr-nav">
                    <ul>
                        <li class="button light">
                            <a href="contact.php" class="nav-link"> Enquire Now</a>
                        </li>
                    </ul>
                </div>
                <!-- End Atribute Navigation -->
            </div>
        </div>
        <!-- Overlay screen for menu -->
        <div class="overlay-screen"></div>
        <!-- End Overlay screen for menu -->
    </nav>


       <!-- End Navigation -->
   </header>
   <!-- End Header -->


   <script>
    document.addEventListener("DOMContentLoaded", function() {
        var currentPath = window.location.pathname.split("/").pop();
        var navLinks = document.querySelectorAll(".navbar-nav .nav-link");

        navLinks.forEach(function(link) {
            var linkPath = link.getAttribute("href");
            if (linkPath === currentPath) {
                link.classList.add("active");
                var parentDropdown = link.closest("li.dropdown");
                if (parentDropdown) {
                    var toggle = parentDropdown.querySelector(".dropdown-toggle");
                    if (toggle) toggle.classList.add("active");
                }
            }
        });
    });
    </script>