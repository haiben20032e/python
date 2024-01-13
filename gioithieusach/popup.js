const loginBtn = document.getElementById('loginBtn');
const registerBtn = document.getElementById('registerBtn');

const loginPopup = document.getElementById('loginPopup');
const registerPopup = document.getElementById('registerPopup');

const closeBtns = document.querySelectorAll('.close');

loginBtn.addEventListener('click', () => {
  loginPopup.style.display = 'block';
});

registerBtn.addEventListener('click', () => {
  registerPopup.style.display = 'block'; 
});

closeBtns.forEach(btn => {
  btn.addEventListener('click', () => {
    loginPopup.style.display = 'none';
    registerPopup.style.display = 'none';
  });
});
