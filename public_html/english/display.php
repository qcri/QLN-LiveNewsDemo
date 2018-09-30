<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>

    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" type="text/css" href="scroll.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <link rel="icon" type="image/png" href="favicon.gif">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
    <link rel="stylesheet" type="text/css" href="navbar.css">
    <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
    <script src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
    <script src="morris.js"></script>
    <style>
    .morris-hover{position:absolute;z-index:1000;}.morris-hover.morris-default-style{border-radius:10px;padding:6px;color:#666;background:rgba(255, 255, 255, 0.8);border:solid 2px rgba(230, 230, 230, 0.8);font-family:sans-serif;font-size:12px;text-align:center;}.morris-hover.morris-default-style .morris-hover-row-label{font-weight:bold;margin:0.25em 0;}
    .morris-hover.morris-default-style .morris-hover-point{white-space:nowrap;margin:0.1em 0;}
    </style>
      <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>

      <script type="text/javascript">
            var google_charts_ready = false;
            google.charts.load('current', {'packages':['gauge']});
            google.charts.setOnLoadCallback(function() {google_charts_ready = true});

          function drawCerntalityChart(val1,val2,val3,val4,val5,val6,val7,divid) {
              if (google_charts_ready == false) {
                return setTimeout(function() { drawCerntalityChart(val1,val2,val3,val4,val5,val6,val7,divid)}, 1000);
              }
              var data = google.visualization.arrayToDataTable([
                ['Label', 'Value'],
                ['PScore', (val3/2+val4+val5/2)*100],
              ]);

              var options = {
                width: 280, height: 110,
                redFrom: 80, redTo: 100,
                yellowFrom:50, yellowTo: 80,
                greenFrom:0, greenTo:50,
                minorTicks: 5
              };
              var chart = new google.visualization.Gauge(document.getElementById(divid));
              chart.draw(data, options);
          }

          function drawHyperPartisanshipChart(val1,val2,val3,val4,val5,val6,val7,divid) {
              if (google_charts_ready == false) {
                return setTimeout(function() { drawHyperPartisanshipChart(val1,val2,val3,val4,val5,val6,val7,divid)}, 1000);
              }
              var data = google.visualization.arrayToDataTable([
                ['Label', 'Value'],
                ['PScore', (val1+val2+val6+val7)*100],
              ]);

              var options = {
                width: 280, height: 110,
                redFrom: 80, redTo: 100,
                yellowFrom:50, yellowTo: 80,
                greenFrom:0, greenTo:50,
                minorTicks: 5
              };
              var chart = new google.visualization.Gauge(document.getElementById(divid));
              chart.draw(data, options);
          }

      </script>
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
        $sql = "SELECT * FROM news_english WHERE user_id='$id'"; 
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
                <li><a data-toggle="tab" href="#menu4">Sentiment Analysis &ensp;<span style="float:right;">
                <i style="color: black;font-size: 25px;" class="fa fa-bolt"></i></span></a></li>
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
                                $factscores = explode(" ", $row["fact_predictions"]);
                                
                                $factlabels = explode(" ","low mixed high");
                                $biasscores = explode(" ",$row["bias_predictions"]);
                                $biaslabels = explode(" ", "extreme-right right right-center center left-center left extreme-left");
                                $bias3scalescores = array(($biasscores[0]+$biasscores[1]+$biasscores[2]/2),($biasscores[2]/2+$biasscores[3]+$biasscores[4]/2),($biasscores[4/2]+$biasscores[5]+$biasscores[6]));
                                $bias3scalelabels = explode(" ", "right center left");
                                $factscores_chart_data="";
                                for ($i = 0; $i < count($factscores); $i++)
                                    $factscores_chart_data .= "{x: '".$factlabels[$i]."', y: ".$factscores[$i]."},";
                                #$factscores_chart_data = "[".$factscores_chart_data."]";
                                $biasscores_chart_data="";
                                for ($i = 0; $i < count($biasscores); $i++)
                                    $biasscores_chart_data .= "{x: '".$biaslabels[$i]."', y: ".$biasscores[$i]."},";
                                $bias3scalescores_chart_data="";
                                for ($i = 0; $i < count($bias3scalescores); $i++)
                                    $bias3scalescores_chart_data .= "{x: '".$bias3scalelabels[$i]."', y: ".$bias3scalescores[$i]."},";
                                #$biasscores_chart_data = "[".$biasscores_chart_data."]";
                                #echo " Fact Score: ".$factscores_chart_data."<br/>";
                                #echo " Bias Score: ".$biasscores_chart_data."<br/>";
                                if (strcmp($cat,'General')==0)
                                {
                                    $gicon='fa fa-globe';
                                }
                                if (strcmp($cat,'Sport')==0)
                                {
                                    $gicon='fa fa-soccer-ball-o';
                                }
                                if (strcmp($cat,'Entertainment')==0)
                                {
                                    $gicon='fa fa-tv';
                                }
                                if (strcmp($cat,'Science')==0)
                                {
                                    $gicon='fa fa-connectdevelop';
                                }
                                if (strcmp($cat,'Health')==0)
                                {
                                    $gicon='healing';
                                }
                                if (strcmp($cat,'Economy')==0)
                                {
                                    $gicon='fa fa-money';
                                }
                                ?>
                                <td>Category:</td>
                                <td><?php echo $cat?><span style="float:right;">
                                <i class="gsize <?php echo $gicon?>"></i></span></td>
                            </tr>
                            <tr>
                            <td>Factuality:
                            </td>
                            <td><?php echo $row["Truthiness"]?>, <?php echo $row["is_factual"]?>  <div style='align:right;position:relative;width:500px;height:150px;' id='factchart'>
                            </td>
                            </tr>
                            <tr>
                            <td>Bias:
                            </td>
                            <td><?php echo $row["bias"]?> <div style='position:relative;width:500px;height:250px;' id='biaschart'></div>
                            </td>
                            </tr>
                            <tr>
                            <td>Bias:
                            </td>
                            <td><?php echo $row["bias"]?> <div style='position:relative;width:500px;height:180px;' id='bias3scalechart'></div>
                            </td>
                            </tr> 
                            <tr style="border-bottom: thin ridge;">
                            <td>Political Stance: 
                            </td>
                            <td >
                            <?php 
                            echo "<br/><table class='ranktable' border='0px' align='center'><tr>";
                            echo "<td width='180px' align='center' style='padding: 5px 10px 5px 5px;'><span id='CerntalityChart' name='CerntalityChart'  title=\"Centrality\">&nbsp;<script>drawCerntalityChart($biasscores[0],$biasscores[1],$biasscores[2],$biasscores[3],$biasscores[4],$biasscores[5],$biasscores[6],'CerntalityChart');</script></span><br>Centrality</td>";
                            echo "<td  width='180px' align='center' style='padding: 5px 10px 5px 5px;'><span id='PartisanshipChart' name='PartisanshipChart'  title=\"Hyper-Partisanship\">&nbsp;<script>drawHyperPartisanshipChart($biasscores[0],$biasscores[1],$biasscores[2],$biasscores[3],$biasscores[4],$biasscores[5],$biasscores[6],'PartisanshipChart');</script></span><br>Hyper-Partisanship</td>";
                            echo "</tr></table>";
                            ?>
                        </td>
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
                    <td><?php echo $row["alexa_rank"]?> rank</td>
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
                    <?php $google="https://plus.google.com/+".$row["GooglePlus (https://plus.google.com/+)"] ?>
                            
                            <?php if(strcmp($row["GooglePlus (https://plus.google.com/+)"],'')==0) { ?>
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
                    <?php $wiki=$row["Wikipedia page (https://en.wikipedia.org/wiki/)"] ?>
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
                    if($row["RSS Feed link"]=='')
                    {
                        echo "<h2 style=\"text-color:red;\">RSS Feed Unavailable</h2>";
                        $rss=$row["user_expanded_url"];
                    } ?>
                    <iframe src="<?php echo $rss ?>" 
                    height=95% width=95% frameborder="0" gesture="media"  allowfullscreen></iframe>
                </div>
                <div style="position:absolute;width:90vw;height:800vh;" id="menu4" class="tab-pane fade msize">
                <div>
                <img align="left" style="width: 55px; height:55px;" src="<?php echo $row["user_profile_image_url"]?>"><h3 class="heading"><?php echo $row["user_name"]?></h3>
                </div>
                <hr>
                <?php
                $t_name= $row["user_screen_name"];
                $t_array = array("ajenglish", "AlArabiya_Eng", "BBCWorld", "BreitbartNews","cnni","foxnews","nytimes","reuters","TheEconomist");
		if (in_array($t_name, $t_array)) {
                    echo "<div style='position:relative;width:60vw;height:750vh;' id='chart'>";
                    echo "</div>";
                    $query="SELECT * FROM sentiment WHERE sentiment.user_screen_name='".$t_name."'";                    $result= mysqli_query($conn,$query);
                    $arr = [];
                    $inc = 0;
                    while ($row=mysqli_fetch_array($result))
                    {
                        $jsonArrayObject = (array('entities' => $row["Entities"], 'negative' => (int)$row["negative"], 'positive' => (int)$row["positive"], 'neutral' => (int)$row["neutral"]));
			$arr[$inc] = $jsonArrayObject;
                        $inc++;
                    }
                    $chart_data= json_encode($arr);
                }
                else {
                    echo "Report Unavailable";
                } 
		?>
                </div>
            </div>
        </div>


</body>
</html>
<script>

    var homeBar= Morris.Bar ({
        element: 'chart',
        data:<?php echo $chart_data ?>,
        xkey: 'entities',
        ykeys:['negative', 'neutral', 'positive'],
        ymax:100,
        labels:['Negative', 'Neutral', 'Positive'],
        barColors: ["#B21516", "#999999", "#1f7a1f"],
        hideHover:'auto',
        horizontal:true,        
        stacked: true,
        gridTextColor: '#000',
        gridTextSize: 15,
        resize:true
    });
 
    
</script>
<script>
   //var $arrColors = ['#34495E', '#26B99A',  '#666', '#3498DB',"#008080", "#800080", "#000800"];
    var $arrColors = ['#461420', '#584738', '#859863', '#F0CE86', '#DD2D2C', '#18845F', '#72529D', '#FF0000','#FF99FF','#0000FF'];

    var FactBar= Morris.Bar ({  
        element: 'factchart',
        data:[<?php echo $factscores_chart_data ?>],
        xkey: 'x',
        ykeys:['y'],
        ymax:1,
        labels:['y'],
        barColors: function (row, series, type) {
        return $arrColors[row.x];
    },
        hideHover:'auto',
        xLabelMargin: 10,
        horizontal:true,        
        stacked: false,
        gridTextColor: '#000',
        gridTextSize: 15,
        resize:true
    });

    

    var BiasBar= Morris.Bar ({        
        element: 'biaschart',
        data:[<?php echo $biasscores_chart_data ?>],
        xkey: 'x',
        ykeys:['y'],
        ymax:1,
        labels:['y'],
        barColors:  function (row, series, type) {
        return $arrColors[row.x];
    },//["#B21516", "#999999", "#1f7a1f", "#000080", "#008080", "#800080", "#000800"],
        hideHover:'auto',
        xLabelMargin: 10,
        horizontal:true,        
        stacked: false,
        gridTextColor: '#000',
        gridTextSize: 15,
        resize:true
    });

var Bias3ScaleBar= Morris.Bar ({        
        element: 'bias3scalechart',
        data:[<?php echo $bias3scalescores_chart_data ?>],
        xkey: 'x',
        ykeys:['y'],
        ymax:1,
        labels:['y'],
        barColors:  function (row, series, type) {
        return $arrColors[row.x+7];
    },//["#B21516", "#999999", "#1f7a1f", "#000080", "#008080", "#800080", "#000800"],
        hideHover:'auto',
        xLabelMargin: 10,
        horizontal:true,        
        stacked: false,
        gridTextColor: '#000',
        gridTextSize: 15,
        resize:true
    });


    FactBar.redraw();
    BiasBar.redraw();
    Bias3ScaleBar.redraw();

$('a[data-toggle="tab"]').on('shown.bs.tab', function(e) {
  var target = $(e.target).attr("href") // activated tab

  switch (target) {
    case "#menu4":
      homeBar.redraw();
      $(window).trigger('resize');
      break;

  }
});
</script>
