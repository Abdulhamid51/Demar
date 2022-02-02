$('button.stone-btn').on('click', function(){
    $button = $(this)
    $product_id = $(this).data('id')
    $mkv = $(this).data('mkv')
    $.ajax({
        url:'/cart-create/',
        type:'GET',
        data:{
            'product_id':$product_id,
            'mkv':$mkv
        },
        success:function(response){
            if(response['data']==='created'){
                $button.css('background-color','#000')
            }
        }
    })
})




const burger = document.getElementById('burger')
const menu = document.getElementById('ul')

burger.addEventListener('click', () => {
    menu.classList.toggle('show')
})


const search = document.querySelector(".search-btn")
const background = document.querySelector('.white')
const clear = document.querySelector(".clear-btn")

search.addEventListener('click', () => {
    background.classList.add('wash')
})

clear.addEventListener('click', () => {
    background.classList.remove('wash')
})

const filter = document.querySelector(".catalog-btn")
const unhiddenItem = document.querySelector(".catalog-hid")

filter.addEventListener('click', () => {
    unhiddenItem.classList.toggle('showes')
})



