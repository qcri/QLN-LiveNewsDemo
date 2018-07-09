<?php
   include 'dbconnection.php';
   ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Site Anatomy</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" type="image/png" href="favicon.gif">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="navbar.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
  <style>
           .heading {
         font-family: "Times New Roman", Times, serif;
         font-weight: bold;
         font-size:30px;
         color:#428bca;
           }
           .desc {
         font-size: 20px;
         font-family: "Times New Roman", Times, serif;
         font-weight:bold;
         }
         .t_desc {
         font-size: 22px;
         font-weight:bold;
         text-decoration: underline;
         font-family: "Times New Roman", Times, serif;
         }
         .gsize {
          font-size: 25px;
          }
          thead {
            color:#428bca;
            
          }
  </style>
</head>
<center>
<nav class="navbar navbar-dark bg-dark justify-content-between">
         <a style="float:left;left:0px;margin-right:auto;" class="heading navbar-brand" href='index.php'>Live News</a>
</nav>
<div class="container">  
<h2 class="heading">English Site Statistics</h2>
<hr>
<?php

    $total_count=$conn->query("SELECT * FROM news_english");
    $total_count_row=mysqli_num_rows($total_count);


    $twitter_count=$conn->query("SELECT distinct user_name FROM news_english");
    $twitter_count_row=mysqli_num_rows($twitter_count);
    $twitter_count_val=round(($twitter_count_row/$total_count_row)*100,0);

    $facebook_count=$conn->query("SELECT distinct `Facebook Page (https://www.facebook.com/)` FROM news_english");
    $facebook_count_row=mysqli_num_rows($facebook_count)-1;
    $facebook_count_val=round(($facebook_count_row/$total_count_row)*100,0);
    

    $rss_count=$conn->query("SELECT distinct `RSS Feed link` FROM news_english");
    $rss_count_row=mysqli_num_rows($rss_count)-1;
    $rss_count_val=round(($rss_count_row/$total_count_row)*100,0);


    $wiki_count=$conn->query("SELECT distinct `Wikipedia page (https://en.wikipedia.org/wiki/)` FROM news_english");
    $wiki_count_row=mysqli_num_rows($wiki_count)-1;
    $wiki_count_val=round(($wiki_count_row/$total_count_row)*100,0);


    $alexa_count=$conn->query("SELECT distinct `Alexa page (https://www.alexa.com/siteinfo/)` FROM news_english");
    $alexa_count_row=mysqli_num_rows($alexa_count)-1;
    $alexa_count_val=round(($alexa_count_row/$total_count_row)*100,0);


    $yt_count=$conn->query("SELECT distinct `YouTube (http://www.youtube.com/)` FROM news_english");
    $yt_count_row=mysqli_num_rows($yt_count)-1;
    $yt_count_val=round(($yt_count_row/$total_count_row)*100,0);


    $gp_count=$conn->query("SELECT distinct `GooglePlus (https://plus.google.com/+)` FROM news_english");
    $gp_count_row=mysqli_num_rows($gp_count)-1;
    $gp_count_val=round(($gp_count_row/$total_count_row)*100,0);


    $insta_count=$conn->query("SELECT distinct `Instagram (https://www.instagram.com/)` FROM news_english");
    $insta_count_row=mysqli_num_rows($insta_count)-1;
    $insta_count_val=round(($insta_count_row/$total_count_row)*100,0);

                    
?>
<h4 class="t_desc">Social Media Profile</h4>        
  <table style="width:50%;border:2px #eee solid;" class="desc table table-striped">
    <tbody>
    <tr>
         <td>Total News Sources</td>
         <td><?php echo $total_count_row ?> sources</td>
    </tr>
    <tr>
         <td>&ensp; Twitter Accounts
         <span style="float:left">
         <i style="color: #00aced;" class="gsize fa fa-twitter-square"></i>
         </span>
         </td>
         <td><?php echo $twitter_count_row ?>&ensp;(<?php echo $twitter_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; Facebook Accounts
         <span style="float:left">
         <i style="color: rgb(59, 89, 152);" class="gsize fa fa-facebook-square"></i>
         </span>
         </td>
         <td><?php echo $facebook_count_row ?>&ensp;(<?php echo $facebook_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; Alexa Page Information
         <span style="float:left">
         <i style="color: #000000;" class="gsize fa fa-amazon"></i>
         </span>
         </td>
         <td><?php echo $alexa_count_row ?>&ensp;(<?php echo $alexa_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; Instagram Accounts
         <span style="float:left">
         <img style="width:25px; height:25px" src="instagram.png">
         </span>
         </td>
         <td><?php echo $insta_count_row ?>&ensp;(<?php echo $insta_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; YouTube Accounts
         <span style="float:left">
         <i style="color: red" class="gsize fa fa-youtube-play"></i>
         </span>
         </td>
         <td><?php echo $yt_count_row ?>&ensp;(<?php echo $yt_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; Google Plus Accounts
         <span style="float:left">
         <img style="width:25px; height:25px" src="googleplus.png">
         </span>
         </td>
         <td><?php echo $gp_count_row ?>&ensp;(<?php echo $gp_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; Wikipedia Pages
         <span style="float:left;">
         <img align="left" style="width: 25px; height:25px;" src="wiki.png">
         </span>
         </td>
         <td><?php echo $wiki_count_row ?>&ensp;(<?php echo $wiki_count_val?>%)</td>
    </tr>
    <tr>
         <td>&ensp; RSS Feeds
         <span style="float:left;">
        <i style="color: orange;font-size: 25px;" class="fa fa-rss-square"></i></span>
         </td>
         <td><?php echo $rss_count_row ?>&ensp;(<?php echo $rss_count_val?>%)</td>
    </tr>

    </tbody>
</table>    
<?php
$sql_country_count="SELECT COUNT(country), country,country_code from news_english GROUP BY country, country_code ORDER BY `COUNT(country)` DESC";
$result_country_count = $conn->query($sql_country_count);
$i=0;
?> 
<h4 class="t_desc">News sources per country</h4>        
  <table style="width:50%;border:2px #eee solid;" class="desc table table-striped">
    <thead>
      <tr>
        <th>Country</th>
        <th>News Sources</th>
      </tr>
    </thead>
    <tbody>
            <?php
    while ($row_country_count = $result_country_count->fetch_assoc())
        {
            $country_name[]=$row_country_count["country"];
            $country_count[]=$row_country_count["COUNT(country)"];
            $country_percent[]=round(($row_country_count["COUNT(country)"]/$total_count_row)*100,0);
            $flag= strtolower($row_country_count["country_code"]);
            $flag.=".svg";
            $f_path="flags\\".$flag;
            ?>
            <tr>
                    <td>&ensp; <?php echo $country_name[$i]?>
                    <span style="float:left;">
                    <img style="width:25px;height:25px;" src="<?php echo $f_path ?>">
                    </span>                    
                    </td>
                    <td><?php echo $country_count[$i]?> (<?php echo $country_percent[$i]?>%)</td>
                    
              </tr>
        <?php
                    $i++;
        }

    echo"</table>";                    
    ?>

    <!-- count of sources per category-->
    <?php
    $sql_category_count="SELECT COUNT(category), Category from news_english GROUP BY Category ORDER BY COUNT(category) DESC";
    $result_category_count = $conn->query($sql_category_count);
    $i=0;
    ?>
<h4 class="t_desc">News sources per category</h4>        
  <table style="width:50%;border:2px #eee solid;" class="desc table table-striped">
    <thead>
      <tr>
        <th>Category</th>
        <th>News Sources</th>
      </tr>
    </thead>
    <tbody>
    <?php
    while ($row_category_count = $result_category_count->fetch_assoc())
        {
            $category_name[]=$row_category_count["Category"];
            $category_count[]=$row_category_count["COUNT(category)"];
            $category_percent[]=round(($row_category_count["COUNT(category)"]/$total_count_row)*100,0);

            $cat= $category_name[$i];
            if (strcmp($cat,'General')==0)
            {
                $fcat='General';
                $gicon='fa fa-globe';
            }
            if (strcmp($cat,'Sport')==0)
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

            <tr>
                    <td>&ensp; <?php echo $category_name[$i]?>
                    <span style="float:left;">
                    <i class="gsize <?php echo $gicon?>"></i></span>
                    </td>
                    <td><?php echo $category_count[$i]?> (<?php echo $category_percent[$i]?>%)</td>
                    
                    </tr> 
        <?php 
                    $i++;
        } ?>
        <tr>
                    <td>&ensp; Health
                    <span style="float:left;">
                    <i class="gsize fa fa-medkit"></i></span>
                    </td>
                    <td>0 (0%)</td>
                    
                    </tr> 
<?php
    echo"</table>";                    
    ?>
    </center>