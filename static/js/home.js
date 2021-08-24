// Append CSRF token on every request
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

(async () => {
  await axios.get('/remove-message/');
})();

(() => {
  const popup = document.querySelector('.popup');
  const cross = document.querySelector('.cross');

  cross.addEventListener('click', () => {
    popup.style.right = '-27%';
  });

  setTimeout(() => {
    popup.style.right = '0%';
  }, 650);
})();

(() => {
  const successMsg = document.querySelector('.success_message_cont');

  setTimeout(() => {
    if (successMsg) {
      successMsg.style.right = '-26%';
    }
  }, 5000);
})();

(() => {
  const button = document.querySelector('.hero').querySelector('button');

  button.addEventListener('click', () => {
    window.location.href = '/booking';
  });
})();
