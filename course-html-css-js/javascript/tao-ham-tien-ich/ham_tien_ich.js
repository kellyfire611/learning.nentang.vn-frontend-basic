// Hàm tính Trung bình cộng
function tinh_trung_binh_cong(a, b, c) {
    var tong = (a + b + c);
    var ketqua = tong / 3;
    return ketqua;
}

// Hàm tính Bình Phương của 1 số
function tinh_binh_phuong(number) {
    var result = number * number;
    return result;
}

// Hàm tính Lập Phương của 1 số
function tinh_lap_phuong(number) {
    var result = number * number * number;
    return result;
}
  
// Hàm hiển thị câu chào mừng
function hien_thi_cau_chao_mung(hoten) {
    document.write('Xin chào mừng <span style="color: red;font-weight: bold;">'+ hoten +'</span> đã ghé thăm trang web của chúng tôi!<br />');
}

