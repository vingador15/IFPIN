    function onEachFeature(feature, layer){
      var popupContent = feature.properties.popup_content;
      layer.bindPopup(popupContent);
    }

    const mbAttr = 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>';
    const mbUrl = 'https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw';
  
    const streets = L.tileLayer(mbUrl, {id: 'mapbox/streets-v11', tileSize: 512, zoomOffset: -1, attribution: mbAttr});

    const osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    });

    const googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
      maxZoom: 20,
      subdomains:['mt0', 'mt1', 'mt2', 'mt3']
    })

    const googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}')


    var pontos = L.geoJson([], {
      style: {
        fillColor: '#6e00d4',
        weight: 2,
        opacity: 1,
        color:'#6e00d4',
        fillOpacity:1
      },
      pointToLayer: function(feature, latlng){
        return new L.CircleMarker(latlng,{radius: 4});
      },
      onEachFeature: onEachFeature,
    });

    var pontos_url = $("#mapageojson").val();

    $.getJSON(pontos_url, function(data){
      pontos.addData(data);
    })

    const map = L.map('map', {
      center: [-22.5206, -43.9906],
      zoom: 17,
      layers: [streets, pontos],
    });


    var watchID = navigator.geolocation.watchPosition(function(pos){
      L.marker([pos.coords.latitude, pos.coords.longitude]).addTo(map).bindPopup("Você está aqui!");
    }, function(error){
      console.log(error);
    }, {
      enableHighAccuracy: true,
      timeout: 30000
    });

   
    const baseLayers = {
      'OpenStreetMap': osm,
      'Streets': streets,
      'Locais': pontos,
    };

    const overlays = {
      
    };

    const layerControl = L.control.layers(baseLayers, overlays).addTo(map);

    const satellite = L.tileLayer(mbUrl, {id: 'mapbox/satellite-v9', tileSize: 512, zoomOffset: -1, attribution: mbAttr});
    layerControl.addBaseLayer(satellite, 'Satellite');