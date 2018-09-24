<?php



  function runMyFunction() {
    echo 'I just ran a php function';
    CallClaimRank($content);
  }


function CallClaimRank($content) {
    $curl = curl_init();
    curl_setopt_array($curl, array(
      CURLOPT_URL => "http://claimrank.qcri.org/showResults",
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_ENCODING => "",
      CURLOPT_MAXREDIRS => 10,
      CURLOPT_TIMEOUT => 30,
      CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
      CURLOPT_CUSTOMREQUEST => "POST",
      CURLOPT_POSTFIELDS => "transcript=".$content."&sources=general&showResults=Evaluate",
      CURLOPT_HTTPHEADER => array(
        "Cache-Control: no-cache",
        "Content-Type: application/x-www-form-urlencoded",
        "Postman-Token: 109ca764-2c54-46c5-b6db-608f33897ca2"
      ),
    ));

    $response = curl_exec($curl);
    $err = curl_error($curl);

    curl_close($curl);

    if ($err) {
      echo "cURL Error #:" . $err;
    } else {
      echo $response;
    }
  }

  if (isset($_GET['tweetid'])) {
      $tid = $_GET['tweetid'];
      include 'dbconnection.php';

      $sql="SELECT article FROM tweets_eng WHERE tweets_eng.tweet_id=".$tid;

      $result = mysqli_query($conn,$sql);

      if ($result->num_rows > 0) 

      {
        $row = $result->fetch_assoc();
        $content = $row['article'];
        if(strlen($content)>0)
        #$content = "TRUMP%3A%20Thank%20you%2C%20Lester.%20Our%20jobs%20are%20fleeing%20the%20country.%20They're%20going%20to%20Mexico.%20They're%20going%20to%20many%20other%20countries.%20You%20look%20at%20what%20China%20is%20doing%20to%20our%20country%20in%20terms%20of%20making%20our%20product";
         CallClaimRank($content);
        else {
          echo "<br><h3>No content!</h3><br/>";
        }
      } else {
        echo "<br><h3>No content!</h3><br/>";
        #echo "Query: $sql";
      }
    }


  //CallClaimRank();
?>
