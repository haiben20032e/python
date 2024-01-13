  // Lấy các element
  const imgs = document.querySelectorAll('.main img'); 
  const nextBtn = document.querySelector('.next');
  const prevBtn = document.querySelector('.prev');

  let currentIndex = 0;

  // Xử lý click next
  nextBtn.addEventListener('click', () => {

    currentIndex++;
    if(currentIndex >= imgs.length) {
      currentIndex = 0;
    }

    showImg(currentIndex);

  });

  // Xử lý click prev
  prevBtn.addEventListener('click', () => {

    currentIndex--;
    if(currentIndex < 0) {
      currentIndex = imgs.length - 1;
    }

    showImg(currentIndex);
    
  });

  // Hàm hiển thị ảnh
  function showImg(index) {

    imgs.forEach(img => img.classList.remove('active'));

    imgs[index].classList.add('active');

  }