let circles = document.querySelectorAll(".circle");
let text = document.querySelector(".hex-code");
const rgb2hex = (rgb) => `#${rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/).slice(1).map(n => parseInt(n, 10).toString(16).padStart(2, '0')).join('')}`;
for (let i of circles) {
  i.addEventListener("pointerover", function() {
        changeText(i);
  })
  {
  i.addEventListener("pointerleave", function() {
        resetText(i);
  })
  };
  i.addEventListener("click", function() {
        copyText(i);
  })};

function changeText(circle) {
    text.innerText = `${rgb2hex(circle.style.backgroundColor)}`
    text.style.color = circle.style.backgroundColor;
}
function resetText(circle) {
    text.innerText = ""
}
function copyText(circle) {
    navigator.clipboard.writeText(`${rgb2hex(circle.style.backgroundColor)}`);
    text.innerHTML = "Copied!"
}