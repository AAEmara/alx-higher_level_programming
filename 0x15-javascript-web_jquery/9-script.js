$.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr',
  function(json) {
    const hello = json.hello;
    $('DIV#hello').after(hello);
  });
