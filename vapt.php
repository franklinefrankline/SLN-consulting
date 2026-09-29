<!DOCTYPE html>
<html lang="en">

<head>
    <!-- ========== Meta Tags ========== -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="Vulnerability Assessment and Penetration Testing (VAPT) services by SLN Consulting. Comprehensive web, mobile, network, API, cloud, and IoT security testing.">

    <!-- ========== Page Title ========== -->
    <title>Vulnerability Assessment &amp; Penetration Testing (VAPT) | SLN Consulting</title>

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

    <!-- Scoped VAPT styles strictly adhering to SLN visual system -->
    <style>
        .vapt-hero-img {
            border-radius: 12px;
            box-shadow: 0 15px 35px rgba(1, 61, 245, 0.12);
            width: 100%;
            height: 400px;
            object-fit: cover;
            display: block;
            border: 1px solid #d0e7f5;
        }

        .vapt-audit-img {
            border-radius: 12px;
            box-shadow: 0 15px 35px rgba(1, 61, 245, 0.12);
            width: 100%;
            height: 380px;
            object-fit: cover;
            display: block;
            border: 1px solid #d0e7f5;
        }

        .vapt-service-card {
            background: #ffffff;
            border-radius: 10px;
            padding: 26px 22px;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.03);
            border: 1px solid #e2e8f0;
            height: 100%;
            display: flex;
            flex-direction: column;
            transition: all 0.3s ease;
        }

        .vapt-service-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 10px 25px rgba(1, 61, 245, 0.1);
            border-color: #013df5;
        }

        .vapt-icon-box {
            width: 52px;
            height: 52px;
            background: #D7F1FA;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #013df5;
            font-size: 22px;
            margin-bottom: 16px;
            transition: all 0.3s ease;
        }

        .vapt-service-card:hover .vapt-icon-box {
            background: #013df5;
            color: #ffffff;
        }

        .vapt-step-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 22px 18px;
            height: 100%;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }

        .vapt-step-card:hover {
            border-color: #013df5;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(1, 61, 245, 0.08);
        }

        .vapt-step-num {
            font-family: var(--font-heading, 'Outfit', sans-serif);
            font-size: 15px;
            font-weight: 700;
            color: #013df5;
            background: #D7F1FA;
            width: 36px;
            height: 36px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 12px;
        }

        .vapt-area-item {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 22px 18px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            height: 100%;
            transition: all 0.3s ease;
        }

        .vapt-area-item:hover {
            border-color: #013df5;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(1, 61, 245, 0.08);
        }

        .vapt-area-icon {
            font-size: 24px;
            color: #013df5;
            margin-bottom: 12px;
        }

        .vapt-deliverable-box {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-left: 4px solid #013df5;
            border-radius: 8px;
            padding: 20px 18px;
            height: 100%;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }

        .vapt-deliverable-box:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(1, 61, 245, 0.08);
        }

        .vapt-benefit-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 22px 18px;
            height: 100%;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            transition: all 0.3s ease;
        }

        .vapt-benefit-card:hover {
            border-color: #013df5;
            transform: translateY(-3px);
            box-shadow: 0 8px 20px rgba(1, 61, 245, 0.08);
        }

        .vapt-soc-box {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 28px 24px;
            height: 100%;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
            position: relative;
        }

        .vapt-soc-badge {
            display: inline-block;
            background: #D7F1FA;
            color: #013df5;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 13px;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
        }

        ul.vapt-check-list {
            list-style: none;
            padding-left: 0;
            margin: 0;
        }

        ul.vapt-check-list li {
            position: relative;
            padding-left: 24px;
            margin-bottom: 10px;
            font-size: 15px;
            line-height: 24px;
            color: var(--color-paragraph, #666666);
        }

        ul.vapt-check-list li i {
            position: absolute;
            left: 0;
            top: 4px;
            color: #013df5;
            font-size: 14px;
        }

        .vapt-cta-box {
            background: #ffffff;
            border: 1px solid #bcdbeb;
            border-radius: 14px;
            padding: 36px 42px;
            box-shadow: 0 10px 30px rgba(1, 61, 245, 0.08);
            width: 100%;
        }

        @media (max-width: 991px) {
            .vapt-hero-img,
            .vapt-audit-img {
                height: 320px;
                margin-top: 25px;
            }
        }
    </style>
</head>

<body>

    <!-- Header 
    ============================================= -->
    <?php include 'header.php'; ?>
    <!-- End Header -->

    <!-- =============================================
         1. HERO / INTRODUCTION (Light Blue Section)
    ============================================= -->
    <div id="back-col" class="about-style-two-area overflow-hidden bg-contain default-padding mtop"
        style="background-image: url(assets/img/shape/29.png);">
        <div class="container">
            <div class="row align-center">
                <div class="about-style-two col-lg-6">
                    <h2 class="title" style="margin-top: 10px; margin-bottom: 16px;">
                        Vulnerability Assessment &amp; Penetration Testing (VAPT)
                    </h2>
                    <p style="font-size: 17px; line-height: 28px; color: #1e293b; margin-bottom: 14px;">
                        Identify, validate, and remediate security vulnerabilities across your digital assets before attackers can exploit them.
                    </p>
                    <p style="font-size: 15px; line-height: 26px; color: #555555; margin-bottom: 24px;">
                        SLN Consulting delivers industry-aligned VAPT services combining automated scanning with skilled manual penetration testing. We uncover real-world risks, eliminate false positives, and provide actionable technical remediation roadmaps to ensure your applications, networks, and cloud infrastructure remain resilient and compliant.
                    </p>
                    <div class="row mt-25">
                        <div class="col-sm-6 mb-15">
                            <div style="background: #ffffff; border: 1px solid #bcdbeb; border-radius: 10px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; height: 100%; box-shadow: 0 2px 8px rgba(1, 61, 245, 0.04);">
                                <div style="width: 38px; height: 38px; border-radius: 8px; background: #d7f1fa; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #013df5;">
                                    <i class="fas fa-shield-alt" style="font-size: 16px;"></i>
                                </div>
                                <div>
                                    <h5 style="font-family: var(--font-heading, 'Outfit', sans-serif); font-size: 14.5px; font-weight: 700; color: #0e0e0e; margin: 0 0 2px 0; line-height: 1.3;">Automated &amp; Manual Audits</h5>
                                    <p style="font-family: var(--font-default, 'Outfit', sans-serif); font-size: 12.5px; color: #64748b; margin: 0; line-height: 1.3;">In-depth threat simulation</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-15">
                            <div style="background: #ffffff; border: 1px solid #bcdbeb; border-radius: 10px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; height: 100%; box-shadow: 0 2px 8px rgba(1, 61, 245, 0.04);">
                                <div style="width: 38px; height: 38px; border-radius: 8px; background: #d7f1fa; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #013df5;">
                                    <i class="fas fa-check-double" style="font-size: 16px;"></i>
                                </div>
                                <div>
                                    <h5 style="font-family: var(--font-heading, 'Outfit', sans-serif); font-size: 14.5px; font-weight: 700; color: #0e0e0e; margin: 0 0 2px 0; line-height: 1.3;">Zero False Positives</h5>
                                    <p style="font-family: var(--font-default, 'Outfit', sans-serif); font-size: 12.5px; color: #64748b; margin: 0; line-height: 1.3;">Evidence-backed validation</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-15">
                            <div style="background: #ffffff; border: 1px solid #bcdbeb; border-radius: 10px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; height: 100%; box-shadow: 0 2px 8px rgba(1, 61, 245, 0.04);">
                                <div style="width: 38px; height: 38px; border-radius: 8px; background: #d7f1fa; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #013df5;">
                                    <i class="fas fa-clipboard-check" style="font-size: 16px;"></i>
                                </div>
                                <div>
                                    <h5 style="font-family: var(--font-heading, 'Outfit', sans-serif); font-size: 14.5px; font-weight: 700; color: #0e0e0e; margin: 0 0 2px 0; line-height: 1.3;">Standards &amp; Compliance</h5>
                                    <p style="font-family: var(--font-default, 'Outfit', sans-serif); font-size: 12.5px; color: #64748b; margin: 0; line-height: 1.3;">OWASP, NIST &amp; ISO mapped</p>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6 mb-15">
                            <div style="background: #ffffff; border: 1px solid #bcdbeb; border-radius: 10px; padding: 14px 16px; display: flex; align-items: center; gap: 12px; height: 100%; box-shadow: 0 2px 8px rgba(1, 61, 245, 0.04);">
                                <div style="width: 38px; height: 38px; border-radius: 8px; background: #d7f1fa; display: flex; align-items: center; justify-content: center; flex-shrink: 0; color: #013df5;">
                                    <i class="fas fa-tools" style="font-size: 16px;"></i>
                                </div>
                                <div>
                                    <h5 style="font-family: var(--font-heading, 'Outfit', sans-serif); font-size: 14.5px; font-weight: 700; color: #0e0e0e; margin: 0 0 2px 0; line-height: 1.3;">Actionable Fixes</h5>
                                    <p style="font-family: var(--font-default, 'Outfit', sans-serif); font-size: 12.5px; color: #64748b; margin: 0; line-height: 1.3;">Clear remediation roadmaps</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="col-lg-6 about-style-two">
                    <div class="thumb" style="padding-left: 0;">
                        <img src="assets/img/sln-img/vapt-hero.jpg" alt="VAPT Security Testing" class="vapt-hero-img">
                        <div class="shape">
                            <img src="assets/img/shape/anim-5.png" alt="Shape">
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- =============================================
         3. OUR VAPT SERVICES (Light Blue Section)
    ============================================= -->
    <div id="vapt-services" class="services-details-area overflow-hidden default-padding" style="background-color: #e6f3f9;">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2 text-center mb-40">
                    <h2 class="title" style="margin-top: 8px;">Our VAPT Services</h2>
                </div>
            </div>

            <div class="row">
                <!-- 01: Web App Pentest -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-globe"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">Web Application Penetration Testing</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Comprehensive security testing against OWASP Top 10, authentication bypass, injection flaws, and business logic vulnerabilities.
                        </p>
                    </div>
                </div>

                <!-- 02: Mobile App Pentest -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-mobile-alt"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">Mobile Application Penetration Testing</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Rigorous Android and iOS audits evaluating local data storage, API communications, reverse engineering, and cryptographic security.
                        </p>
                    </div>
                </div>

                <!-- 03: Network Pentest -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-network-wired"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">Network Penetration Testing</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Internal and external infrastructure testing detecting unpatched network services, misconfigured firewalls, and lateral movement paths.
                        </p>
                    </div>
                </div>

                <!-- 04: API Security Testing -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-code"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">API Security Testing</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Targeted evaluation of REST, SOAP, and GraphQL APIs against OWASP API Top 10, broken authorization (BOLA), and data exposure.
                        </p>
                    </div>
                </div>

                <!-- 05: Cloud Security Assessment -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-cloud"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">Cloud Security Assessment</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Multi-cloud configuration and architecture reviews across AWS, Azure, and GCP to resolve IAM privilege escalation and compliance gaps.
                        </p>
                    </div>
                </div>

                <!-- 06: AI Security Testing -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-service-card">
                        <div class="vapt-icon-box">
                            <i class="fas fa-brain"></i>
                        </div>
                        <h4 style="font-size: 19px; font-weight: 600; margin-bottom: 8px;">AI Security Testing</h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #666666; margin-bottom: 0;">
                            Specialized security testing for AI systems, applications, and APIs to identify prompt injection, data leakage, model evasion, and algorithmic vulnerabilities.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- =============================================
         4. SECURITY ASSESSMENT AREAS (White Section)
    ============================================= -->
    <div class="default-padding overflow-hidden">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2 text-center mb-40">
                    <h2 class="title" style="margin-top: 8px;">Security Assessment Areas</h2>
                </div>
            </div>

            <div class="row">
                <!-- Area 1 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-laptop-code"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Web Applications &amp; Portals</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Customer portals, enterprise SaaS platforms, e-commerce stores, and corporate web applications.
                        </p>
                    </div>
                </div>

                <!-- Area 2 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-mobile"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Mobile Applications</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Native Android (APK) and iOS (IPA) applications, hybrid frameworks, and local encrypted data storage.
                        </p>
                    </div>
                </div>

                <!-- Area 3 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-project-diagram"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">APIs &amp; Microservices</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            REST endpoints, GraphQL services, webhooks, microservices, and third-party data exchange interfaces.
                        </p>
                    </div>
                </div>

                <!-- Area 4 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-server"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Network Infrastructure</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Internal LAN/WAN perimeters, routers, corporate firewalls, VPN endpoints, and DNS configurations.
                        </p>
                    </div>
                </div>

                <!-- Area 5 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-cloud-upload-alt"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Cloud Environments</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            AWS, Microsoft Azure, Google Cloud Platform (GCP), and containerized Kubernetes clusters.
                        </p>
                    </div>
                </div>

                <!-- Area 6 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-area-item">
                        <div class="vapt-area-icon">
                            <i class="fas fa-wifi"></i>
                        </div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">IoT &amp; Connected Systems</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Smart telemetry sensors, embedded firmware, industrial automation hardware, and edge gateways.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- =============================================
         5. OUR VAPT APPROACH (Light Blue Section)
    ============================================= -->
    <div id="back-col" class="default-padding overflow-hidden" style="background-color: #d7f1fa;">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2 text-center mb-40">
                    <h2 class="title" style="margin-top: 8px;">Our VAPT Approach</h2>
                </div>
            </div>

            <div class="row">
                <!-- Step 01 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">01</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Planning &amp; Scoping</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Define target IP ranges, explicit rules of engagement, and testing windows to ensure zero operational disruption.
                        </p>
                    </div>
                </div>

                <!-- Step 02 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">02</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Information Gathering</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Map the organization's complete attack surface through OSINT intelligence, port scanning, and service enumeration.
                        </p>
                    </div>
                </div>

                <!-- Step 03 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">03</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Vulnerability Assessment</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Execute automated scanners alongside manual inspection to uncover security flaws, misconfigurations, and missing patches.
                        </p>
                    </div>
                </div>

                <!-- Step 04 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">04</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Penetration Testing</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Safely simulate real-world attacks to exploit vulnerabilities, demonstrate business risk, and eliminate false positives.
                        </p>
                    </div>
                </div>

                <!-- Step 05 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">05</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Analysis &amp; Reporting</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Synthesize test findings into actionable reports featuring executive scorecards, CVSS ratings, and proof of concept.
                        </p>
                    </div>
                </div>

                <!-- Step 06 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-step-card">
                        <div class="vapt-step-num">06</div>
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px;">Remediation &amp; Retesting</h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Assist development teams during patch implementation and conduct retesting to verify that all gaps are resolved.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>


    <!-- =============================================
         7. WHY VAPT MATTERS (Light Blue Section)
    ============================================= -->
    <div id="bg-col-2" class="default-padding overflow-hidden" style="background-color: #e6f3f9;">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2 text-center mb-40">
                    <h2 class="title" style="margin-top: 8px;">Why VAPT Matters</h2>
                </div>
            </div>

            <div class="row">
                <!-- Benefit 1 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-eye text-primary mr-2"></i> Identify Hidden Weaknesses
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Uncover software vulnerabilities and logic flaws before malicious adversaries can exploit them.
                        </p>
                    </div>
                </div>

                <!-- Benefit 2 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-compress-arrows-alt text-primary mr-2"></i> Reduce Attack Surface
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Harden systems by disabling unnecessary services and patching exposed endpoints across infrastructure.
                        </p>
                    </div>
                </div>

                <!-- Benefit 3 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-check-double text-primary mr-2"></i> Validate Security Controls
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Verify that firewalls, WAFs, and intrusion prevention mechanisms perform effectively under live attack scenarios.
                        </p>
                    </div>
                </div>

                <!-- Benefit 4 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-chart-line text-primary mr-2"></i> Improve Security Posture
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Gain clear visibility into organizational cyber defense maturity to guide targeted security investments.
                        </p>
                    </div>
                </div>

                <!-- Benefit 5 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-balance-scale text-primary mr-2"></i> Support Compliance
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Fulfill mandatory periodic audit requirements for ISO 27001, SOC 2, PCI-DSS, and regulatory directives.
                        </p>
                    </div>
                </div>

                <!-- Benefit 6 -->
                <div class="col-lg-4 col-md-6 mb-24">
                    <div class="vapt-benefit-card">
                        <h4 style="font-size: 18px; font-weight: 600; margin-bottom: 6px; color: var(--color-heading);">
                            <i class="fas fa-sort-amount-up text-primary mr-2"></i> Prioritize Remediation
                        </h4>
                        <p style="font-size: 14px; line-height: 22px; color: #666666; margin-bottom: 0;">
                            Enable engineering teams to direct urgent resources toward critical, high-impact risks first.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- =============================================
         8. VAPT + SOC CONNECTION (White Section)
    ============================================= -->
    <div class="default-padding overflow-hidden">
        <div class="container">
            <div class="row">
                <div class="col-lg-8 offset-lg-2 text-center mb-40">
                    <h2 class="title" style="margin-top: 8px;">How VAPT and SOC Complement Each Other</h2>
                </div>
            </div>

            <div class="row align-center">
                <!-- VAPT Side -->
                <div class="col-lg-6 mb-24">
                    <div class="vapt-soc-box">
                        <span class="vapt-soc-badge">Offensive Security</span>
                        <h4 style="font-size: 20px; font-weight: 600; margin-bottom: 10px; color: var(--color-heading);">
                            VAPT: Find &amp; Validate Weaknesses
                        </h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #555555; margin-bottom: 12px;">
                            Periodic evaluations that uncover hidden security gaps and test defenses before code deployment.
                        </p>
                        <ul class="vapt-check-list">
                            <li><i class="fas fa-check-circle"></i> Simulates adversary attack paths across systems</li>
                            <li><i class="fas fa-check-circle"></i> Uncovers flaws in code, configurations, and architecture</li>
                            <li><i class="fas fa-check-circle"></i> Delivers actionable developer fixes to patch vulnerabilities</li>
                        </ul>
                    </div>
                </div>

                <!-- SOC Side -->
                <div class="col-lg-6 mb-24">
                    <div class="vapt-soc-box" style="border-top: 4px solid #013df5;">
                        <span class="vapt-soc-badge">Defensive Security</span>
                        <h4 style="font-size: 20px; font-weight: 600; margin-bottom: 10px; color: var(--color-heading);">
                            SOC: Continuous Monitoring &amp; Response
                        </h4>
                        <p style="font-size: 14.5px; line-height: 24px; color: #555555; margin-bottom: 12px;">
                            24×7 live monitoring, SIEM log correlation, and rapid incident response to actively contain live threats.
                        </p>
                        <ul class="vapt-check-list">
                            <li><i class="fas fa-check-circle"></i> 24×7 real-time monitoring of logs, traffic, and endpoints</li>
                            <li><i class="fas fa-check-circle"></i> Real-time anomaly detection and threat intelligence correlation</li>
                            <li><i class="fas fa-check-circle"></i> Rapid incident containment and forensic remediation</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- =============================================
         9. FINAL CTA (Light Blue Section)
    ============================================= -->
    <div id="back-col" class="default-padding overflow-hidden"
        style="background-color: #d7f1fa; background-image: url(assets/img/shape/29.png); padding: 70px 0;">
        <div class="container">
            <div class="row">
                <div class="col-12">
                    <div class="vapt-cta-box">
                        <div class="row align-items-center">
                            <div class="col-lg-8 col-md-12 mb-20 mb-lg-0">
                                <h3 style="font-family: var(--font-heading, 'Outfit', sans-serif); font-size: 26px; font-weight: 700; color: var(--color-heading, #0e0e0e); margin-bottom: 12px;">
                                    Strengthen Your Security Before Attackers Do
                                </h3>
                                <div style="display: flex; flex-wrap: wrap; gap: 8px 25px; font-size: 14.5px; color: #334155;">
                                    <span class="d-inline-block">
                                        <i class="fas fa-envelope mr-2" style="color: #013df5;"></i> <strong>srinivas.c@slnconsulting.co.in</strong>
                                    </span>
                                    <span class="d-inline-block">
                                        <i class="fas fa-phone mr-2" style="color: #013df5;"></i> <strong>+91 9940196195</strong>
                                    </span>
                                </div>
                            </div>
                            <div class="col-lg-4 col-md-12 text-lg-right text-center">
                                <a href="contact.php" class="btn btn-theme secondary btn-md animation" style="padding: 14px 28px; font-size: 15px; font-weight: 600;">
                                    Reach Us Now <i class="fas fa-arrow-right ml-2"></i>
                                </a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

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

</body>

</html>
