$(document).ready(function() {
    let scroll_pos = 0;
    $(document).scroll(function() {
        scroll_pos =  $(this).scrollTop();
        if(scroll_pos > 100){
            $('.nav').css('background-color', '#121212');
        }else{
            $('.nav').css('background-color', 'rgba(0,0,0,0)');
        }
    });
});