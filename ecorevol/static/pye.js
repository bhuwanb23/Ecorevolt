Result Skip Results Iframe
EDIT ON
const sliderEl = document.querySelector("#range2")
const sliderValue = document.querySelector(".value2")

sliderEl.addEventListener("input", (event) => {
  const tempSliderValue = event.target.value; 
  sliderValue.textContent = tempSliderValue;
  
  const progress = (tempSliderValue / sliderEl.max) * 100;