<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <style>
        .mobile-nav {
            background: #555;
            color: #fff;
            display: none;
            justify-content: space-between;
            align-items: center;
            height: 35px;
            padding: 20px;
            font-size: 20px;
        }

        .mobile-nav .nav-btn {
            cursor: pointer;
        }

        .nav {
            background: cornflowerblue;
        }

        ul {
            list-style: none;
            display: flex;
            background: cornflowerblue;
        }

        ul li a,
        ul li {
            cursor: pointer;
            font-size: 20px;
            text-decoration: none;
        }

        ul li {
            display: block;
        }

        ul li a {
            padding: 15px 25px;
            background: cornflowerblue;
            color: #fff;
            display: block;
        }

        li a:hover {
            background-color: #ccc3;
            color: #111;
        }

        ul li ul {
            background: #555;
            padding-left: 5px;
            position: absolute;
            width: 10em;
            display: none;
        }

        li ul li a {
            padding: 10px;
            background: #555;
            color: #fff;
        }

        li ul li a:hover {
            background: #555;
        }

        ul li ul li {
            position: relative;
        }

        ul li ul li ul {
            position: absolute;
            top: 5px;
            left: 100%;
        }

        li:hover>ul,
        li:active>ul {
            display: block;
        }

        .dropdown {
            position: relative;
        }

        .dropdown>a,
        .dropdown>a:hover,
        .dropdown.active>a,
        .dropdown.active>a:hover {
            background: url("https://i.postimg.cc/y8b7mfcJ/arrow.png");
            background-position: right;
            background-size: 15px;
            background-repeat: no-repeat;
            color: #fff;
        }

        @media screen and (max-width: 768px) {
            .mobile-nav {
                display: flex;
            }

            ul.nav {
                visibility: hidden;
                transform: translateY(-120%);
                opacity: 0;
                transition: 0.5s ease-in-out;
            }

            ul.nav.toggle {
                visibility: visible;
                transform: translateY(0);
                opacity: 1;
            }

            ul {
                flex-direction: column;
            }

            ul li {
                overflow: hidden;
                border: none;
            }

            ul li ul {
                position: relative;
                width: 90%;
                padding: 0 5%;
                transform: translateX(-100%);
                display: block;
                visibility: hidden;
                height: 0;
                overflow: hidden;
                transition: transform 400ms ease;
            }

            ul li ul li ul {
                position: initial;
                background: #555;
                top: 0;
                width: 96%;
                padding: 0 2%;
            }

            li:hover>ul,
            li:active>ul {
                display: block;
            }

            li.active>ul {
                transform: translateX(0);
                visibility: visible;
                height: 100%;
            }

            .dropdown>a,
            .dropdown>a:hover,
            .dropdown.active>a,
            .dropdown.active>a:hover {
                background-position: 95% 50%;
            }
        }
    </style>


    <div class="container">
        <nav>
            <div class="mobile-nav">
                <span>Menu</span>
                <div class="nav-btn">
                    <i class="fas fa-bars"></i>
                </div>
            </div>

            <ul class="nav">
                <li>
                    <a href="#">Home</a>
                </li>

                <li class="dropdown">
                    <a href="#">Gallery</a>
                    <ul>
                        <li>
                            <a href="#">Gallery A</a>
                        </li>
                        <li>
                            <a href="#">Gallery B</a>
                        </li>
                    </ul>
                </li>








                <li class="dropdown">
                    <a href="#">Our Offering</a>
                    <ul>
                        <li class="dropdown">
                            <a href="#">Skilling Solutions</a>
                            <ul>
                                <li class="dropdown">
                                    <a href="#">Services-1</a>
                                </li>
                                <li>
                                    <a href="#">Services-2</a>
                                </li>
                            </ul>
                        </li>
                        <li><a href="cambridge.php">Cambridge Learning </a></li>
                        <li><a href="nure-campus.php">NuRe Campus</a></li>
                        <li><a href="it-service.php">IT Services</a></li>
                    </ul>
                </li>













                <li>
                    <a href="#">About</a>
                </li>
            </ul>
        </nav>
    </div>
    <script>
        const li = document.querySelectorAll('li.dropdown a');
        const btn = document.querySelector('.nav-btn');
        const nav = document.querySelector('ul.nav');

        btn.addEventListener('click', e => {
            nav.classList.toggle('toggle');
        })


        li.forEach((each) => {
            if (each.nextElementSibling !== null) {
                each.addEventListener('click', e => {
                    if (window.innerWidth < 768) {
                        e.target.parentElement.classList.toggle("active");
                    }
                })
            }
        })
    </script>

</body>


</html>