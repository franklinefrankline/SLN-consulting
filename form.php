<?php
require_once __DIR__ . '/security.php';
require_once __DIR__ . '/forms-config.php';
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
    <meta name="description" content="SLN Consulting Solution - Enquiry Form">

    <!-- ========== Page Title ========== -->
    <title>Enquiry Form - SLN Consulting Solution</title>

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

        <div class="container">
            <div class="form-single-card-wrapper">

                <div class="contact-form-style-one">
                    <h2 class="heading">Send us a Message</h2>
                    <!-- Form Submission Status Banner -->
                    <div id="contact-status-container">
                        <?php if (isset($_GET['status'])): ?>
                            <div id="contact-status" class="alert <?php echo ($_GET['status'] === 'success') ? 'alert-success' : 'alert-danger'; ?>" style="<?php echo ($_GET['status'] === 'success') ? 'background-color: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46;' : 'background-color: #fef2f2; border: 1px solid #fecaca; color: #991b1b;'; ?> border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;">
                                <?php if ($_GET['status'] === 'success'): ?>
                                    <i class="fas fa-check-circle" style="color: #059669; margin-right: 8px;"></i>
                                    <strong>Thank you!</strong> Your request has been submitted successfully. We will call you at your preferred time.
                                <?php else: ?>
                                    <i class="fas fa-exclamation-circle" style="color: #dc2626; margin-right: 8px;"></i>
                                    <strong>Notice:</strong> <?php echo htmlspecialchars($_GET['msg'] ?? 'Unable to send request at this time.'); ?>
                                <?php endif; ?>
                            </div>
                        <?php endif; ?>
                    </div>
                    <form action="conmail1.php" method="POST">
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
                                    <small class="time-label">Right time to call <span style="color:red;">*</span></small>
                                    <input class="form-control" name="appt" value="<?php echo htmlspecialchars($formData['appt'] ?? '', ENT_QUOTES, 'UTF-8'); ?>" placeholder="Right time to call" type="time" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <select class="form-control" name="Services">
                                        <option value="">Select Service (Optional)</option>
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
                                    <textarea class="form-control" name="Message" placeholder="Please describe your requirements" maxlength="3000"><?php echo htmlspecialchars($formData['Message'] ?? '', ENT_QUOTES, 'UTF-8'); ?></textarea>
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

    <!-- Secure Callback Form Validation & Asynchronous Submission Handler -->
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form[action="conmail1.php"]');
        if (!form) return;

        var container = document.getElementById('contact-status-container');

        var inputs = form.querySelectorAll('input, select, textarea');

        function clearFieldErrors() {
            inputs.forEach(function(el) {
                el.style.borderColor = '';
                el.style.boxShadow = '';
            });
        }

        inputs.forEach(function(el) {
            el.addEventListener('input', function() {
                el.style.borderColor = '';
                el.style.boxShadow = '';
            });
            el.addEventListener('change', function() {
                el.style.borderColor = '';
                el.style.boxShadow = '';
            });
        });

        function markInvalid(inputEl) {
            if (!inputEl) return;
            inputEl.style.borderColor = '#dc2626';
            inputEl.style.boxShadow = '0 0 0 3px rgba(220, 38, 38, 0.15)';
            inputEl.focus();
        }

        function showStatus(type, msg) {
            if (!container) return;
            var isSuccess = (type === 'success');
            var bg = isSuccess ? '#ecfdf5' : '#fef2f2';
            var border = isSuccess ? '#a7f3d0' : '#fecaca';
            var text = isSuccess ? '#065f46' : '#991b1b';
            var icon = isSuccess ? 'fa-check-circle' : 'fa-exclamation-circle';
            var iconColor = isSuccess ? '#059669' : '#dc2626';
            var label = isSuccess ? 'Success!' : 'Notice:';

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
            clearFieldErrors();

            var nameInput = form.querySelector('input[name="Name"]');
            var fnameInput = form.querySelector('input[name="Fname"]');
            var subjectInput = form.querySelector('input[name="Subject"]');
            var emailInput = form.querySelector('input[name="Email"]');
            var numberInput = form.querySelector('input[name="Number"]');
            var apptInput = form.querySelector('input[name="appt"]');
            var servicesInput = form.querySelector('select[name="Services"]');
            var messageInput = form.querySelector('textarea[name="Message"]');

            var nameVal = (nameInput ? nameInput.value : '').trim();
            var fnameVal = (fnameInput ? fnameInput.value : '').trim();
            var subjectVal = (subjectInput ? subjectInput.value : '').trim();
            var emailVal = (emailInput ? emailInput.value : '').trim();
            var numberVal = (numberInput ? numberInput.value : '').trim();
            var apptVal = (apptInput ? apptInput.value : '').trim();
            var servicesVal = (servicesInput ? servicesInput.value : '').trim();
            var messageVal = (messageInput ? messageInput.value : '').trim();

            // Client-side Validation: Name (required, reject blank/whitespace)
            if (!nameVal || nameVal.length < 2 || nameVal.length > 100 || !/[a-zA-Z]/.test(nameVal) || !/^[a-zA-Z\s.'-]{2,100}$/.test(nameVal)) {
                showStatus('error', 'Please enter a valid full name (letters and spaces only, 2-100 characters).');
                markInvalid(nameInput);
                return;
            }

            // Client-side Validation: Organisation (required, reject blank, standard corporate chars)
            if (!fnameVal || fnameVal.length < 2 || fnameVal.length > 150 || !/[a-zA-Z0-9]/.test(fnameVal) || !/^[a-zA-Z0-9\s.',&()\/#-]{2,150}$/.test(fnameVal)) {
                showStatus('error', 'Please enter a valid organisation name (2-150 characters).');
                markInvalid(fnameInput);
                return;
            }

            // Client-side Validation: Designation (required, must contain letters)
            if (!subjectVal || subjectVal.length < 2 || subjectVal.length > 100 || !/[a-zA-Z]/.test(subjectVal) || !/^[a-zA-Z0-9\s.',&\-\/()]{2,100}$/.test(subjectVal)) {
                showStatus('error', 'Please enter a valid designation / job title (must contain letters, 2-100 characters).');
                markInvalid(subjectInput);
                return;
            }

            // Client-side Validation: Email (required, valid format)
            var emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
            if (!emailVal || emailVal.length < 6 || emailVal.length > 254 || !emailPattern.test(emailVal) || emailVal.indexOf('..') !== -1 || (emailVal.match(/@/g) || []).length !== 1) {
                showStatus('error', 'Please provide a valid email address (e.g. name@domain.com).');
                markInvalid(emailInput);
                return;
            }

            // Client-side Validation: Phone (required, valid digits & country-code symbols)
            var digitsOnly = numberVal.replace(/\D/g, '');
            if (!numberVal || !/^\+?[0-9\s\-()]{7,20}$/.test(numberVal) || digitsOnly.length < 7 || digitsOnly.length > 15) {
                showStatus('error', 'Please provide a valid phone number (between 7 and 15 digits).');
                markInvalid(numberInput);
                return;
            }

            // Client-side Validation: Preferred Call Time (required in this form)
            if (!apptVal || apptVal.length < 2 || apptVal.length > 30 || !/^[0-9a-zA-Z\s:.-]{2,30}$/.test(apptVal)) {
                showStatus('error', 'Please specify a preferred time for a callback.');
                markInvalid(apptInput);
                return;
            }

            // Client-side Validation: Message length
            if (messageVal.length > 3000) {
                showStatus('error', 'Requirement details cannot exceed 3,000 characters.');
                markInvalid(messageInput);
                return;
            }

            var submitBtn = form.querySelector('button[type="submit"]');
            var originalBtnHtml = submitBtn ? submitBtn.innerHTML : 'Submit';

            // Prevent duplicate clicks while request is in progress
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin" style="margin-right: 8px;"></i> Submitting...';
            }

            var formData = new FormData(form);
            var urlParams = new URLSearchParams();
            formData.forEach(function(val, key) {
                urlParams.append(key, val);
            });

            var controller = (typeof AbortController !== 'undefined') ? new AbortController() : null;
            var timeoutId = null;
            if (controller) {
                timeoutId = setTimeout(function() {
                    controller.abort();
                }, 15000);
            }

            // Asynchronously dispatch to backend on the same page
            fetch('conmail1.php', {
                method: 'POST',
                body: urlParams,
                signal: controller ? controller.signal : undefined,
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json'
                }
            })
            .then(function(res) {
                if (timeoutId) clearTimeout(timeoutId);
                return res.json().catch(function() {
                    return { success: false, status: 'error', message: 'Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.' };
                });
            })
            .then(function(data) {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }

                if (data && (data.success === true || (data.status === 'success' && data.success !== false))) {
                    // Success: Display required message on the same page
                    showStatus('success', 'Your enquiry has been submitted successfully! Thank you for contacting SLN Consulting. Our team will get back to you soon.');
                    // Clear fields only after successful server-side processing
                    form.reset();
                    clearFieldErrors();
                    if (window.jQuery && typeof window.jQuery.fn.niceSelect === 'function') {
                        window.jQuery('select').niceSelect('update');
                    }
                } else {
                    // Failure: Preserve entered values and show designated error
                    var failureMsg = (data && data.message && data.message !== 'Unable to parse server response.') 
                        ? data.message 
                        : 'Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.';
                    showStatus('error', failureMsg);
                }
            })
            .catch(function(err) {
                if (timeoutId) clearTimeout(timeoutId);
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }
                // Failure / Timeout / Network error: Preserve entered values
                showStatus('error', 'Unable to submit your enquiry right now. Your details have not been confirmed as saved. Please try again.');
            });
        });
    });
    </script>

</body>

</html>