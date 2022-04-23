"use strict";

// Chọn element
const btnNav = document.getElementById("sidebar");

// Bổ sung Animation cho Sidebar
btnNav.addEventListener("click", function () {
  let active = document.getElementById("sidebar");
  active.classList.toggle("active");
});

/////////////////////////////////
/////////////////////////////////
const btnSubmit = document.getElementById("submit-btn");

let tableBodyEl = document.getElementById("tbody");

const petArr = [];

// Bắt sự kiện Click vào nút "Submit"
btnSubmit.addEventListener("click", function () {
  // Lấy dữ liệu từ các Input Form
  const inputId = document.getElementById("input-id").value;
  const inputName = document.getElementById("input-name").value;
  const inputAge = parseInt(document.getElementById("input-age").value);
  const inputType = document.getElementById("input-type").value;
  const inputWeight = parseInt(document.getElementById("input-weight").value);
  const inputLength = parseInt(document.getElementById("input-length").value);
  const inputColor = document.getElementById("input-color-1").value;
  const inputBreed = document.getElementById("input-breed").value;
  const inputVaccinated = document.getElementById("input-vaccinated").checked;
  const inputDewormed = document.getElementById("input-dewormed").checked;
  const inputSterilized = document.getElementById("input-sterilized").checked;

  const data = {
    id: inputId,
    name: inputName,
    age: inputAge,
    type: inputType,
    weight: inputWeight,
    length: inputLength,
    color: inputColor,
    breed: inputBreed,
    vaccinated: inputVaccinated,
    dewormed: inputDewormed,
    sterilized: inputSterilized,
    date: new Date(),
  };

  // Validate dữ liệu hợp lệ
  if (data.id === "") {
    alert("Please input for pet id!");
    return false;
  }

  for (let i = 0; i < petArr.length; i++) {
    if (data.id === petArr[i].id) {
      alert("ID must unique!");
      return false;
    }
  }

  if (data.name === "") {
    alert("Please input for pet name!");
    return false;
  }

  if (data.age === "" || isNaN(data.age)) {
    alert("Please input for age!");
    return false;
  } else if (data.age < 1 || data.age > 15) {
    alert("Age must be between 1 and 15!");
    return false;
  }

  if (data.type === "Select Type") {
    alert("Please select type!");
    return false;
  }

  if (data.weight === "" || isNaN(data.weight)) {
    alert("Please input for weight!");
    return false;
  } else if (data.weight < 1 || data.weight > 15) {
    alert("Weight must be between 1 and 15!");
    return false;
  }

  if (data.length === "" || isNaN(data.length)) {
    alert("Please input for length!");
    return false;
  } else if (data.length < 1 || data.length > 100) {
    alert("Length must be between 1 and 100!");
    return false;
  }

  if (data.breed === "Select Breed") {
    alert("Please select Breed");
    return false;
  }

  petArr.push(data);

  renderTableData(petArr);
  resetForm();
});

// Hiển thị danh sách thú cưng
function renderTableData(petArr) {
  tableBodyEl.innerHTML = "";

  let table = ``;
  for (let i = 0; i < petArr.length; i++) {
    table += `<tr>
              <th>${petArr[i].id}</th>
              <td>${petArr[i].name}</td>
              <td>${petArr[i].age}</td>
              <td>${petArr[i].type}</td>
              <td>${petArr[i].weight} kg</td>
              <td>${petArr[i].length} cm</td>
              <td>${petArr[i].breed}</td>
              <td>
                <i class="bi bi-square-fill" style="color: ${
                  petArr[i].color
                }"></i>
              </td>
              <td>
                <i class="bi bi-${
                  petArr[i].vaccinated ? "check" : "x"
                }-circle-fill"></i>
              </td>
              <td><i class="bi bi-${
                petArr[i].dewormed ? "check" : "x"
              }-circle-fill"></i></td>
              <td><i class="bi bi-${
                petArr[i].sterilized ? "check" : "x"
              }-circle-fill"></i></td>
              <td>${petArr[i].date.getDate()}/${
      petArr[i].date.getMonth() + 1
    }/${petArr[i].date.getFullYear()}</td>
              <td>
                <button type="button" class="btn btn-danger" onclick ="deletePet('${
                  petArr[i].id
                }')">Delete</button>
              </td>
            </tr>`;
  }
  tableBodyEl.innerHTML += table;
}

// Xóa các dữ liệu vừa nhập trên Form
function resetForm() {
  document.getElementById("input-form").reset();
}

// Xóa một thú cưng
function deletePet(x) {
  if (confirm("Are you sure?")) {
    for (let i = 0; i < petArr.length; i++) {
      if (petArr[i].id === x) {
        petArr.splice(i, 1);
        renderTableData(petArr);
      }
    }
  }
}
