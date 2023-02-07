const left = document.querySelector('.left');
const right = document.querySelector('.right');
const container = document.querySelector('.container');
var specs_left = document.querySelector('.specs-left');
var title_left = document.querySelector('#title-left');
var btn_left = document.querySelector('#btn-left');
var specs_right = document.querySelector('.specs-right');
var title_right = document.querySelector('#title-right');
var btn_right = document.querySelector('#btn-right');

left.addEventListener('mouseenter', () => container.classList.add('hover-left'));
left.addEventListener('mouseleave', () => container.classList.remove('hover-left'));
left.addEventListener('mouseenter', () => close_right());
right.addEventListener('mouseenter', () => container.classList.add('hover-right'));
right.addEventListener('mouseleave', () => container.classList.remove('hover-right'));
right.addEventListener('mouseenter', () => close_left());

function open_left(){
    specs_left.style.display = 'block';
    title_left.style.display = 'none';
    btn_left.style.display = 'none';
}

function open_right(){
    specs_right.style.display = 'block';
    title_right.style.display = 'none';
    btn_right.style.display = 'none';
}

function close_left(){
    specs_left.style.display = 'none';
    title_left.style.display = 'block';
    btn_left.style.display = 'block';
}

function close_right(){
    specs_right.style.display = 'none';
    title_right.style.display = 'block';
    btn_right.style.display = 'block';
}