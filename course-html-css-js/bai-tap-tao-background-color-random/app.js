let array_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]

console.log(_.without(array_of_numbers, 3));

var body = document.getElementById('gradient');
// var input1 = document.getElementsByClassName("input1")[0];
var input1 = document.querySelector(".input1")
var input2 = document.getElementsByClassName("input2")[0];
var h3 = document.getElementsByTagName('h3')[0];

// console.log(input1);
// console.log(input2);
// console.log(h3);


function set_gradient(event) {
    // console.log(event.target.value);
    // console.log(input1.value);
    body.style.background = "linear-gradient(to right" + "," + input1.value + "," + input2.value + ")";

    h3.textContent = body.style.background;
}


input1.addEventListener('input', set_gradient)
input2.addEventListener('input', set_gradient)