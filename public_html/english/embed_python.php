<?php $myArray=[];
 function php_func($url){
	$validation = exec("python3 script.py $url");


    /*$validation = explode("+",$validation);
    foreach ($validation as $str) {
        echo "<li>".$str."</li>";
}*/
    //passthru("python script.py");
    echo $validation;

 }
?>
<!DOCTYPE HTML>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="navbar.css">
        <script async defer
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBL1f-4bT07OPdO-ugFjHfLIFeT1BkGIRs&callback=initMap">
</script>
    <meta charset="utf-8">
    <title>Button</title>
    <script src="mapFunctions.js" async defer></script>

    <script> function echoHello(number,title){
        if(number==1){
        	var res = "<?php 
        $url = "https://www.aljazeera.com/news/2018/06/occupy-ice-temporarily-shuts-facilities-cities-180627182119792.html";
    	php_func($url); ?>"
    };
    if(number==2){
                    var res = "<?php 
        $url = "https://www.economist.com/special-report/2018/06/23/how-dubai-became-a-model-for-free-trade-openness-and-ambition?fsrc=scn/tw/te/bl/ed/howdubaibecameamodelforfreetradeopennessandambitiondobuy";
        php_func($url); ?>"
    };
    if(number==3){
                    var res = "<?php 
        $url = "https://timesofindia.indiatimes.com/sports/football/fifa-world-cup/fifa-world-cup-2018-rojos-last-gasp-rescue-act-takes-argentina-to-last-16/articleshow/64757113.cms";
        php_func($url); ?>"
    };
        if(number==4){
                    var res = "<?php 
        $url = "https://edition.cnn.com/2018/06/27/americas/mexico-political-deaths-election-season-trnd/index.html";
        php_func($url); ?>"
    };
            if(number==5){
                    var res = "<?php 
        $url = "https://www.bbc.com/news/world-middle-east-44354409";
        php_func($url); ?>"
    };
    	document.getElementById("here").innerHTML = res;
        displayAll(title);
        }
        function displayAll(title){
            x=document.getElementById("here").innerHTML;
            //codeAddress("Qatar");
            x=x.split(",");
            for(var i=0;i<x.length;i++){
                codeAddress(x[i],title);
            }
            }
	</script>
        <style>
       /* Set the size of the div element that contains the map */
      #map {
        height: 500px;  /* The height is 400 pixels */
        width: 60%;  /* The width is the width of the web page */
        display:inline-block;
        float:right;
       }
   #news{
    width:36%;
    display:inline-block;
   }
   #here{
    display:none;
   }
   .button{
    display:inline-block;
    float:right;
   }

   </style>
</head>
<body>
<nav class="navbar navbar-dark bg-dark justify-content-between">
         <a style="float:left;left:0px;margin-right:auto;" class="heading navbar-brand" href='index.php'>Live News</a>
</nav>
    <div id="map" ></div>
	<br/>
	<p id="here"></p>
    <script src="mapFunctions.js">initMap()</script>
    
<div id="news">
<input type="button" value="Remove All" class= "button" onclick="removeAll()">
<div>
<h2>Occupy ICE temporarily shuts down facilities in several US cities
</h2>
<h3>aljazeera</h3>
<a target= "_blank" href="https://www.aljazeera.com/news/2018/06/occupy-ice-temporarily-shuts-facilities-cities-180627182119792.html" id="link-1">more..</a>
<input type="button" value="display" class= "button" onclick="echoHello(1,'Occupy ICE temporarily shuts down facilities in several US cities')">


</div>
<div>
<h2>How Dubai became a model for free trade, openness and ambition</h2>
<h3>economist</h3>
<a target= "_blank" href="https://www.economist.com/special-report/2018/06/23/how-dubai-became-a-model-for-free-trade-openness-and-ambition?fsrc=scn/tw/te/bl/ed/howdubaibecameamodelforfreetradeopennessandambitiondobuy">more..</a>
<input type="button" value="display" class= "button" onclick="echoHello(2,'How Dubai became a model for free trade, openness and ambition')">
</div>
<div>
<h2>FIFA World Cup 2018: Rojo's last-gasp rescue act takes Argentina to last-16</h2>
<h3>timesofindia</h3>
<a target= "_blank" href="https://timesofindia.indiatimes.com/sports/football/fifa-world-cup/fifa-world-cup-2018-rojos-last-gasp-rescue-act-takes-argentina-to-last-16/articleshow/64757113.cms">more..</a>
<input type="button" value="display" class= "button" onclick="echoHello(3,'FIFA World Cup 2018: Rojo\'s last-gasp rescue act takes Argentina to last-16')">
</div>
<div>
<h2>Mexico goes to the polls this weekend. 132 candidates have been killed since campaigning began, per one count
</h2>
<h3>cnn</h3>
<a target= "_blank" href="https://edition.cnn.com/2018/06/27/americas/mexico-political-deaths-election-season-trnd/index.html">more..</a>
<input type="button" value="display" class= "button" onclick="echoHello(4,'Mexico goes to the polls this weekend. 132 candidates have been killed since campaigning began, per one count')">
</div>
<div>
<h2>Qatar cash and cows help buck Gulf boycott</h2>
<h3>bbc</h3>
<a target= "_blank" href="https://www.bbc.com/news/world-middle-east-44354409">more..</a>
<input type="button" value="display" class= "button" onclick="echoHello(5,'Qatar cash and cows help buck Gulf boycott')">
</div>
</div>
</body>
</html>


