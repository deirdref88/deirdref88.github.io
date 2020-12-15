// code for modals adapted from https://getbootstrap.com/docs/4.0/components/modal/

var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
};

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
};

//When user clicks the right button, play good sound if they want sound on - code adapted from https://www.w3schools.com/jsref/met_audio_play.asp
function play() {
    var sound = document.getElementById("sound").value;
    if (sound == "on") {
      var audio = document.createElement("AUDIO");
      audio.setAttribute("src", "/static/yay.mp3");
      audio.volume = 0.2;
      audio.play();
    };
};