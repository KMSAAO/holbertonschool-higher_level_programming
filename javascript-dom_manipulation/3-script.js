const btn = document.querySelector('#toggle_header');
const header = document.querySelector('header');

btn.addEventListener('click', () => {
    header.classList.toggle('red');
    header.classList.toggle('green');
});
