// Initialize and add the map
function initMap() {
  window.map = new google.maps.Map(document.getElementById('map'), {
    zoom: 3,
    center: {lat: 0, lng: -180},
    mapTypeId: 'terrain'   
  });
  var p =makePath(29.315874, 30.051648,73.827492, 141.068329);
  var bound = new google.maps.LatLngBounds(p[0],p[1]);
  //window.map.fitBounds(bound);
  window.map.setZoom(2);
  window.map.setCenter(p[0]);
  window.geocoder = new google.maps.Geocoder();
  window.sourceMarkers=[];
  window.targetMarkers=[];
  //codeAddress("Egypt");
}



  function codeAddress(address1,title) {
    console.log(address1);
    if(address1 == "Warning: This article doesn't have any countries mentioned."){
      alret(address1);
    }
    else{
    geocoder.geocode( { 'address': address1}, function(results, status) {
      if (status == 'OK') {
        window.lat_1= results[0].geometry.location.lat(); window.lng_1= results[0].geometry.location.lng()
      } else {
        alert('Geocode was not successful for the following reason: ' + status);
      }
    drawPath(window.lat_1,window.lng_1,title);
    });
  }
}

  function makePath(x1,y1){
      var c1 = new google.maps.LatLng(x1,y1);
      return [c1];
  }
  function drawPath(x1,y1,name){
  path=makePath(x1+Math.random(),y1+Math.random());
    window.sourceMarkers.push(new google.maps.Marker({
    position: path[0],
    map: window.map,
    title: name
  }));
  }

  function removeAll(){
    for (var i =0; i<window.sourceMarkers.length;i++){
      m=window.sourceMarkers[i];
      m.setMap(null);
  }
} 