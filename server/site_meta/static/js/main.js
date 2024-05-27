let currentAboutusIndex = 0;
let currentNewsIndex = 0;
const aboutusSlides = document.querySelectorAll('.aboutus__slider__slide');
const newsSlides = document.querySelectorAll('.news__slide');
const totalAboutusSlides = aboutusSlides.length;
const totalNewsSlides = newsSlides.length;

function updateAboutusSlidePosition() {
  const slider = document.querySelector('.aboutus__slider__container');
  slider.style.transform = `translateX(-${currentAboutusIndex * 100}%)`;
}

function updateNewsSlidePosition() {
  const slider = document.querySelector('.news__slider');
  slider.style.transform = `translateX(-${currentNewsIndex * 100}%)`;
}

function nextAboutusSlide() {
  currentAboutusIndex = (currentAboutusIndex + 1) % totalAboutusSlides;
  updateAboutusSlidePosition();
}

function nextNewsSlide() {
  currentNewsIndex = (currentNewsIndex + 1) % totalNewsSlides;
  updateNewsSlidePosition();
}

function prevAboutusSlide() {
  currentAboutusIndex = (currentAboutusIndex - 1 + totalAboutusSlides) % totalAboutusSlides;
  updateAboutusSlidePosition();
}

function prevNewsSlide() {
  currentNewsIndex = (currentNewsIndex - 1 + totalNewsSlides) % totalNewsSlides;
  updateNewsSlidePosition();
}
