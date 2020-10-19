function myMap(lat, lon) {
    var properties = {
        center: new google.maps.LatLng(lat, long),
        zoom: zoom,
    };

    var map = new google.maps.Map(document.getElementById("googleMap"), properties)
}