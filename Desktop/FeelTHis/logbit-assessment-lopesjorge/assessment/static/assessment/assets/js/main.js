const body = document.body

//PAGES
const pageInitial = document.querySelector("#initial")
const pageVideo = document.querySelector("#video")
const pageModule = document.querySelector("#module")
const pageHome = document.querySelector("#home")


//VERIFICATION 
if (pageInitial) {
    body.classList.add("body__initial")

} else if (pageVideo) {
    body.classList.add("body__video")

} else if (pageModule) {
    body.classList.add("body__module")

} else if (pageHome) {
    body.classList.add("body__home")
}


// EVENTOS 🧙‍♂️
document.addEventListener("DOMContentLoaded", () => body.classList.add("DOMContentLoaded"))

