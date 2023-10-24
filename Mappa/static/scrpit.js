const image = document.getElementById('img');
const video = document.getElementById('Background');

image.addEventListener('click', () => {
    if (video.getAttribute('src') === 'video1.mp4') {
        video.setAttribute('src', '${trailer}');
    } else {
        video.setAttribute('src', 'video1.mp4');
    }
});