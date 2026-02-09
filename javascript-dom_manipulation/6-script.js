const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    const name = document.querySelector('#character');
    name.textContent = data.name;
  })
  .catch(error => {
    console.error('حدث خطأ', error);
  });
