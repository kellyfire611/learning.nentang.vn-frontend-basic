function KiemTraDuLieu()
{
    // Tạo biến chứa thông tin lỗi
    var thongTinLoi = '';

    // Lấy thông tin của form nhập liệu
    var hoTen = document.getElementById('txtHoVaTen').value;
    var email = document.getElementById('txtEmail').value;
    var selectDanhMuc = document.getElementById('slDanhMuc').value;

    // Kiểm tra bắt buộc nhập liệu
    if (hoTen == '')
    {
        thongTinLoi += 'Vui lòng nhập Họ tên\n';
    }

    if (email == '') {
        thongTinLoi += 'Vui lòng nhập Email\n';
    }

    if (selectDanhMuc == '') {
        thongTinLoi += 'Vui lòng chọn Danh mục\n';
    }

    // Kiểm tra email Nhập vào có hợp lệ hay không
    var bieuthuc = /^([a-zA-Z0-9\-])+\@(([a-zA-Z0-9])+\.([a-zA-Z]){2,4})+$/;
    if (!bieuthuc.test(email)) {
        thongTinLoi += "Email không hợp lệ!\n";
    }

    // Nếu thông tin lỗi không rỗng : có nghĩa là có chứa thông tin lỗi, hiển thị thông báo cho người dùng
    if(thongTinLoi != '')
    {
        alert(thongTinLoi);
        return false;
    }

    return true;
}