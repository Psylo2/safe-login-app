const popupItems = document.querySelectorAll('.popup-item');
const body = document.querySelector('body');
var i=0,j=0,z=0,flag=false;
var nextArrow=document.querySelectorAll('.slide_img__next');
var prevArrow=document.querySelectorAll('.slide_img__prev');
let standartDotColor="rgba(0, 0, 0, 0.6)";
let unlock = true;
let el=document.querySelector('.slide_img_4').querySelector(".slide_img__next");
let nextTiming=3000;
const timeout = 800;
let dots=document.querySelectorAll(".dots");

let timeID=window.setInterval(nextClick, nextTiming);

for (let k=0;k<dots.length;k++){
dots[k].addEventListener("click",function(event){
    i = (event.target.getAttribute("for").slice(-1))-1;
    z = i;
    flag = true;
    clearInterval(timeID);
    timeID=window.setInterval(nextClick, nextTiming);
dotLight(event.target);
});
}

for(j=0;j<nextArrow.length;j++){
    nextArrow[j].addEventListener('click', event => {
        if (i>=nextArrow.length)
            i = 0;
        clearInterval(timeID);
        timeID=window.setInterval(nextClick, nextTiming);
        i = (event.target.getAttribute("for").slice(-1))-1;
        z = i;
        flag = true;
        dotLight(event.target);
    });
}

for(j=0;j<prevArrow.length;j++){
    prevArrow[j].addEventListener('click', event => {
        if (i>=prevArrow.length)
            i = 0;
        clearInterval(timeID);
        timeID=window.setInterval(nextClick, nextTiming);
        i = (event.target.getAttribute("for").slice(-1))-1;
        z = i;
        flag = true;
        dotLight(event.target);
    });
}

dotLight(el);

function removePrev(dot){
    dot="dot"+dot;
    for (k=0;k<dots.length;k++) {
        if (dots[k] != dot) {
            dots[k].style.backgroundColor = standartDotColor;
        }
    }
}

function dotLight(el){
    let myCheck=el.getAttribute("for");
    myCheck=myCheck.slice(-1);
    removePrev(myCheck);
 i = myCheck;
    myCheck="dot"+myCheck;
    let abs=document.querySelector("#"+myCheck);
    switch(true) {
        case myCheck=="dot1":
            abs.style.backgroundColor="#795548";
            break;
        case myCheck=="dot2":
            abs.style.backgroundColor="#F44336";
            break;
        case myCheck=="dot3":
            abs.style.backgroundColor="#2196F3";
            break;
        case myCheck=="dot4":
            abs.style.backgroundColor="#4CAF50";
            break;
        default:
        // code block
    }



}
function nextClick(){
   if(!flag){
       i = (el.getAttribute("for").slice(-1))-1;
   }
   else{
       flag = false;
       i = z;
   }

    console.log(i);
     el=nextArrow[i];
    const evnt = el["click"];
    console.log(el);
        evnt.call(el);
        i++;
    if (i>=nextArrow.length)
        i = 0;
    dotLight(el);
}

if (popupItems.length > 0) {
    for (let index = 0; index < popupItems.length; index++) {
        const popupItem = popupItems[index];
        popupItem.addEventListener("click", function (e) {
            let currentImg=e.target.src;
            console.log(currentImg);
            const currentPopup = document.getElementById('popup');
            popupOpen(currentPopup,currentImg);
            e.preventDefault();
        });
    }
}
const popupCloseIcon = document.querySelectorAll('.close-popup');
if (popupCloseIcon.length > 0) {
    for (let index = 0; index < popupCloseIcon.length; index++) {
        const el = popupCloseIcon[index];
        el.addEventListener('click', function (e) {
            popupClose(el.closest('.popup'));
            e.preventDefault();
        });
    }
}

function popupOpen(currentPopup,currentImg) {
    document.querySelector('.popup__image-content').src=currentImg;
    if (currentPopup && unlock) {
        const popupActive = document.querySelector('.popup.open');
        if (popupActive) {
            popupClose(popupActive, false);
        } else {
            bodyLock();
        }
        currentPopup.classList.add('open');
        currentPopup.addEventListener("click", function (e) {
            if (!e.target.closest('.popup__content')) {
                popupClose(e.target.closest('.popup'));
            }
        });
    }
}

function popupClose(popupActive, doUnlock = true) {
    if (unlock) {
        popupActive.classList.remove('open');
        if (doUnlock) {
            bodyUnLock();
        }
    }
}

function bodyLock() {
    body.classList.add('lock');

    unlock = false;
    setTimeout(function () {
        unlock = true;
    }, timeout);
}

function bodyUnLock() {
    setTimeout(function () {
        body.style.paddingRight = '0px';
        body.classList.remove('lock');
    }, timeout);

    unlock = false;
    setTimeout(function () {
        unlock = true;
    }, timeout);
}