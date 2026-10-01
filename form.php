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
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input class="form-control" name="Name" placeholder="Name *" type="text" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input class="form-control" name="Fname" placeholder="Organisation Name *" type="text" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input class="form-control" name="Subject" placeholder="Desigination *" type="text" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input class="form-control" name="Email" placeholder="Email *" type="email" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <input class="form-control" name="Number" placeholder="Phone *" type="text" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <small class="time-label">Right time to call <span style="color:red;">*</span></small>
                                    <input class="form-control" name="appt" placeholder="Right time to call" type="time" required>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group">
                                    <select class="form-control" name="Services" required>
                                        <option value="">Select Service *</option>
                                        <option value="soc">SOC As A Service</option>
                                        <option value="vapt">VAPT</option>
                                        <option value="cybersecurity_internship">Cybersecurity Internship</option>
                                        <option value="skilling">Skilling</option>
                                        <option value="cambridge">Cambridge</option>
                                        <option value="nure">ISC2</option>
                                        <option value="ec">EC-Council</option>
                                        <option value="it_services">IT Services</option>
                                    </select>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-lg-12">
                                <div class="form-group comments">
                                    <textarea class="form-control" name="Message" placeholder="Please describe your requirements"></textarea>
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

    <script>
    document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form[action="conmail1.php"]');
        if (!form) return;

        form.addEventListener('submit', function(e) {
            e.preventDefault();

            var submitBtn = form.querySelector('button[type="submit"]');
            var originalBtnHtml = submitBtn ? submitBtn.innerHTML : 'Submit';
            var container = document.getElementById('contact-status-container');

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin" style="margin-right: 8px;"></i> Sending...';
            }

            var formData = new FormData(form);

            fetch('conmail1.php', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json'
                }
            })
            .then(function(res) {
                return res.json().catch(function() {
                    return { status: res.ok ? 'success' : 'error', message: 'Unable to parse server response.' };
                });
            })
            .then(function(data) {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }

                if (data.status === 'success') {
                    if (container) {
                        container.innerHTML = '<div id="contact-status" class="alert alert-success" style="background-color: #ecfdf5; border: 1px solid #a7f3d0; color: #065f46; border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;"><i class="fas fa-check-circle" style="color: #059669; margin-right: 8px;"></i> <strong>Thank you!</strong> ' + (data.message || 'Your request has been submitted successfully.') + '</div>';
                    }
                    form.reset();
                    if (window.jQuery && typeof window.jQuery.fn.niceSelect === 'function') {
                        window.jQuery('select').niceSelect('update');
                    }
                } else {
                    if (container) {
                        container.innerHTML = '<div id="contact-status" class="alert alert-danger" style="background-color: #fef2f2; border: 1px solid #fecaca; color: #991b1b; border-radius: 8px; padding: 14px 18px; font-size: 15px; margin-bottom: 20px;"><i class="fas fa-exclamation-circle" style="color: #dc2626; margin-right: 8px;"></i> <strong>Notice:</strong> ' + (data.message || 'Unable to send request at this time.') + '</div>';
                    }
                }

                if (container && container.scrollIntoView) {
                    container.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
                }
            })
            .catch(function(err) {
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnHtml;
                }
                form.submit();
            });
        });
    });
    </script>

</body>

</html>