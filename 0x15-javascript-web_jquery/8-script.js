$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json',
  function (json) {
    const results = json.results;
    for (let i = 0; i < results.length; i++) {
      const title = results[i].title;
      $('UL#list_movies').after('<li>' + title + '</li>');
    }
  });
