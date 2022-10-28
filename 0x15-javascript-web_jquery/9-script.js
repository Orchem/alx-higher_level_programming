document.addEventListener('DOMContentLoaded', () => {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', body =>
    $('div#hello').text(body.hello));
});
