var map, issues, newIssue, marker, bctSearch = [];
newIssue = new L.LayerGroup();

L.mapbox.accessToken = 'pk.eyJ1IjoiaXRiYWtlcnlkZXYiLCJhIjoieU1GMkhkdyJ9.UeS6fL1jCIM2LFz6nI-9CA';
map = L.mapbox.map('map', 'examples.map-i86l3621')
.setView([13.783, 100.495], 10);
map.addControl(L.mapbox.geocoderControl('mapbox.places', {
    autocomplete: true
}));

L.control.locate().addTo(map);
// Since featureLayer is an asynchronous method, we use the `.on('ready'`
// call to only use its marker data once we know it is actually loaded.
var allline = L.mapbox.featureLayer('itbakerydev.j20f7al9').on('ready', function(e) {

    // The clusterGroup gets each marker in the group added to it
    // once loaded, and then is added to the map
    var clusterGroup = new L.MarkerClusterGroup();
    e.target.eachLayer(function(layer) {
        clusterGroup.addLayer(layer);
    });
    map.addLayer(clusterGroup);
});

var layers = {
    Streets: L.mapbox.tileLayer('examples.map-i87786ca'),
    Outdoors: L.mapbox.tileLayer('examples.ik7djhcc'),
    Satellite: L.mapbox.tileLayer('examples.map-igb471ik')
};

var all = L.mapbox.featureLayer('itbakerydev.j20f7al9')
var pink = L.mapbox.featureLayer('itbakerydev.ij92cj0p')
var chalearm = L.mapbox.featureLayer('itbakerydev.i8ib0jmi')
var orange = L.mapbox.featureLayer('itbakerydev.j455eid3')
var green = L.mapbox.featureLayer('itbakerydev.j38mpdg2')
var yellow = L.mapbox.featureLayer('itbakerydev.ie62580n')
var purple = L.mapbox.featureLayer('itbakerydev.ic27e4i9')
var blue = L.mapbox.featureLayer('itbakerydev.ic00jmg3')

var overlayMaps = { 
    "All Line": all,
    "pink-สีชมพู": pink,
    "chalearm": chalearm,
    "orange": orange,
    "green": green,
    "yellow": yellow,
    "purple": purple,
    "blue": blue,
};

layers.Streets.addTo(map);
L.control.layers(layers,overlayMaps).addTo(map);

var placesCluster = L.markerClusterGroup();
//ajax get geojson
$.getJSON("/map/place", function(data) {
    geojsonLayer = L.geoJson(data,{
        onEachFeature: function(feature, layer){
            layer.setIcon(L.mapbox.marker.icon({'marker-symbol': feature.properties.marker, 'marker-color': '59245f'}));
            layer.bindPopup("<header>" + feature.properties.title + "</header>"+
                    feature.properties.popupContent
                    );
            layer.on('mouseover', function (e) {
                this.openPopup();
            });
//            layer.on('mouseout', function (e) {
//                this.closePopup();
//            });
        }
    });   
    //1 add to map
    //geojsonLayer.addTo(map);
    //2 add to cluster
    placesCluster.addLayer(geojsonLayer);
});
//test
//map.addLayer(placesCluster);


var featureLayer;
featureLayer = placesCluster;
$("#report").click(function(e){
    e.preventDefault();
    if (map.hasLayer(featureLayer)){
        map.removeLayer(featureLayer);
        $(this).toggleClass('"btn btn-danger btn-xs" "btn btn-primary btn-xs"');
    }else{
        //featureLayer = L.mapbox.featureLayer().loadURL('/map/place');
        //map.addLayer(featureLayer);

        map.addLayer(featureLayer);
        $(this).toggleClass('"btn btn-danger btn-xs" "btn btn-primary btn-xs"');
    }
    return false;
});

var marker = L.marker(map.getCenter(), {
    icon: L.mapbox.marker.icon({
        'marker-color': 'ff8888'
    }),
    draggable: true
});
marker.addTo(map);

// every time the marker is dragged, update the coordinates container
marker.on('dragend', ondragend);

// Set the initial marker coordinate on load.

function ondragend() {
    var m = marker.getLatLng();
    coordinates.innerHTML = 'Latitude: ' + m.lat + '<br />Longitude: ' + m.lng;
    $("#latlng").val(m.lat+','+m.lng);
}

$("#issue").click(addissue);

/* dow */
/* Update the lat/long values of the form after a marker dragend event; reopen the popup window */
function markerDrag(e) {
}


/* cancel issue registration */
function cancelRegistration() {
    newIssue.clearLayers();
    $('#map').css('cursor', '');
    map.removeEventListener('click', onMapClick);
    $("#loading").hide();
}

/* inserts trouble issue into sqlite database after Submit is clicked */

  $("#loading").hide();

function insertIssue() {
  $("#loading").show();
  var title = $("#title").val();
  var description = $("#description").val();
  var lat = $("#lat").val();
  var lng = $("#lng").val();
  var csrf = $("input[name='csrfmiddlewaretoken']").val();
  var user = $("input[name='user']").val();
  var reporttype = $("#reporttype").val();
  
  if (title.length == 0) {
    alert("Title is required!");
    return false;
  }
  if (description.length == 0) {
    alert("Description is required!");
    return false;
  }
  var dataString = {
      title: title,
      description: description,
      lat: lat,
      lng: lng,
      csrfmiddlewaretoken: csrf,    
      user: user,
      reporttype: reporttype,
  }; 
  $.ajax({
    type: "POST",
    url: "/save_issue/",
    data: dataString,
    success: function(data) {
      console.log(data);
      cancelRegistration();
      issues.clearLayers();
      getIssues();
      $("#loading").hide();
    }
  });
  return false;
}



function onMapClick(e) {
    var markerLocation = new L.LatLng(e.latlng.lat, e.latlng.lng);
    marker = new L.Marker(markerLocation, {draggable:true});

    newIssue.clearLayers();
    newIssue.addLayer(marker);
    newIssue.addTo(map);
    var form =  '<form enctype="multipart/form-data" class="form" id="inputform">'+
        '<label>Title:</label><i>&nbsp;&nbsp;report title</i>'+
        '<input type="text" class="form-control" placeholder="Required" id="title" name="title" />'+
        '<label>Description:</label><i>&nbsp;&nbsp;never shared</i>'+
        '<textarea class="form-control" rows="3" id="description" name="description" placeholder="Required"></textarea>'+
        '<select class="form-control" id="reporttype">'+
          '<option value="t">Traffic Jam</option>'+
          '<option value="c">Construction</option>'+
          '<option value="b">Traffic Close</option>'+
          '<option value="v">Vibration</option>'+
          '<option value="w">Water</option>'+
          '<option value="n">Noise</option>'+
          '<option value="d">Dust</option>'+
        '</select>'+
        '<input style="display: none;" type="text" id="lat" name="lat" value="'+e.latlng.lat.toFixed(6)+'" />'+
        '<input style="display: none;" type="text" id="lng" name="lng" value="'+e.latlng.lng.toFixed(6)+'" /><br><br>'+
        '<div class="form-group">'+
        '<button type="button" class="btn btn-default" onclick="cancelRegistration()">Cancel</button>&nbsp;&nbsp;'+
        '<button type="button" class="btn btn-primary" onclick="insertIssue()">Submit</button>'+
        '</div>'+
        '</form>';
    marker.bindPopup(form, {minWidth: "250"}).openPopup();
}

function addissue(){
    map.on('click', onMapClick);
    $('#map').css('cursor', 'crosshair');
    return false;
}


