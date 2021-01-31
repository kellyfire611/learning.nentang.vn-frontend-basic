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
  var url = "./data/danh_sach_va_vo.xlsx";
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
    dataVaVo = XLSX.utils.sheet_to_json(worksheet, {
      raw: true
    });
    // console.log(dataVaVo);
    dataVaVo_MienBac = dataVaVo.filter(function (item) {
      return item.mien === 'mien_bac';
    });
    dataVaVo_MienTrung = dataVaVo.filter(function (item) {
      return item.mien === 'mien_trung';
    });
    dataVaVo_MienNam = dataVaVo.filter(function (item) {
      return item.mien === 'mien_nam';
    });

    // Generate menu
    generateMenu_MienBac();
    generateMenu_MienTrung();
    generateMenu_MienNam();

    // Binding event
    $('#main-menu').on('click', '#mnuMienBac .mnuItemTinhThanh', function () {
      loadContent(this);
    });
    $('#main-menu').on('click', '#mnuMienTrung .mnuItemTinhThanh', function () {
      loadContent(this);
    });
    $('#main-menu').on('click', '#mnuMienNam .mnuItemTinhThanh', function () {
      loadContent(this);
    });
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

function generateMenu_MienTrung() {
  if (!dataVaVo_MienTrung)
    return;

  let uniqueTinhThanhArray = _.mapPick(dataVaVo_MienTrung, ['tinh_thanh']);
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
      <li><a href="#" data-id="mien_trung" data-tinh_thanh="${item.tinh_thanh}" class="mnuItemTinhThanh">${item.tinh_thanh}</a></li>
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

  $('#mnuMienTrung').html(htmlStr);
}

function generateMenu_MienNam() {
  if (!dataVaVo_MienNam)
    return;

  let uniqueTinhThanhArray = _.mapPick(dataVaVo_MienNam, ['tinh_thanh']);
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
      <li><a href="#" data-id="mien_nam" data-tinh_thanh="${item.tinh_thanh}" class="mnuItemTinhThanh">${item.tinh_thanh}</a></li>
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

  $('#mnuMienNam').html(htmlStr);
}

// Content
function loadContent(ele) {
  let mnuId = $(ele).data('id');
  let mnuTinhThanh = $(ele).data('tinh_thanh');
  generateButtons(mnuId, mnuTinhThanh);
}

function generateButtons(mnuId, tinh_thanh) {
  if (!dataVaVo)
    return;

  let filteredArray;
  if(mnuId == 'mien_bac') {
    filteredArray = dataVaVo_MienBac;
  } else if(mnuId == 'mien_trung') {
    filteredArray = dataVaVo_MienTrung;
  } else if(mnuId == 'mien_nam') {
    filteredArray = dataVaVo_MienNam;
  }

  filteredArray = filteredArray.filter(function (item) {
    return item.mien === mnuId
      && item.tinh_thanh == tinh_thanh;
  });
  if (!filteredArray || filteredArray.length <= 0) {
    return;
  }

  let htmlStr = '<div class="text-center">';
  htmlStr += `<h1 class="text-center cuuho-title">DANH SÁCH CÁC ĐƠN VỊ VÁ VỎ</h1><span class="cuuho-title-tinhthanh">${tinh_thanh}</span>`;

  filteredArray.forEach(function (item) {
    let sdt = '0' + item.vavo_sdt;
    let htmlButton = `
      <a href="tel:${sdt}" class="btn btn-primary btn-cuuho-sdt m-3 w-75">
        ${item.vavo_ten}<br />${sdt}
      </a><br />
    `;

    htmlStr += htmlButton;
  });
  htmlStr += '</div>';

  $('#main-content').html(htmlStr);
}

// jQuery code
$(function () {
  // Prevent closing from click inside dropdown
  $(document).on('click', '#main-menu .dropdown-menu', function (e) {
  });

  // Read data Excel
  parseExcel('danh_sach_va_vo.xlsx');
})
