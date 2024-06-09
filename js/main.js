"use strict"

function randomIntensity() {
  return (0.5 + Math.random()) / 1.6;
}

function rollBg() {
  const header = $('#header');
  const intensity = randomIntensity();
  header.css('box-shadow', '0 0 40px 0 rgba(30, 144, 255, ' + intensity + ')');
  setTimeout(function(){rollBg();}, 3000);
}
