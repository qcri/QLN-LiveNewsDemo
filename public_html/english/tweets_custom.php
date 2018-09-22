<style>

.profile_img {

    width:35px;

    height:35px;

    display:inline-block;

}

.username {

    font-size: 18px;

    font-weight:bold;

    color:gray;

    font-family: "Times New Roman", Times, serif;

    display: inline-block;

}

.tweet {

    font-size: 23px;

    font-family: "Times New Roman", Times, serif;   

    display: inline-block;

}

.ranktable { 
    border-spacing: 10px;
    border-collapse: separate;
}

.tooltip {
    position: relative;
    display: inline-block;
    border-bottom: 1px dotted black;
}

.tooltip .tooltiptext {
    visibility: hidden;
    width: 120px;
    background-color: black;
    color: #fff;
    text-align: center;
    border-radius: 6px;
    padding: 5px 0;

    /* Position the tooltip */
    position: absolute;
    z-index: 1;
}

.tooltip:hover .tooltiptext {
    visibility: visible;
}

.tweet_time {

    font-size: 18px;

    color:gray;

    font-family: "Times New Roman", Times, serif;           

    display:inline-block;

}

.div_tweet {
	border: 3px #eee solid;
	display: flex;
	min-height: 100px;	
	overflow: auto;
	border-radius: 10px;
}

.tweet_pic {

    margin: 10px 10px;

    width:250px;

    height:150px;

    top:0%;

    float:right;

    display: inline-block;

    vertical-align:top;

}

.div_text {
	flex: 0 0 65%;
	width: 60vw;
}

.div_tweet_pic {
	flex:1;
	width: 30vw;

}

</style>

<!-- TWITTER USER PROFILE INFORMATION WILL BE HERE -->

<?php
//include 'callAPI.php';
function time_elapsed_string($datetime,$present, $full = false) 

{

   $now = new DateTime($present);

   $ago = new DateTime($datetime);

   $diff = $now->diff($ago);



   $diff->w = floor($diff->d / 7);

   $diff->d -= $diff->w * 7;



   $string = array(

       'y' => 'year',

       'm' => 'month',

       'w' => 'week',

       'd' => 'day',

       'h' => 'hour',

       'i' => 'minute',

       's' => 'second',

   );

   foreach ($string as $k => &$v) {

       if ($diff->$k) {

           $v = $diff->$k . ' ' . $v . ($diff->$k > 1 ? 's' : '');

       } else {

           unset($string[$k]);

       }

   }



   if (!$full) $string = array_slice($string, 0, 1);

   return $string ? implode(', ', $string) . ' ago' : 'just now';

}

?>



   

<?php

    include 'dbconnection.php';

    $sql="SELECT * FROM tweets_eng, eng_source_name WHERE eng_source_name.source_user_name = tweets_eng.screen_name ORDER BY tweets_eng.date DESC LIMIT 50";

    $result = mysqli_query($conn,$sql);

    if ($result->num_rows > 0) 

    {

        while($row = $result->fetch_assoc()) 

        {

            $tweetid = $row['tweet_id'];
            $json = $row['tweet'];
            $json_title = $row['title'];
            $json_image = $row['image'];
            $pscore = $row['propaganda_score']; 

            // decode json format tweets

            $tweet=json_decode($json, TRUE);

            

                

            $now = gmdate('D M d H:i:s +0000 Y');

            //echo $now;

                    

            // get tweet text

            $tweet_text=$tweet['text'];                 

            

            $org_tweet_text = $tweet_text;

            // make links clickable

            $tweet_text=preg_replace('@(https?://([-\w\.]+)+(/([\w/_\.]*(\?\S+)?(#\S+)?)?)?)@', '<a href="$1" target="_blank">... &nbsp;</a>', $tweet_text);

            

            if (array_key_exists('urls', $tweet['entities']))

            {

                if(array_key_exists(0, $tweet['entities']['urls']))

                {

                    $tweet_url = $tweet['entities']['urls'][0]['expanded_url'];

                }

            }

            else

            {

                $tweet_url = NULL;

            }

            

            

            //$tweet_text=preg_replace('@(https?://([-\w\.]+)+(/([\w/_\.]*(\?\S+)?(#\S+)?)?)?)@', ' ', $tweet_text );

                                                    

            // filter out the retweets                      

            if(preg_match('/^RT/', $tweet_text) == 0)

            {           

                echo "<div class=\"div_tweet\">";

                echo "<div class='div_text'>";

                

                

                // show name and screen name

                echo "<img class=\"profile_img\" src='{$tweet['user']['profile_image_url_https']}' class='img-thumbnail' />";

                echo "<html>&ensp;</html>";

                echo "<p class=\"username\">{$tweet['user']['name']}</p> ";

                //echo "<span class='color-gray'>@{$screen_name}</span>";

                                    

                                

                // output

                if($json_title != NULL)

                {

                    echo "<h4 class='margin-top-4px'>";

                    echo "<p class=\"tweet\">$json_title &nbsp;</p>";

                    echo "<a href='{$tweet_url}'>...</a> ";

                    echo "</h4>";

                }

                else

                {

                    echo "<h4 class='margin-top-4px'>";

                    echo "<p class=\"tweet\">From tweet: $tweet_text</p>";

                    echo "</h4>";

                }

                

                // get tweet time

                $tweet_time = $tweet['created_at'];

                //echo $tweet_time;

                //echo nl2br("\n ");

                            

                $t_time= time_elapsed_string($tweet_time,$now);

                echo "<p class='tweet_time'>$t_time &nbsp; ($tweet_time)</p>";

                echo "<table class='ranktable'><tr><td><span id='$tweetid' name='$tweetid'  title=\"Propaganda Score\">PScore:$pscore<script>drawChart($pscore,'$tweetid');</script></span></td><td><a href='#'  title=\"QCRI Claim Rank\" onClick='MyWindow=window.open(\"callAPI.php\",\"MyWindow\",width=300,height=300); return false;'><img src='iconClaim.png' alt='ClaimRank' width='68px'></a></td></tr></table>";

                echo "</div>"; //ended div_text

                echo "<div class='div_tweet_pic'>";

                //picture from tweet url

                

                    if($json_image != NULL)

                    {

                        echo "<img class='tweet_pic' src='{$json_image}' class='img-thumbnail'/>";

                    } 

                    else if(array_key_exists('media', $tweet['entities']))

                    {

                        // get tweet picture

                        //if(array_key_exists('media_url', $tweet['entities']['media']))

                        //{

                            $tweet_pic= $tweet['entities']['media'][0]["media_url"];

                            echo "<img class='tweet_pic' src='{$tweet_pic}' class='img-thumbnail'/>";

                        //}

                    }

                    echo "</div>"; //ended div_tweet_pic





                echo "</div>";

            }   

            

            

    ?>

    <script>
// When the user clicks on div, open the popup
function myFunction() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
}
</script>

    <?php

    

            //echo strlen($row['tweet']).'<br>';

            //echo $row['tweet'].'<br>';

            echo '<br>';

        }

    }

?>
