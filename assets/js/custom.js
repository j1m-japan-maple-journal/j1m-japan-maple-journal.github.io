document.querySelectorAll('.tree-lightbox').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    document.getElementById('tree-lightbox-img').src = link.href;
    document.getElementById('tree-lightbox-overlay').style.display = 'flex';
  });
});

document.getElementById('tree-lightbox-overlay')
  ?.addEventListener('click', () => {
    document.getElementById('tree-lightbox-overlay').style.display = 'none';
  });