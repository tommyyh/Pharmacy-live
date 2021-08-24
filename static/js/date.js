// Append CSRF token on every request
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';

const getElement = (tag) => {
  const element = document.querySelector(tag);

  return element;
};

const times = [
  '9:00',
  '9:05',
  '9:10',
  '9:15',
  '9:20',
  '9:25',
  '9:30',
  '9:35',
  '9:40',
  '9:45',
  '9:50',
  '9:55',
  '10:00',
  '10:05',
  '10:10',
  '10:15',
  '10:20',
  '10:25',
  '10:30',
  '10:35',
  '10:40',
  '10:45',
  '10:50',
  '10:55',
  '11:00',
  '11:05',
  '11:10',
  '11:15',
  '11:20',
  '11:25',
  '11:30',
  '11:35',
  '11:40',
  '11:45',
  '11:50',
  '11:55',
  '12:00',
  '12:05',
  '12:10',
  '12:15',
  '12:20',
  '12:25',
  '12:30',
  '12:35',
  '12:40',
  '12:45',
  '12:50',
  '12:55',
  '14:05',
  '14:10',
  '14:15',
  '14:20',
  '14:25',
  '14:30',
  '14:35',
  '14:40',
  '14:45',
  '14:50',
  '14:55',
  '15:00',
  '15:05',
  '15:10',
  '15:15',
  '15:20',
  '15:25',
  '15:30',
  '15:35',
  '15:40',
  '15:45',
  '15:50',
  '15:55',
  '16:00',
  '16:05',
  '16:10',
  '16:15',
  '16:20',
  '16:25',
  '16:30',
  '16:35',
  '16:40',
  '16:45',
  '16:50',
  '16:55',
  '17:00',
  '17:05',
  '17:10',
  '17:15',
  '17:20',
  '17:25',
  '17:30',
  '17:35',
  '17:40',
  '17:45',
  '17:50',
  '17:55',
  '18:00',
  '18:05',
  '18:10',
  '18:15',
  '18:20',
  '18:25',
  '18:30',
];

const datePicker = getElement('.date_picker');

datePicker.innerHTML = times
  .map(
    (time) =>
      `<div class="date_picker_item_dis">
    <h6>${time}</h6>
  </div>`
  )
  .join('');

// Check for available times
const dateInput = getElement('#booking__date');
const continueBooking = getElement('.continue_button');
const datePickerErr = getElement('.date_picker_error');
const bookAppointment = getElement('#book_appointment');
const datePickerSuccess = getElement('.date_picker_success');

continueBooking.addEventListener('click', async () => {
  dateInput.addEventListener('focusin', () => {
    datePickerErr.classList.remove('date_picker_error_on');
  });

  if (!dateInput.value) {
    datePickerErr.classList.add('date_picker_error_on');

    return;
  }

  const res = await axios.post('/booking/new-date/', {
    date: dateInput.value,
  });

  const available_times = res.data.available_times;

  datePickerSuccess.classList.add('date_picker_success_on');

  // Show in html
  datePicker.innerHTML = available_times
    .map(
      (time) =>
        `<div class="date_picker_item">
    <h6>${time}</h6>
  </div>`
    )
    .join('');

  // Change button
  bookAppointment.innerText = 'Pick a Time';

  // Add event listener on time clicks
  const timeItems = document.querySelectorAll('.date_picker_item');
  let selectedTime;

  timeItems.forEach((timeItem) => {
    timeItem.addEventListener('click', (e) => {
      // Reset the previous ones
      timeItems.forEach((timeItem) => {
        timeItem.style.background = '#eeeeee';
      });

      if (e.target.className === 'date_picker_item') {
        // Re-assign value
        selectedTime = e.target.querySelector('h6').textContent;

        e.target.style.background = '#ffb498';
      } else {
        // Re-assign value
        selectedTime = e.target.textContent;

        e.target.parentNode.style.background = '#ffb498';
      }

      bookAppointment.style.background = '#046865';
      bookAppointment.style.cursor = 'pointer';
      bookAppointment.disabled = false;
      bookAppointment.innerHTML = 'Book appointment';
    });
  });

  bookAppointment.addEventListener('click', async () => {
    const res = await axios.post('/booking/book-appointment/', {
      date: dateInput.value,
      time: selectedTime,
    });

    if (res.data.status === 200) {
      window.location.href = '/';
    }
  });
});
