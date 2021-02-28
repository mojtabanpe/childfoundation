$(window).scroll(function() {    
    var scroll = $(window).scrollTop();    
    if (scroll >= 160) {
        $(".top-header").addClass("d-none");
        $(".bottom-header").addClass("bottom-header-fixed")
        $(".carousel").addClass("be-relative");
        $(".cover").addClass("cover-go-bot");
        $(".content").addClass("content-go-bot");
    } else {
        $(".bottom-header").removeClass("bottom-header-fixed");
        $(".top-header").removeClass("d-none");
        $(".carousel").removeClass("be-relative");
        $(".cover").removeClass("cover-go-bot");
        $(".content").removeClass("content-go-bot");
    }
})
$('#open-sidebar').click(function() {
    $("#sidebar").addClass("show");
})
$('#close-sidebar').click(function() {
    $("#sidebar").removeClass("show");
})
