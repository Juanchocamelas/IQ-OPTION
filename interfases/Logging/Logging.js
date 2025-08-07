 
 //Sonidos para botones y placeholders (input)
 const sound = document.getElementById("Sound_button");
const buttons = document.querySelectorAll("button");
  
  buttons.forEach(btn => {
    btn.addEventListener("click", () => {
      sound.currentTime = 0;
      sound.play();
    });
  });

 const keySound = document.getElementById("Single_type_key");
const inputs = document.querySelectorAll(".input-field");

inputs.forEach(input => {
  input.addEventListener("keydown", () => {
    keySound.currentTime = 0;
    keySound.play();
  });
});

/* Segunda pantalla al hacer click en registrarse*/

document.querySelector('.btn').onclick = () => {
  document.getElementById('registroPanel').classList.add('visible');
};
