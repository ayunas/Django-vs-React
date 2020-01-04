console.log('javascript for Django vs React');
console.log('i still test this file');


const [djangoBtn,reactBtn] = document.querySelectorAll('button');

// djangoBtn.onclick = () => console.log('i have been clicked');
// reactBtn.onclick = () => console.log('react button has been clicked');

// djangoBtn.onclick = getree;

djangoBtn.addEventListener('click',getree);

function getree() {
    console.log('get the tree');
}

