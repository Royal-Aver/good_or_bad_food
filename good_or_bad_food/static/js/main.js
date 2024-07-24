var swiper = new Swiper(".mySwiper", {
  spaceBetween: 30,
  effect: "fade",
  autoplay: {
    delay: 5000,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
});


// const openModalBtn = document.getElementById('openModal');
// const modal = document.getElementById('modal');
// const closeModalBtn = document.getElementsByClassName('close')[0];

// openModalBtn.addEventListener('click', function() {
//   modal.style.display = 'block';
// });

// closeModalBtn.addEventListener('click', function() {
//   modal.style.display = 'none';
// });

// window.addEventListener('click', function(event) {
//   if (event.target == modal) {
//     modal.style.display = 'none';
//   }
// });


document.addEventListener("DOMContentLoaded", function() {
  const dropdownButton = document.querySelector('.category-menu__btn');
  const dropdown = document.querySelector('.category-menu__dropdown');

  dropdownButton.addEventListener('click', function() {
      dropdown.classList.toggle('active');
  });


  document.addEventListener('click', function(event) {
      if (!dropdown.contains(event.target) && dropdown.classList.contains('active')) {
          dropdown.classList.remove('active');
      }
  });
});


// document.querySelector('.filter__btn').addEventListener('click', function() {
//   document.querySelector('.filter__form-menu').classList.toggle('show-filter');
// });


