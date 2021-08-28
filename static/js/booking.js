// Append CSRF token on every request
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const getElement = (tag) => {
  const element = document.querySelector(tag);

  return element;
};

const nameInput = getElement('#booking__name');
const emailInput = getElement('#booking__email');
const msgInput = getElement('#booking__message');
const phoneInput = getElement('#booking__phone');
const birthInput = getElement('#booking__date');
const postalInput = getElement('#booking__postal');
const nhsInput = getElement('#booking__nhs');
const nameLabel = getElement('#name_label');
const emailLabel = getElement('#email_label');
const msgLabel = getElement('#textarea_l');
const phoneLabel = getElement('#phone_label');
const birthLabel = getElement('#date_label');
const postalLabel = getElement('#postal_label');
const nhsLabel = getElement('#nhs_label');
const button = getElement('.continue_button');

if (window.innerWidth < 481) {
  birthInput.type = 'date';
  birthInput.style.padding = '0 5% 0 5%';
  birthLabel.style.display = 'none';
}

const focusOutDate = (e) => {
  if (!e.value && window.innerWidth > 480) {
    e.type = 'text';
  }
};

(() => {
  if (nameInput.value) {
    nameLabel.style.top = '29%';
    nameLabel.style.color = '#333333';
    nameLabel.style.fontSize = '0.55rem';

    nameLabel.innerHTML = 'Full Name';
    nameInput.style.border = 'none';
  }

  if (emailInput.value) {
    emailLabel.style.top = '29%';
    emailLabel.style.color = '#333333';
    emailLabel.style.fontSize = '0.55rem';

    emailLabel.innerHTML = 'Email Address';
    emailInput.style.border = 'none';
  }

  if (phoneInput.value) {
    phoneLabel.style.top = '29%';
    phoneLabel.style.color = '#333333';
    phoneLabel.style.fontSize = '0.55rem';

    phoneLabel.innerHTML = 'Phone Number (eg. +44 566 6465)';
    phoneInput.style.border = 'none';
  }

  if (birthInput.value) {
    birthLabel.style.top = '29%';
    birthLabel.style.color = '#333333';
    birthLabel.style.fontSize = '0.55rem';

    birthLabel.innerHTML = 'Date Of Birth';
    birthInput.style.border = 'none';
    birthInput.type = 'date';
  }

  if (postalInput.value) {
    postalLabel.style.top = '29%';
    postalLabel.style.color = '#333333';
    postalLabel.style.fontSize = '0.55rem';

    postalLabel.innerHTML = 'Postal Code';
    postalInput.style.border = 'none';
  }

  if (nhsInput.value) {
    nhsLabel.style.top = '29%';
    nhsLabel.style.color = '#333333';
    nhsLabel.style.fontSize = '0.55rem';

    nhsLabel.innerHTML = 'NHS Number';
    nhsInput.style.border = 'none';
  }

  // Adjust floating labels on focus
  nameInput.addEventListener('focusin', () => {
    nameLabel.style.top = '29%';
    nameLabel.style.color = '#333333';
    nameLabel.style.fontSize = '0.55rem';

    nameLabel.innerHTML = 'Full Name';
    nameInput.style.border = 'none';
  });

  nameInput.addEventListener('focusout', () => {
    if (!nameInput.value) {
      nameLabel.style.top = '42%';
      nameLabel.style.color = '#464646';
      nameLabel.style.fontSize = '0.81rem';
    }
  });

  emailInput.addEventListener('focusin', () => {
    emailLabel.style.top = '29%';
    emailLabel.style.color = '#333333';
    emailLabel.style.fontSize = '0.55rem';

    emailLabel.innerHTML = 'Email Address';
    emailInput.style.border = 'none';
  });

  emailInput.addEventListener('focusout', () => {
    if (!emailInput.value) {
      emailLabel.style.top = '42%';
      emailLabel.style.color = '#464646';
      emailLabel.style.fontSize = '0.81rem';
    }
  });

  phoneInput.addEventListener('focusin', () => {
    phoneLabel.style.top = '29%';
    phoneLabel.style.color = '#333333';
    phoneLabel.style.fontSize = '0.55rem';

    phoneLabel.innerHTML = 'Phone Number (eg. +44 566 6465)';
    phoneInput.style.border = 'none';
  });

  phoneInput.addEventListener('focusout', () => {
    if (!phoneInput.value) {
      phoneLabel.style.top = '42%';
      phoneLabel.style.color = '#464646';
      phoneLabel.style.fontSize = '0.81rem';
    }
  });

  birthInput.addEventListener('focusin', () => {
    birthLabel.style.top = '29%';
    birthLabel.style.color = '#333333';
    birthLabel.style.fontSize = '0.55rem';

    birthLabel.innerHTML = 'Date Of Birth';
    birthInput.style.border = 'none';
  });

  birthInput.addEventListener('focusout', () => {
    if (!birthInput.value) {
      birthLabel.style.top = '42%';
      birthLabel.style.color = '#464646';
      birthLabel.style.fontSize = '0.81rem';
    }
  });

  postalInput.addEventListener('focusin', () => {
    postalLabel.style.top = '29%';
    postalLabel.style.color = '#333333';
    postalLabel.style.fontSize = '0.55rem';

    postalLabel.innerHTML = 'Postal Code';
    postalInput.style.border = 'none';
  });

  postalInput.addEventListener('focusout', () => {
    if (!postalInput.value) {
      postalLabel.style.top = '42%';
      postalLabel.style.color = '#464646';
      postalLabel.style.fontSize = '0.81rem';
    }
  });

  nhsInput.addEventListener('focusin', () => {
    nhsLabel.style.top = '29%';
    nhsLabel.style.color = '#333333';
    nhsLabel.style.fontSize = '0.55rem';

    nhsLabel.innerHTML = 'NHS Number';
    nhsInput.style.border = 'none';
  });

  nhsInput.addEventListener('focusout', () => {
    if (!nhsInput.value) {
      nhsLabel.style.top = '42%';
      nhsLabel.style.color = '#464646';
      nhsLabel.style.fontSize = '0.81rem';
    }
  });

  // Send message
  button.addEventListener('click', async () => {
    if (!nameInput.value) {
      nameLabel.style.color = '#FF3C3C';
      nameLabel.innerHTML = 'This field is required';
      nameInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (!emailInput.value) {
      emailLabel.style.color = '#FF3C3C';
      emailLabel.innerHTML = 'This field is required';
      emailInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (!phoneInput.value) {
      phoneLabel.style.color = '#FF3C3C';
      phoneLabel.innerHTML = 'This field is required';
      phoneInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (!birthInput.value) {
      birthLabel.style.color = '#FF3C3C';
      birthLabel.innerHTML = 'This field is required';
      birthInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (!postalInput.value) {
      postalLabel.style.color = '#FF3C3C';
      postalLabel.innerHTML = 'This field is required';
      postalInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (!nhsInput.value) {
      nhsLabel.style.color = '#FF3C3C';
      nhsLabel.innerHTML = 'This field is required';
      nhsInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    if (nhsInput.value.length !== 10) {
      nhsLabel.style.color = '#FF3C3C';
      nhsLabel.innerHTML = 'Please enter a valid NHS number';
      nhsInput.style.border = '0.5px solid #FF3C3C';

      return;
    }

    const res = await axios.post('/booking/new-user/', {
      name: nameInput.value,
      email: emailInput.value,
      phone: phoneInput.value,
      birth: birthInput.value,
      postal: postalInput.value,
      nhs: nhsInput.value,
    });

    if (res.data.status === 200) {
      window.location.href = '/booking/date/';
    }
  });
})();
