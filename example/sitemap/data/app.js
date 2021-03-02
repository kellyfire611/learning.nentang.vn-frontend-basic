var GOOGLE_MAP_API_KEY = 'AIzaSyDXhL7KLg0QZMsbvNy1R2BXnFzGl1ETFUY';
var dataVaVo;
var dataVaVo_MienBac;
var dataVaVo_MienTrung;
var dataVaVo_MienNam;

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

    // Generate marker
  }
  oReq.send();
};

function generateMenu_MienBac() {
  if (!dataVaVo_MienBac)
    return;

  let uniqueTinhThanhArray = _.mapPick(dataVaVo_MienBac, ['tinh_thanh']);
  uniqueTinhThanhArray = _.uniqBy(uniqueTinhThanhArray, 'tinh_thanh');

  let totalItem = uniqueTinhThanhArray.length;
  let itemPerGroup = 6;
  let start = 0;
  let index = 0;
  let htmlStr = '<div class="row row-cols-1">';
  htmlStr += '<div class="col">';
  uniqueTinhThanhArray.forEach(function (item) {
    let htmlMenu = '';
    if ((index == 0) || (index % itemPerGroup == 0)) {
      // htmlMenu += '<div class="col">';
    }
    htmlMenu += '<ul>';
    htmlMenu += `
      <li><a href="#" data-id="mien_bac" data-tinh_thanh="${item.tinh_thanh}" class="mnuItemTinhThanh">${item.tinh_thanh}</a></li>
    `;
    htmlMenu += '</ul>';

    if ((index % itemPerGroup) == (itemPerGroup - 1) || ((index + 1) == totalItem)
    ) {
      // htmlMenu += '</div>';
    }

    htmlStr += htmlMenu;
    index++;
  });
  htmlStr += '</div>';
  htmlStr += '</div>';

  $('#mnuMienBac').html(htmlStr);
}

// jQuery code
$(function () {
  // Read data Excel
  parseExcel('danh_sach_garage.xlsx');
})
