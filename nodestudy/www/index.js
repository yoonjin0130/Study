var 음료 = ''
var 금액 = 0
var 수량 = 0
function btn1() {
    음료 = '콜라'
    금액 = 500
    document.getElementById("step1_txt").classList.remove("dis-none")
    document.getElementById("step1_txt").innerText = '콜라를 주문했습니다. 500원';
}
function btn2() {
    음료 = '사이다'
    금액 = 450
    document.getElementById("step1_txt").classList.remove("dis-none")
    document.getElementById("step1_txt").innerText = '사이다를 주문했습니다. 450원';
}
function btn3() {
    음료 = '환타'
    금액 = 300
    document.getElementById("step1_txt").classList.remove("dis-none")
    document.getElementById("step1_txt").innerText = '환타를 주문했습니다. 300원';
}

function ipt1() {
    수량 = document.getElementById("s").value


document.getElementById("step2_txt").classList.remove("dis-none")
    document.getElementById("step2_txt").innerText = 음료 + 수량 + '개 금액은 '+ (금액 * 수량) +'원 입니다.'
}    

function ipt2() {
   var 지불 = document.getElementById("m").value
document.getElementById("step3_txt").classList.remove("dis-none")
    document.getElementById("step3_txt").innerText = '' + 지불 + '원을 받고 ' + (지불 - (금액 * 수량)) + '원 거스름돈을 받으세요.'        
}