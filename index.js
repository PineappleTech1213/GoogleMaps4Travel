// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map;
let current_pos;
let search_pos;
let autocomplete;
function initMap() {
  writeIntro();
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 41.85,lng: -87.65 },
    zoom: 10,
    }); 
  const locationButton = document.getElementById("button");
  locationButton.textContent = "Get Your Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          current_pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };
          map.setCenter(current_pos);
          //add a marker to the current location
          addMarker(current_pos,map);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
  completeSearch();
  new GetDirection(map);
}


function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
  
}

function writeIntro() {
    const content = "Hello, welcome to my Google Maps API project! Try clicking the button to see your current location."
    document.getElementById("intro").innerHTML = content;
}

function addMarker(coords,map){
    var marker = new google.maps.Marker({position:coords, map: map,icon:"http://maps.google.com/mapfiles/kml/paddle/orange-stars.png"});
    var inforWindow = new google.maps.InfoWindow({content:"<h1>Current Location</h1>"});
    //set zooming to 15
    map.setZoom(15);
    marker.addEventListener("click", () => {
      inforWindow.open(map, marker);
    });
}

window.initMap = initMap;

function completeSearch(){
  //make the input box autocomplete
  const options = {
    fields: ["place_id", "geometry", "name", "formatted_address"],
    strictBounds: false,
 }
  autocomplete = new google.maps.places.Autocomplete(document.getElementById("autocomplete"),options);
  autocomplete.bindTo("bounds", map);
  
  const auto_marker = new google.maps.Marker({
    map,
    anchorPoint: new google.maps.Point(0, -29),});
  autocomplete.addListener("place_changed", () => {
    auto_marker.setVisible(false);
    const place = autocomplete.getPlace();
    search_pos = place.geometry.location;
    console.log(search_pos);
    if (!place.geometry || !place.geometry.location) {
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);
    }

    auto_marker.setPosition(place.geometry.location);
    auto_marker.setVisible(true);
    //create a new infoWindow
    const info = new google.maps.InfoWindow();
    const InfoContent = document.getElementById('infoWindow');
    InfoContent.children['place-name'].textContent = place.name;
    InfoContent.children['place-address'].textContent = place.formatted_address;
    info.setContent(InfoContent);
    info.open(map, auto_marker);
    
  });  
}
class GetDirection {
  map;
  originId;
  destinationId;
  travelMode;
  directionService;
  directionRenderer;
  constructor(map){
    this.map = map;
    this.originId = "";
    this.destinationId = "";
    this.tranvelMode = google.maps.TravelMode.DRIVING;
    this.directionService = new google.maps.DirectionsService();
    this.directionRenderer = new google.maps.DirectionsRenderer();
    this.directionRenderer.setMap(map);

    const originId = document.getElementById("start");
    const destinationId = document.getElementById("end");
    const originAutoComplete = new google.maps.places.Autocomplete(originId,
      {fields:['place_id']});
    const destinationAutoComplete = new google.maps.places.Autocomplete(destinationId,
      {fields:['place_id']});
    this.setupPlaceChangedListener(originAutoComplete, "ORIG");
    this.setupPlaceChangedListener(destinationAutoComplete, "DEST");
    }

    setupPlaceChangedListener(autocomplete, mode){
      autocomplete.bindTo("bounds",this.map);
      autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        if (!place.place_id) {
          window.alert("Please select an option from the dropdown list.");
          return;
        }
        if (mode === "ORIG") {
          this.originId = place.place_id;
        } else {
          this.destinationId = place.place_id;
        }
        this.route();
      });
    }

    route(){
      if (!this.originId || !this.destinationId) {
        return;
      }
      const me = this;
      this.directionService.route(
        {origin: {placeId: this.originId},
      destination: {placeID:this.destinationId},
    travelMode: this.tranvelMode},
        (res, status) => {
          if (status ==="OK") {
            me.directionRenderer.setDirections(res);
          } else {
            console.log("Directions request failed due to " + status);
          }
        }
      )
    }

}
function getDirectionAfterSearch(map,search_pos){

}
