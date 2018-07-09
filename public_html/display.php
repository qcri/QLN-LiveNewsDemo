<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="scroll.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="icon" type="image/png" href="favicon.gif">
    <link rel="stylesheet" type="text/css" href="navbar.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <title>News Source</title>
    <style>
    .msize {
        width:95%;
        height:95%;
        position:absolute;
    }
    .heading {
        color: #428bca;
        font-family: "Times New Roman", Times, serif;
        font-size: 35px;
        font-weight: bold;
    }
    .sm_heading {
        color: #428bca;
        font-family: "Times New Roman", Times, serif;
        font-weight: bold;
    }
    .desc {
        font-size: 20px;
        font-family: "Times New Roman", Times, serif;
    }
    ul.social-network {
    list-style: none;
    display: inline;
    margin-left: 0 !important;
    padding: 0;
    }
    @media (max-width: 769px){
    .social-circle li a {
    display: inline-block;
    position: relative;
    margin: 0 auto 10px auto;
    border-radius: 19px;
    text-align: center;
    width: 38px;
    height: 38px;
    font-size: 16px;
    -moz-border-radius: 19px;
    -webkit-border-radius: 19px;
    }
    .social-circle li a {
    display: inline-block;
    position: relative;
    margin: 0 auto 10px auto;
    -moz-border-radius: 25px;
    -webkit-border-radius: 25px;
    border-radius: 25px;
    text-align: center;
    width: 50px;
    height: 50px;
    font-size: 20px;
    
    }
    }
    .gsize {
    font-size: 35px;
    }
    .lii {
        float:left;
    }
    @media only screen and (min-width: 768px) {
    table.tres { 
        width:40%; 
    }
    @media only screen and (min-width: 768px) {
    table.t1res { 
        width:60%; 
    }
    }
}
    </style>
    
</head>
<body style="bgcolor:"#a2a276"">
<nav class="navbar navbar-dark bg-dark justify-content-between">
         <a style="float:left;left:0px;margin-right:auto;" class="heading navbar-brand" href='index.php'>Live News</a>
</nav>
    <?php
    include 'dbconnection.php';
    $id= $_GET["id"];
    ?>
    <?php 
        $sql = "SELECT * FROM news_arabic WHERE user_id='$id'"; 
        $rs = $conn->query($sql);
        $row = mysqli_fetch_array($rs);
    ?>
        <div class="container" >
            <ul class="nav nav-tabs">
                <li class="active"><a data-toggle="tab" href="#home">Home &ensp;<span style="float:right;">
                                <i style="color:black;font-size: 25px;" class="fa fa-home">
                                </i></span></a></li>
                <li><a data-toggle="tab" href="#menu1">Wikipedia &ensp;<span style="float:right;">
                <img align="left" style="width: 25px; height:25px;" src="wiki.png">
                                </span></a></li>
                <li><a data-toggle="tab" href="#menu2">Website  &ensp;<span style="float:right;">
                <img align="left" style="width: 25px; height:25px;" src="<?php echo $row["user_profile_image_url"]?>">
                </span></a></li>
                <li><a data-toggle="tab" href="#menu3">RSS Feed &ensp;<span style="float:right;">
                                <i style="color: orange;font-size: 25px;" class="fa fa-rss-square"></i></span></a></li>
            </ul>

            <div class="tab-content">
                <div id="home" class="tab-pane fade in active">
                    <img align="left" style="width: 55px; height:55px;" src="<?php echo $row["user_profile_image_url"]?>"> 
                    <h3 class="heading"><?php echo $row["user_name"]?></h3>  
                    <hr>
                    <p class="desc"><u>Description:</u>&ensp;<?php echo $row["user_description"]?></p>
                    <br>
                    <center>
                    <center>
                    <div style="width:100%;"  class="tres table-responsive">
                        <table class="tres desc table table-striped">
                            <tr>
                                <td>Country:</td>
                                <td>
                                <?php
                                echo $row["country"];
                                $flag= strtolower($row["country_code"]);
                                $flag.=".svg";
                                $f_path="flags\\".$flag;
                                ?><span style="float:right;">
                                <img style="width:35px;height:35px;" src="<?php echo $f_path ?>">
                                </span>
                                </td>
                            </tr>
                            <tr>
                                <?php 
                                $cat= $row["Category"];
                                if (strcmp($cat,'General')==0)
                                {
                                    $fcat='General';
                                    $gicon='fa fa-globe';
                                }
                                if (strcmp($cat,'Sports')==0)
                                {
                                    $fcat='Sports';
                                    $gicon='fa fa-soccer-ball-o';
                                }
                                if (strcmp($cat,'Entertainment')==0)
                                {
                                    $fcat='Entertainment';
                                    $gicon='fa fa-tv';
                                }
                                if (strcmp($cat,'Science')==0)
                                {
                                    $fcat='Science';
                                    $gicon='fa fa-cogs';
                                }
                                if (strcmp($cat,'Health')==0)
                                {
                                    $fcat='Health';
                                    $gicon='fa fa-medkit';
                                }
                                if (strcmp($cat,'Economy')==0)
                                {
                                    $fcat='Economy';
                                    $gicon='fa fa-money';
                                }
                                ?>
                                <td>Category:</td>
                                <td><?php echo $cat?><span style="float:right;">
                                <i class="gsize <?php echo $gicon?>"></i></span></td>
                            </tr>
                        </table>
                    </div>
                    <h3 class="sm_heading">Social Media Profiles</h3>
                    <p><u>click on icons to see page</u></p>
                    <div style="width:100%;"  class="t1res table-responsive">
                    <table class="t1res desc table table-striped">
                    <tr>
                    <td>Facebook:</td>
                    <td>12345 friends</td>
                    <td>
                    <?php $fb= "https://www.facebook.com/".$row["Facebook Page (https://www.facebook.com/)"]?>
                            <a href=<?php echo $fb ?> target="_blank" class="icoFacebook" title="Facebook">
                            <i style="color: rgb(59, 89, 152);" class="gsize fa fa-facebook-square"></i></a>
                    </td>
                    </tr>
                    <tr>
                    <td>Twitter:</td>
                    <td><?php echo $row["user_followers_count"]?> followers</td>
                    <td>
                    <?php $tw="https://twitter.com/".$row["user_screen_name"] ?>
                            <a href=<?php echo $tw ?> target="_blank" class="icoTwitter" title="Twitter">
                            <i style="color: #00aced;" class="gsize fa fa-twitter-square"></i></a>
                    </td>
                    </tr>
                    <tr>
                    <td>Amazon Alexa:</td>
                    <td>12345 rank</td>
                    <td>
                    <?php $alexa="https://www.alexa.com/siteinfo/".$row["Alexa page (https://www.alexa.com/siteinfo/)"] ?>
                            <a href=<?php echo $alexa ?> target="_blank" class="icoWikipedia" title="Alexa">
                            <i style="color: #000000;" class="gsize fa fa-amazon"></i></a>
                    </td>
                    </tr>
                    <tr>
                    <td>YouTube:</td>
                    <td>12345 subscribers</td>
                    <td>
                    <?php $youtube="http://www.youtube.com/".$row["YouTube (http://www.youtube.com/)"] ?>
                        <?php if(strcmp($row["YouTube (http://www.youtube.com/)"],'')==0) { ?>
                            <a href=# class="icoWikipedia" title="YouTube link not found">
                            <i style="color: grey" class="gsize fa fa-youtube-play"></i></a>
                        <?php } else {?>
                            <a href=<?php echo $youtube ?> target="_blank" class="icoWikipedia" title="YouTube">
                            <i style="color: red" class="gsize fa fa-youtube-play"></i></a>
                        <?php }?>
                    </td>
                    </tr>
                    <tr>
                    <td>Google+:</td>
                    <td>12345 connections</td>
                    <td>
                    <?php $google="https://plus.google.com/".$row["GooglePlus (https://plus.google.com/)"] ?>
                            
                            <?php if(strcmp($row["GooglePlus (https://plus.google.com/)"],'')==0) { ?>
                            <a href=#  class="icoWikipedia" title="Google+ link not found">
                            <img style="width:35px; height:35px" src="google-plus-bnw.jpg"></a>
                            <?php } else {?>
                            <a href=<?php echo $google ?> target="_blank" class="icoWikipedia" title="Google+">    
                            <img style="width:35px; height:35px" src="googleplus.png"></a>
                            <?php } ?>

                    </td>
                    </tr>
                    <tr>
                    <td>Instagram:</td>
                    <td>12345 followers</td>
                    <td>
                    <?php $instagram="https://www.instagram.com/".$row["Instagram (https://www.instagram.com/)"] ?>
                    <?php if(strcmp($row["YouTube (http://www.youtube.com/)"],'')==0) { ?>
                        <a href=# class="icoWikipedia" title="Instagram link not found">
                            <img style="width:35px; height:35px" src="instagram-bw.png"></a>
                    <?php } else { ?>
                            <a href=<?php echo $instagram ?> target="_blank" class="icoWikipedia" title="Instagram">
                            <img style="width:35px; height:35px" src="instagram.png"></a>
                    <?php } ?>
                    </td>
                    </tr>
                    </table> 
                    </div>
                </div>
                <div id="menu1" class="tab-pane fade msize">
                    <?php $wiki="https://ar.wikipedia.org/wiki/".$row["Wikipedia page (https://ar.wikipedia.org/wiki/)"] ?>
                    <iframe src=<?php echo $wiki?> 
                    height=95% width=95% frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
                </div>
                <div style="align:left;" id="menu2" class="tab-pane fade msize">
                    <iframe src="<?php echo $row["user_expanded_url"]?>" 
                    height=95% width=95% frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
                </div>
                <div id="menu3" class="tab-pane fade msize">
                    <?php 
                    $rss=$row["RSS Feed link"];
                    if($row["RSS Feed link"]=='-')
                    {
                        echo "<h2 style=\"text-color:red;\">RSS Feed Unavailable</h2>";
                        $rss=$row["user_expanded_url"];
                    } ?>
                    <iframe src="<?php echo $rss ?>" 
                    height=95% width=95% frameborder="0" gesture="media"  allowfullscreen></iframe>
                </div>
            </div>
        </div>


</body>
</html>