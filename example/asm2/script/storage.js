"use strict";

// Lấy danh sách thú cưng đã có trong localStorage

/**
 * Hàm thực hiện việc Lưu trữ vào LocalStorage
 * @param {*} key Từ khóa
 * @param {*} value Giá trị
 */
function saveToStorage(key, value) {
  var data = value;

  // Kiểm tra, nếu dữ liệu là kiểu mảng ARRAY
  // -> cần phải convert về kiểu String để lưu trữ được vào LocalStorage
  if(Array.isArray(value)) {

    // Hàm JSON.stringify sẽ chuyển đổi ARRAY thành STRING
    data = JSON.stringify(value);
  }

  // Lưu trữ vào LocalStorage với từ khóa "key"
  window.localStorage.setItem(key, data);
}

/**
 * Hàm lấy giá trị được lưu trữ trong LocalStorage
 * @param {*} key Từ khóa
 */
function getFromStorage(key) {

  // Lấy dữ liệu từ LocalStorage
  return window.localStorage.getItem(key);
}