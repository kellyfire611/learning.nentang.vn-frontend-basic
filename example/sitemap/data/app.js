var GOOGLE_MAP_API_KEY = 'AIzaSyDXhL7KLg0QZMsbvNy1R2BXnFzGl1ETFUY';
let dataGarage;

// extend lodash
_.mixin({
  mapPick: function (objs, keys) {
    return _.map(objs, function (obj) {
      return _.pick(obj, keys)
    })
  }

});

var parseExcel = function (file) {
  /* set up XMLHttpRequest */
  var url = "./data/danh_sach_garage.xlsx";
  var oReq = new XMLHttpRequest();
  oReq.open("GET", url, true);
  oReq.responseType = "arraybuffer";

  oReq.onload = function (e) {
    var arraybuffer = oReq.response;

    /* convert data to binary string */
    var data = new Uint8Array(arraybuffer);
    var arr = new Array();
    for (var i = 0; i != data.length; ++i) arr[i] = String.fromCharCode(data[i]);
    var bstr = arr.join("");

    /* Call XLSX */
    var workbook = XLSX.read(bstr, {
      type: "binary"
    });

    /* DO SOMETHING WITH workbook HERE */
    var first_sheet_name = workbook.SheetNames[0];
    /* Get worksheet */
    var worksheet = workbook.Sheets[first_sheet_name];
    data = XLSX.utils.sheet_to_json(worksheet, {
      raw: true
    });

    // Init map and Generate marker
    dataGarage = data;
    initMap();
  }
  oReq.send();
};

function generateMarker(map) {
  if (!dataGarage)
    return;

  dataGarage.forEach(function (item) {
    const contentString =
      '<div id="content">' +
      '<div id="siteNotice">' +
      "</div>" +
      '<h1 id="firstHeading" class="firstHeading">'+ item.garage_ten +'</h1>' +
      '<div id="bodyContent">' +
      "<p>" +
      item.tinh_thanh
      "</p>" +
      "</div>" +
      "</div>";
    const infowindow = new google.maps.InfoWindow({
      content: contentString,
    });
    const marker = new google.maps.Marker({
      position: {lat: item.latitude, lng: item.longitude },
      map,
      title: item.garage_ten,
    });
    marker.addListener("click", () => {
      infowindow.open(map, marker);
    });
  });
}

// This example displays a marker at the center of Australia.
// When the user clicks the marker, an info window opens.
function initMap() {
  // Generate marker
  if (!dataGarage)
    return;

  const firstItem = dataGarage[0];
  const uluru = { lat: firstItem.latitude, lng: firstItem.longitude };
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 9,
    center: uluru,
  });
  generateMarker(map);
}

// jQuery code
$(function () {
  // Read data Excel
  parseExcel('danh_sach_garage.xlsx');
})
