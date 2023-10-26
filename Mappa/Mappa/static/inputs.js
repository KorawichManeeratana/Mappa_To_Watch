const infogather = document.querySelector(".infogather"),
selectBtn = infogather.querySelector(".sel-btn"),
options = infogather.querySelector(".options");

let genres = ["Action", "Adventure", "Shounen", "Shoujo", "Sci-Fi", "Horror", "Fantasy","Winning Award", "Slice of life", "Sport"]

function addGenres() {
    genres.forEach(genre => {
        let li = '<li onclick=updateName(this)>${genre}</li>';
        options.insertAdjacentHTML("beforeend", li);
    });
}
addGenres();

function updateName(selectedone){
    selectBtn.firstElementChild.innerText = selectedone.innerText
}

selectBtn.addEventListener("click", ()=> {
    infogather.classList.toggle("active");
});