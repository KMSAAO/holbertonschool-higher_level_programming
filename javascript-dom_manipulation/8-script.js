document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://hellosalut.stefanbohacek.com/?lang=fr';

    fetch(url)
    .then(response => {
        return response.json();
    })
    .then(data => {
        const hello1 = document.querySelector('#hello');
        hello1.textContent = data.hello;
    })
    .catch(error => {
            console.error('Error fetching data:', error);
        });
});
