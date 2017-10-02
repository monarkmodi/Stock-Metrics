var displayedImage = document.querySelector('.displayed-img');
var thumbBar = document.querySelector('.thumb-bar');

btn = document.querySelector('button');
var overlay = document.querySelector('.overlay');

/* Looping through images */
var i = 2;
while (i <= 4) {
  var newImage = document.createElement('img');
  var file = 'images/pic' + i + '.jpg';
  newImage.setAttribute('src', file);
  thumbBar.appendChild(newImage);
  newImage.onclick = function (listener) {
    var image_clicked = listener.target.getAttribute('src');
    displayedImage.setAttribute('src', image_clicked);
  }
  i++;
}


/* Wiring up the Darken/Lighten button */

}
