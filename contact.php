<?php
require_once __DIR__ . '/security.php';
sln_send_security_headers();
sln_start_session();
$csrfToken = sln_get_csrf_token();
$formData = $_SESSION['sln_form_data'] ?? [];
unset($_SESSION['sln_form_data']);
?>
<!DOCTYPE html>
<html lang="en">



<head>
    <!-- ========== Meta Tags ========== -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="SLN Consulting Solution For Seamless Growth">

    <!-- ========== Page Title ========== -->
    <title>SLN Consulting Solution For Seamless Growth</title>

    <!-- ========== Favicon Icon ========== -->
    <link rel="shortcut icon" href="assets/img/sln-img/logo2.png" type="image/x-icon">

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" integrity="sha512-SnH5WK+bZxgPHs44uWIX+LLJAJ9/2PkPKZ5QiAj6Ta86w+fsb2TkcmfRyVX3pBnMFcV7oQPJkl9QevSCWr3W6A==" crossorigin="anonymous" referrerpolicy="no-referrer" />

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

</head>

<body>






    <!-- Header 
    ============================================= -->
    <?php include 'header.php'; ?>
    <!-- End Header -->


    <!-- Start Contact Us 
    ============================================= -->
    <div id="back-col" class="contact-style-one-area overflow-hidden">

        <div class="contact-shape">
            <img src="assets/img/shape/37.png" alt="Image Not Found">
        </div>

        <div class="container">
            <div class="contact-desktop-grid">

                <div class="contact-office-col">
                    <div class="contact-style-one-info">
                        <h2>Corporate Office</h2>
                        <ul>
                            <li>
                                <div class="icon">
                                    <i class="fas fa-map-marker-alt"></i>
                                </div>
                                <div class="info">
                                    <h5 class="title">Our Location</h5>
                                    <p> Chennai-600042, India</p>
                                </div>
                            </li>
                            <li>
                                <div class="icon">
                                    <i class="fas fa-phone-alt"></i>
                                </div>
                                <div class="info">
                                    <h5 class="title">Mobile</h5>
                                    <a href="tel:+919940196195">+91 9940196195</a>
                                </div>
                            </li>
                            <li>
                                <div class="icon">
                                    <i class="fas fa-envelope-open-text"></i>
                                </div>
                                <div class="info">
                                    <h5 class="title">Email Id</h5>
                                    <a href="mailto:srinivas.c@slnconsulting.co.in">srinivas.c@slnconsulting.co.in</a>
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>

                <div class="contact-form-col">
                    <div class="contact-form-style-one">
                        <h2 class="heading">Send us a Message</h2>
                        <!-- Form Submission Status Banner -->
                        <div id="contact-status-container">
                            <?php if (isset($_GET['status'])): ?>
                                <div id="contact-status" class="alert <?php echo ($_GET['status'] === 'success') ? 'alert-success' : 'alert-danger'; ?>" style="<?php echo ($_GET['status'] === 'success') ? 'background-color: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;' : 'background-color: #fef2f2; border: 1px solid #fecaca; color: #991b1b;'; ?> border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;">
                                    <?php if ($_GET['status'] === 'success'): ?>
                                        <i class="fas fa-check-circle" style="color: #059669; margin-right: 8px;"></i>
                                        <strong>Thank you!</strong> Your message has been sent successfully. We will get in touch with you shortly.
                                    <?php else: ?>
                                        <i class="fas fa-exclamation-circle" style="color: #dc2626; margin-right: 8px;"></i>
                                        <strong>Notice:</strong> <?php echo htmlspecialchars($_GET['msg'] ?? 'Unable to send message at this time.'); ?>
                                    <?php endif; ?>
                                </div>
                            <?php endif; ?>
                        </div>
                        <form action="conmail.php" method="POST">
                            <input type="hidden" name="csrf_token" value="<?php echo htmlspecialchars($csrfToken, ENT_QUOTES, 'UTF-8'); ?>">
                            <div style="position: absolute; left: -9999px; top: -9999px; opacity: 0; pointer-events: none;" aria-hidden="true">
                                <label for="sln_website_url">Website</label>
                                <input type="text" id="sln_website_url" name="website_url" tabindex="-1" autocomplete="off" value="">
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <input class="form-control" name="Name" value="<?php echo htmlspecialchars($formData['Name'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Name *" type="text" required maxlength="100">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <input class="form-control" name="Fname" value="<?php echo htmlspecialchars($formData['Fname'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Organisation Name *" type="text" required maxlength="150">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <input class="form-control" name="Subject" value="<?php echo htmlspecialchars($formData['Subject'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Designation *" type="text" required maxlength="100">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <input class="form-control" name="Email" value="<?php echo htmlspecialchars($formData['Email'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Email *" type="email" required maxlength="254">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <input class="form-control" name="Number" value="<?php echo htmlspecialchars($formData['Number'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Phone *" type="text" required maxlength="20">
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group">
                                        <select class="form-control" name="Services" required>
                                            <option value="">Select Service *</option>
                                            <option value="soc" <?php echo (($formData['Services'] ?? '') === 'soc') ? 'selected' : ''; ?>>SOC As A Service</option>
                                            <option value="vapt" <?php echo (($formData['Services'] ?? '') === 'vapt') ? 'selected' : ''; ?>>VAPT</option>
                                            <option value="cybersecurity_internship" <?php echo (($formData['Services'] ?? '') === 'cybersecurity_internship') ? 'selected' : ''; ?>>Cybersecurity Internship</option>
                                            <option value="skilling" <?php echo (($formData['Services'] ?? '') === 'skilling') ? 'selected' : ''; ?>>Skilling</option>
                                            <option value="cambridge" <?php echo (($formData['Services'] ?? '') === 'cambridge') ? 'selected' : ''; ?>>Cambridge Learning</option>
                                            <option value="nure" <?php echo (($formData['Services'] ?? '') === 'nure') ? 'selected' : ''; ?>>ISC2</option>
                                            <option value="ec" <?php echo (($formData['Services'] ?? '') === 'ec') ? 'selected' : ''; ?>>EC-Council</option>
                                            <option value="it_services" <?php echo (($formData['Services'] ?? '') === 'it_services') ? 'selected' : ''; ?>>IT Services</option>
                                        </select>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="form-group comments">
                                        <textarea class="form-control" name="Message" placeholder="Please describe your requirement" maxlength="3000"><?php echo htmlspecialchars($formData['Message'] ?? '', ENT_QUOTES, 'UTF-8'); ?></textarea>
                                    </div>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <button type="submit" name="submit">
                                        Submit
                                    </button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>

            </div>
        </div>
    </div>
    <!-- End Contact -->
    <!-- Start Footer 
    ============================================= -->
    <?php include "footer.php" ?>
    <!-- End Footer -->

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

    <!-- Secure Contact Form Validation & Asynchronous Submission Handler -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form[action="conmail.php"]');
        if (!form) return;

        var container = document.getElementById('contact-status-container');

        function showStatus(type, msg) {
            if (!container) return;
            var isSuccess = (type === 'success');
            var bg = isSuccess ? '#ecfdf5' : '#fef2f2';
            var border = isSuccess ? '#a7f3d0' : '#fecaca';
            var text = isSuccess ? '#065f46' : '#991b1b';
            var icon = isSuccess ? 'fa-check-circle' : 'fa-exclamation-circle';
            var iconColor = isSuccess ? '#059669' : '#dc2626';
            var label = isSuccess ? 'Thank you!' : 'Notice:';

            container.innerHTML = '<div id="contact-status" class="alert ' + (isSuccess ? 'alert-success' : 'alert-danger') + '" style="background-color: ' + bg + '; border: 1px solid ' + border + '; color: ' + text + '; border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;">' +
                '<i class="fas ' + icon + '" style="color: ' + iconColor + '; margin-right: 8px;"></i> ' +
                '<strong>' + label + '</strong> ' + msg +
                '</div>';
            if (container.scrollIntoView) {
                container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
            }
        }

        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var nameInput = form.querySelector('input[name="Name"]');
            var fnameInput = form.querySelector('input[name="Fname"]');
            var subjectInput = form.querySelector('input[name="Subject"]');
            var emailInput = form.querySelector('input[name="Email"]');
            var numberInput = form.querySelector('input[name="Number"]');
            var servicesInput = form.querySelector('select[name="Services"]');
            var messageInput = form.querySelector('textarea[name="Message"]');

            var nameVal = (nameInput ? nameInput.value : '').trim();
            var fnameVal = (fnameInput ? fnameInput.value : '').trim();
            var subjectVal = (subjectInput ? subjectInput.value : '').trim();
            var emailVal = (emailInput ? emailInput.value : '').trim();
            var numberVal = (numberInput ? numberInput.value : '').trim();
            var servicesVal = (servicesInput ? servicesInput.value : '').trim();
            var messageVal = (messageInput ? messageInput.value : '').trim();

            // Client-side Validation: Name
            if (nameVal.length < 2 || nameVal.length > 100 || !/[a-zA-Z]/.test(nameVal) || !/^[a-zA-Z\s.'-]{2,100}$/.test(nameVal)) {
                showStatus('error', 'Please enter a valid full name (letters and spaces only, 2-100 characters).');
                if (nameInput) nameInput.focus();
                return;
            }

            // Client-side Validation: Organisation
            if (fnameVal.length < 2 || fnameVal.length > 150 || !/[a-zA-Z0-9]/.test(fnameVal) || !/^[a-zA-Z0-9\s.',&()\/#-]{2,150}$/.test(fnameVal)) {
                showStatus('error', 'Please enter a valid organisation name (2-150 characters).');
                if (fnameInput) fnameInput.focus();
                return;
            }

            // Client-side Validation: Designation
            if (subjectVal.length < 2 || subjectVal.length > 100 || !/[a-zA-Z]/.test(subjectVal) || !/^[a-zA-Z0-9\s.',&\-\/()]{2,100}$/.test(subjectVal)) {
                showStatus('error', 'Please enter a valid designation / job title (must contain letters, 2-100 characters).');
                if (subjectInput) subjectInput.focus();
                return;
            }

            // Client-side Validation: Email
            var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (emailVal.length < 6 || emailVal.length > 254 || !emailPattern.test(emailVal) || emailVal.indexOf('..') !== -1 || (emailVal.match(/@/g) || []).length !== 1) {
                showStatus('error', 'Please provide a valid email address (e.g. name@domain.com).');
                if (emailInput) emailInput.focus();
                return;
            }

            // Client-side Validation: Phone
            var digitsOnly = numberVal.replace(/\D/g, '');
            if (!/^\+?[0-9\s\-()]{7,20}$/.test(numberVal) || digitsOnly.length < 7 || digitsOnly.length > 15) {
                showStatus('error', 'Please provide a valid phone number (between 7 and 15 digits).');
                if (numberInput) numberInput.focus();
                return;
            }

            // Client-side Validation: Service
            if (!servicesVal) {
                showStatus('error', 'Please select a service from the dropdown list.');
                if (servicesInput) servicesInput.focus();
                return;
            }

            // Client-side Validation: Message length
            if (messageVal.length > 3000) {
                showStatus('error', 'Requirement details cannot exceed 3,000 characters.');
                if (messageInput) messageInput.focus();
                return;
            }

            var submitBtn = form.querySelector('button[type="submit"]');
            var originalBtnHtml = submitBtn ? submitBtn.innerHTML : 'Submit';

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin" style="margin-right: 8px;"></i> Sending...';
            }

            var formData = new FormData(form);

            fetch('conmail.php', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json'
                }
            })
            .then(function(res) {
                return res.json().catch(function() {
                    return { success: false, status: 'error', message: 'Unable to parse server response.' };
                });
            })
            .then(function(data) {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }

                if (data && (data.success === true || (data.status === 'success' && data.success !== false))) {
                    showStatus('success', data.message || 'Your message has been sent successfully. We will get in touch with you shortly.');
                    form.reset();
                    if (window.jQuery && typeof window.jQuery.fn.niceSelect === 'function') {
                        window.jQuery('select').niceSelect('update');
                    }
                } else {
                    showStatus('error', (data && data.message) ? data.message : 'Unable to send message at this time.');
                }
            })
            .catch(function(err) {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }
                showStatus('error', 'Connection error. Please try submitting again.');
            });
        });
    });
    </script>
</body>



</html>