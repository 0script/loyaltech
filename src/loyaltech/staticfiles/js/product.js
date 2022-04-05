const imgs=document.querySelectorAll('img.product-img');

imgs.forEach(img=>{
    /* Display the details when mouse is over the img cart item */

    img.addEventListener('mouseenter',(e)=>{
        img.classList.add('not');
        img.parentElement.firstElementChild.classList.add('display');

        img.parentElement.firstElementChild.addEventListener('mouseleave',()=>{
            img.parentElement.firstElementChild.classList.remove('display');
            img.classList.remove('not');
        });
    });

});
