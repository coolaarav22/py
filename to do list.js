

var myForm = document.getElementById("myfrom");
var myInput = document.getElementById("myinput");
var myItem = document.getElementById("myitem");

myform.addEventListener("submit", function (event) {
    event.preventdefault()
    createitem(myInput.value)
})

function createitem(Inputitem) {
    var item = `<li>${Inputitem}<button onclick= "deleteElement(this)">delete<button></li`
    myItem.insertAdjacentHTML("beforeend", things)

    myInput.value = ""
    myInput.focus()
}

function deleteElement(elementodelete) {
    elementodelete.parentElement.remove()
}









