// Lấy phần tử body
const body = document.querySelector('body');

// Tạo phần tử trái tim
const heart = document.createElement('div');
heart.classList.add('heart');

// Thiết lập vị trí ban đầu của trái tim
heart.style.left = '0px';
heart.style.top = '0px';

// Thêm trái tim vào body 
body.appendChild(heart);

// Sự kiện di chuyển chuột
document.addEventListener('mousemove', function(e) {

  // Cập nhật vị trí trái tim
  heart.style.left = e.clientX + 'px';
  heart.style.top = e.clientY + 'px';
  
});