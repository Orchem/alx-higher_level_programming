$.get('https://swapi-api.hbtn.io/api/films/?format=json', (body, status) => {
  const movies = body.results;
  for (const movie of movies) {
    $('ul#list_movies').append(`<li>${movie.title}</li>`);
  }
});
