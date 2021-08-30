// Append CSRF token on every request
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

(async () => {
  await axios.get('/remove-message/');
})();

(() => {
  const popup = document.querySelector('.popup');
  const cross = document.querySelector('.cross');

  if (window.innerWidth > 1024) {
    cross.addEventListener('click', () => {
      popup.style.right = '-27%';
    });

    setTimeout(() => {
      popup.style.right = '0%';
    }, 780);
  } else {
    cross.addEventListener('click', () => {
      popup.style.top = '-4.3rem';
    });

    setTimeout(() => {
      popup.style.top = '0%';
    }, 780);
  }
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

(() => {
  const button = document.querySelector('.map_book');

  button.addEventListener('click', () => {
    window.location.href = '/booking';
  });
})();
