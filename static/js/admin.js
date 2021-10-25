const date = new Date();

const renderCalendar = () => {
  date.setDate(1);

  const firstDayIndex = date.getDay();
  const lastDayIndex = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDay();
  const months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
  ];
  const month = months[date.getMonth()];
  const monthDays = document.querySelector('.days');
  const lastDay = new Date(
    date.getFullYear(),
    date.getMonth() + 1,
    0
  ).getDate();
  const prevLastDay = new Date(
    date.getFullYear(),
    date.getMonth(),
    0
  ).getDate();
  const nextDays = 7 - lastDayIndex - 1;

  document.querySelector('.date h1').innerHTML = month;
  document.querySelector('.date p').innerHTML = new Date().toDateString();

  let days = '';

  for (let i = firstDayIndex; i > 0; i--) {
    days += `<div class="prev_date">${prevLastDay - i + 1}</div>`;
  }

  for (let x = 1; x <= lastDay; x++) {
    if (
      x === new Date().getDate() &&
      date.getMonth() === new Date().getMonth()
    ) {
      days += `<div class="today">${x}</div>`;
    } else {
      days += `<div>${x}</div>`;
    }
  }

  for (let j = 1; j <= nextDays; j++) {
    days += `<div class="next_date">${j}</div>`;
    monthDays.innerHTML = days;
  }
};

document.querySelector('.prev').addEventListener('click', () => {
  date.setMonth(date.getMonth() - 1);

  renderCalendar();
});

document.querySelector('.next').addEventListener('click', () => {
  date.setMonth(date.getMonth() + 1);

  renderCalendar();
});

renderCalendar();
