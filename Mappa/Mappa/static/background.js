const video = document.getElementById('Background');
const image = document.getElementsByClassName("rest_card");
// .addEventListener('click', (e) => console.log(e))
for (let i = 0; i < image.length; i++) {
    console.log(image[0])
    image[i].addEventListener('click', () => {
        fetch("app.json").then(Response => Response.json())
            .then((data) => {
                data.forEach(s => {
                    if (image[i].getElementsByTagName('h4')[0].innerText == s.name) {
                        console.log(s.trailer)
                        video.src = s.trailer
                    }
                });
            });
    }); 
}