/*
  ---------------------------------------------------
    Copyright (c) Abubaker Saeed (@AbubakerSaeed96)
                  (MIT LICENSE)

  Check it out on GitHub:
     github.com/AbubakerSaeed/plants-shopping-uix
  ---------------------------------------------------
*/

// GSAP
// ---------------------------------------
gsap.registerPlugin(Flip);

// HELPERS
// ---------------------------------------
let $ = (e) => document.querySelector(e);

// VARIABLES
// ---------------------------------------
let listContainer = $(".basket__list");
let items = gsap.utils.toArray(".item__image");

// HACKING
// ---------------------------------------
items.forEach((item) => {
  let itemContainer = item.parentNode;

  item.addEventListener("click", () => {
    let state = Flip.getState(item);

    const newContainer =
          item.parentNode === itemContainer ? listContainer : itemContainer;

    item.parentNode === itemContainer
      ? item.classList.add("basket__item")
    : item.classList.remove("basket__item");

    newContainer.appendChild(item);

    Flip.from(state, {
      duration: 1,
      ease: "power1.inOut",
      scale: true,
      zIndex: 10,
    });
  });
});

// On *Window* load
// Click on plant 1, plant 3, & plant 6
// ---------------------------------------
window.addEventListener("load", () => {
  items[0].click();
  setTimeout(() => {
    items[2].click();
  }, 1000);
  setTimeout(() => {
    items[5].click();
  }, 2000);
});
document.body.insertAdjacentHTML('afterbegin', `<a href="https://github.com/yairEO/ui-range" target="_blank"><img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Logo.png"/></a>`)

// These slider range component was used in my other component:
// https://github.com/yairEO/color-picker

var settings = {
  visible: 1, 
  theme: {
    background: "rgba(0,0,0,.9)",
  },
  CSSVarTarget: document.querySelector('.range-slider'),
  knobs: [
    {
      label: '<h2>These Are Some of The Variables:</h2>',
      render: ' ',
    },
    "Thumb",
    {
      cssVar: ['thumb-size', 'px'],
      label: 'thumb-size',
      type: 'range',
      min: 6, max: 33 //  value: 16,
    },
    {
      cssVar: ['thumb-color'], // alias for the CSS variable
      label: 'thumb-color',
      type: 'color',
    },
    "Value",
    {
      cssVar: ['value-active-color'], // alias for the CSS variable
      label: 'value active color',
      type: 'color',
      value: 'white'
    },
    {
      cssVar: ['value-background'], // alias for the CSS variable
      label: 'value-background',
      type: 'color',
    },
    {
      cssVar: ['value-background-hover'], // alias for the CSS variable
      label: 'value-background-hover',
      type: 'color',
    },
    {
      cssVar: ['primary-color'], // alias for the CSS variable
      label: 'primary-color',
      type: 'color',
    },
    // {
    //   cssVar: ['value-offset-y', 'px'],
    //   label: 'value-offset-y',
    //   type: 'range', value: 5, min: -10, max: 20
    // },
    "Track",
    {
      cssVar: ['track-height', 'px'],
      label: 'track-height',
      type: 'range', value: 8, min: 6, max: 33
    },
    {
      cssVar: ['progress-radius', 'px'],
      label: 'progress-radius',
      type: 'range', value: 20, min: 0, max: 33
    },
    {
      cssVar: ['progress-background'], // alias for the CSS variable
      label: 'progress-background',
      type: 'color',
      value: '#EEEEEE'
    },
    {
      cssVar: ['fill-color'], // alias for the CSS variable
      label: 'fill-color',
      type: 'color',
      value: '#0366D6'
    },
    "Ticks",
    {
      cssVar: ['show-min-max'],
      label: 'hide min max',
      type: 'checkbox',
      value: 'none'
    },
    {
      cssVar: ['ticks-thickness', 'px'],
      label: 'ticks-thickness',
      type: 'range',
      value: 1, min: 0, max: 10
    },
    {
      cssVar: ['ticks-height', 'px'],
      label: 'ticks-height',
      type: 'range',
      value: 5, min: 0, max: 15
    },
    {
      cssVar: ['ticks-gap', 'px'],
      label: 'ticks-gap',
      type: 'range',
      value: 5, min: 0, max: 15
    },
    {
      cssVar: ['min-max-x-offset', '%'],
      label: 'min-max-x-offset',
      type: 'range',
      value: 10, step: 1, min: 0, max: 100
    },
    {
      cssVar: ['min-max-opacity'],
      label: 'min-max-opacity',
      type: 'range', value: .5, step: .1, min: 0, max: 1
    },
    {
      cssVar: ['ticks-color'], // alias for the CSS variable
      label: 'ticks-color',
      type: 'color',
      value: '#AAAAAA'
    },
  ]
}

new Knobs(settings)

