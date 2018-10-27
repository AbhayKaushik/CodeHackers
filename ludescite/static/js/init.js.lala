(function ($) {
	$(function () {

		$('.sidenav').sidenav();
		$('.parallax').parallax();

		// Nav menu icon click event
		$('header .brand .menu-icon').click(function () {
			$('.menu-list').addClass('activate');
			$('menu').addClass('activate');
		})

		// Nav menu list ending event
		$('menu').click(function (event) {
			// event.preventDefault();
			$('.menu-list').removeClass('activate');
			$('menu').removeClass('activate');
		})

		// page-transitions
		$(".board-wrapper").css("display", "none");
		$(".board-wrapper").fadeIn(1000);

		$(".transition").click(function (event) {
			event.preventDefault();
			linkLocation = this.href;
			$(".board-wrapper").fadeOut(500, redirectPage);
		});

		function redirectPage() {
			window.location = linkLocation;
		}

	}); // end of document ready
})(jQuery); // end of jQuery name space