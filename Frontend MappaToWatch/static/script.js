const wrapper = document.querySelector(".wrapper");
const loginlink = document.querySelector(".login-link");
const regislink = document.querySelector(".regis-link");
const btnpop= document.querySelector(".login-button");
const closeicon = document.querySelector(".close-icon")

regislink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
})

loginlink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
})

btnpop.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
})

closeicon.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
})
