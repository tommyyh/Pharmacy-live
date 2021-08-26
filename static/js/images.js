const images = document.querySelector('.images').querySelectorAll('img');
let isOpen = false;

images.forEach((img) => {
  img.addEventListener('click', () => {
    isOpen = !isOpen;

    console.log(isOpen);
  });
});
