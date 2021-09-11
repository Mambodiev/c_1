/* Project specific Javascript goes here. */
//   language

$('.selectpicker').on('change', function () {
	$(this).closest('form').submit();
  });
//   end language


$(document).ready(function() {
  "use strict";

  $('ul.navar-nav > li').click(function(e) {
    e.preventDefault();
    $('ul.navar-nav > li').removeClass('active');
    $(this).addClass('active');
  });
});