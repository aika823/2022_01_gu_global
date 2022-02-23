$('.btn-menu').mouseover(function() {
    $('.logo img').attr('src', '/static/images/logo_color.png');
    $('header').css({ 'background-color': '#fff' });
    $('.btn-menu').addClass('color');
    $('.btn-menu').removeClass('active');
    $(this).addClass('active');
    $('.header-content').css('display', 'block');
    if ($(this).hasClass('menu-company') == true) {
      $('.category-box').css('display', 'none');  
      $('.company-category').css('display', 'block');
    } else if ($(this).hasClass('menu-products') == true) {
      $('.category-box').css('display', 'none');  
      $('.product-category').css('display', 'grid');
    } else if ($(this).hasClass('menu-solution') == true) {
        $('.category-box').css('display', 'none');
        $('.solution-category').css('display', 'grid');
    } else if ($(this).hasClass('menu-support') == true) {
        $('.category-box').css('display', 'none');
        $('.support-category').css('display', 'block');
    }
});
$('.header-content').mouseleave(function() {
  if($('header').hasClass('.down') == true) {
    console.log('down')
    $('.logo img').attr('src', '/static/images/logo.png');
    $('header').css({ 'background-color': 'transparent' });
    $('.btn-menu').removeClass('color');
    $('.btn-menu').removeClass('active');
  }
  $('.category-box').css('display', 'none');
  $('.header-content').css('display', 'none');
});