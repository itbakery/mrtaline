$(document).ready(function(){
    $(".button-collapse").sideNav();
    $('a#toggle-search').click(function()
    {
        var search = $('div#search');
        search.is(":visible") ? search.slideUp() : search.slideDown(function()
        {
            search.find('input').focus();
        });
        return false;
    });




    var mapCenter = new google.maps.LatLng(13.736717, 100.523186); //Google map Coordinates
    var map;
    var token;
    var point = $('#slidein-panel  ul');
    var bounds = new google.maps.LatLngBounds();
    var markerCluster = null;
    var jsonObject = null;
    var infowindow = new google.maps.InfoWindow();
    map_initialize(); // initialize google map
    //############### Google Map Initialize ##############
    function map_initialize()
    {
        var markers = [];
        var googleMapOptions = 
        { 
            center: mapCenter, // map center
            zoom: 14, //zoom level, 0 = earth view to higher value
            maxZoom: 18,
            minZoom: 5,
            zoomControlOptions: {
                style: google.maps.ZoomControlStyle.SMALL //zoom control size
            },
            scaleControl: true, // enable scale control
            mapTypeId: google.maps.MapTypeId.ROADMAP // google map type
        };

        map = new google.maps.Map(document.getElementById("map-canvas"), googleMapOptions);			

        // Create the serch box
        var input = /** @type {HTMLInputElement} */(document.getElementById('pac-input'));
        map.controls[google.maps.ControlPosition.TOP_LEFT].push(input);
        
        var searchBox = new google.maps.places.SearchBox(/** @type {HTMLInputElement} */(input));
         
        // Listen for the event search 
        //
        google.maps.event.addListener(searchBox, 'places_changed', function() {

            var places = searchBox.getPlaces();

            if (places.length == 0) {
                return;
            }
            for (var i = 0, marker; marker = markers[i]; i++) {
                marker.setMap(null);
            }

            // For each place, get the icon, place name, and location.
            markers = [];
            var bounds = new google.maps.LatLngBounds();
            for (var i = 0, place; place = places[i]; i++) {
                var image = {
                    url: place.icon,
                    size: new google.maps.Size(71, 71),
                    origin: new google.maps.Point(0, 0),
                    anchor: new google.maps.Point(17, 34),
                    scaledSize: new google.maps.Size(25, 25)
                };

                // Create a marker for each place.
                var marker = new google.maps.Marker({
                    map: map,
                    icon: image,
                    title: place.name,
                    position: place.geometry.location
                });

                markers.push(marker);

                bounds.extend(place.geometry.location);
            }

            map.fitBounds(bounds);
        });

        // Load geodata from django pass url to hiddle input
        //map.data.loadGeoJson('https://storage.googleapis.com/maps-devrel/google.json');

        var layers = [];
        //layers[0] = map.data.loadGeoJson('/media/geojson/features-allline.json');
        var url0  = "https://a.tiles.mapbox.com/v4/itbakerydev.j20f7al9/features.json?access_token=pk.eyJ1IjoiaXRiYWtlcnlkZXYiLCJhIjoieU1GMkhkdyJ9.UeS6fL1jCIM2LFz6nI-9CA";
        layers[0] = map.data.loadGeoJson(url0);


        var placeurl = $("#place").val();
        // map.data.loadGeoJson(placeurl)  take url
       // map.data.loadGeoJson(placeurl);
        $.getJSON(placeurl, function(data) {
            //console.log(data);
            console.log(data);
            jsonObject = data;
            for (var i = 0, feature; feature = jsonObject.features[i]; i++) {
                if (feature.geometry) {
                    var marker = new google.maps.Marker({
                        fid: i,
                        position: new google.maps.LatLng(
                                feature.geometry.coordinates[1], 
                                feature.geometry.coordinates[0]
                                )
                    });
                    bounds.extend(marker.position);
                    markers.push(marker);
                    //console.log(markers);
                    google.maps.event.addListener(marker, 'click', function(e) {
                        var feature = jsonObject.features[this.fid];
                        //var infoHtml = "no: " + feature.properties.model
                        var infoHtml = "<div style='width:150px; text-align: center;'>" + 
                            feature.properties.popupContent + 
                            "</div>"
                            infowindow.setContent(infoHtml);
                        infowindow.open(map, this);
                    });
                }

            }
            console.log(markers);
            markerCluster = new MarkerClusterer(map, markers);
            map.fitBounds(bounds);
        });


        // global infowindow
        var infowindow = new google.maps.InfoWindow();

        // When the user clicks, open an infowindow
        map.data.addListener('click', function(event) {
            var myHTML = event.feature.getProperty("popupContent");
            infowindow.setContent("<div style='width:150px; text-align: center;'>"+myHTML+"</div>");
            infowindow.setPosition(event.feature.getGeometry().get());
            infowindow.setOptions({pixelOffset: new google.maps.Size(0,-30)});
            infowindow.open(map);
        });

        //Right Click to Drop a New Marker
        google.maps.event.addListener(map, 'click', function(event) {
            //Edit form to be displayed with new marker
            var EditForm = $(".save-form").clone().show()[0]; 
            //Drop a new Marker with our Edit Form
            create_marker(map,event.latLng, 'New Report', EditForm.outerHTML, true, true, true, "/static/icons/pin_green.png");
        });

    }

});
