$('.btn-menu').mouseover(function() {
    $('.logo img').attr('src', '/static/images/logo_color.png');
    $('header').css({ 'background-color': '#fff' });
    $('.btn-menu').addClass('color');
    $(this).addClass('active');
    $('.header-content').css('display', 'block');
    if ($(this).hasClass('menu-company') == true) {
        $('.company-category').css('display', 'block');
    } else if ($(this).hasClass('menu-products') == true) {
        $('.product-category').css('display', 'grid');
    } else if ($(this).hasClass('menu-solution') == true) {
        $('.solution-category').css('display', 'grid');
    } else if ($(this).hasClass('menu-support') == true) {
        $('.support-category').css('display', 'block');
    }
});
$('.btn-menu').mouseleave(function() {
    $('.logo img').attr('src', '/static/images/logo.png');
    $('header').css({ 'background-color': 'transparent' });
    $('.btn-menu').removeClass('color');
    $(this).removeClass('active');
    $('.category-box').css('display', 'none');
    $('.header-content').css('display', 'none');
});