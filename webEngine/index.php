<!--
    @author
        Jeong Han
    @library
        bootstrap CDN
    @date
        2018.01.22
    @title
        Web for Image Classification
-->
<!-- bootstrap theme "Cyborg"-->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootswatch/4.0.0-beta.3/cyborg/bootstrap.min.css">
<style>
    .title{
        font-size:3rem;
        font-weight:300;
        line-height:1.2
    }
    .subtitle{
        font-size:2rem;
        font-weight:200
    }
    .continue {
        font-weight: bold;
        padding-left: 10px;
        padding-right: 10px;
        padding-top: 7px;
        padding-bottom: 7px;
    }
</style>
<html>
    <head>
        <meta charset-"utf-8">
    </head>
    <body>
        <!-- Menu Bar Area -->
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <!-- Title Menu -->
            <a class="navbar-brand" href="./index.php">
                "Web for Image Classification EX"
            </a>
        </nav>
        <!-- Title Area -->
        <div class="jumbotron text-center">
            <!-- Title -->
            <h1 class="title"> title </h1>
            <!-- Subtitle -->
            <p class="subtitle"> subtitle </p>
        </div>
        <!-- Main Page Area -->
        <div class="container">
            <!-- CountDown 60sec Script
                 ref : https://stackoverflow.com/questions/31106189/create-a-simple-10-second-countdown -->
            <p class="text-right"><span id="countdowntimer"> 60 </span> Seconds later</p>
            <script type="text/javascript">
                var timeleft = 60;
                var countdown = setInterval(function(){
                    timeleft--;
                    document.getElementById("countdowntimer").textContent = timeleft;
                    if(timeleft <= 0)
                        clearInterval(countdown);
                },1000);
            </script>
            <!-- Center Frame -->
            <div class="row">
                <!-- Image Area -->
                <div class="col-12 col-md-9">
                    <!-- Image Box -->
                    <div class="card bg-light my-4 p-4 text-center">
                        <div class="row">
                            <!-- Tag Input Box -->
                            <form name="Tagtext" action="./index.php" method="post" onsubmit="return validate(this);">
                                <div>Answer:
                                    <input type="text" name="tag" id="tag" size="100" /> &nbsp;
                                    <!-- Continue Button -->
                                    <input type="submit" value="Continue" id="continueButton" class="continue" /> &nbsp;
                                </div>
                            </form>
                            <script type="text/javascript">
                                document.Tagtext.tag.focus();
                            </script>
                        </div>
                    </div>
                </div>
                <!-- Recommend Tag Area -->
                <div class="col-12 col-md-3">
                    <div class="row">
                        <!-- Recommend Tag Box -->
                        <div class="col-12 d-none d-lg-block">
                            <div class="card bg-light text-center">
                                Recommend Tag Area
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Tail Text Area -->
        <footer class="mt-5 py-4 text-center">
            <div class="container">
                <div class="row">
                    <div class="col-12">
                    </div>
                </div>
            </div>
        </footer>
    </body>
</html>