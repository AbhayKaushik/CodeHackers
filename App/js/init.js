(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('.parallax').parallax();

    $('header .brand .menu-icon').click(function() {
      $('.menu-list').addClass('activate');
      $('menu').addClass('activate');
    })
    
    $('menu').click(function() {
      $('.menu-list').removeClass('activate');
      $('menu').removeClass('activate');
    })

  }); // end of document ready
})(jQuery); // end of jQuery name space
