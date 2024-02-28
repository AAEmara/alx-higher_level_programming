$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json',
  function (json) {
    const name = json.name;
    $('DIV#character').append(name);
  });
