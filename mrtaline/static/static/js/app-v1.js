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
   
    map_initialize(); // initialize google map
    //############### Google Map Initialize ##############
    function map_initialize()
    {
        
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
        map.data.loadGeoJson('https://storage.googleapis.com/maps-devrel/google.json');
        var placeurl = $("#place").val();
        // map.data.loadGeoJson(placeurl)  take url
        map.data.loadGeoJson(placeurl);
        $.getJSON(placeurl, function(data) {
            console.log(data);
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
        //var mydata;
        //$.ajax({
        //    url: placeurl,
        //    dataType: 'json',
        //    success: function (data) {
        //        mydata = data;
        //        console.log(mydata);
        //    }
        //});

        //Load Markers from the XML File, Check (map_process.php)
        //        $.get("map_process.php", function (data) {
        //            $(data).find("marker").each(function () {
        //                var name 		= $(this).attr('name');
//                var address 	= '<p>'+ $(this).attr('address') +'</p>';
//                var type 		= $(this).attr('type');
//                var point 	= new google.maps.LatLng(parseFloat($(this).attr('lat')),parseFloat($(this).attr('lng')));
//                create_marker(point, name, address, false, false, false, "http://sanwebe.com/assets/google-map-save-markers-db/icons/pin_blue.png");
//            });
//        });	

        //Right Click to Drop a New Marker
        google.maps.event.addListener(map, 'click', function(event) {
            //Edit form to be displayed with new marker
            var EditForm = $(".save-form").clone().show()[0]; 
            //Drop a new Marker with our Edit Form
            create_marker(map,event.latLng, 'New Report', EditForm.outerHTML, true, true, true, "/static/icons/pin_green.png");
        });

    }

});
