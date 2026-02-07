const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    const mylist = document.querySelector('#list_movies');

    data.results.forEach(element => {
        const li = document.createElement('li');
        li.textContent = element.title;

        mylist.appendChild(li)
    });
  })
  .catch(error => {
    console.error('error', error);
  });