jQuery(document).ready(function(){

  var help-text = $('<p>To understand more about markdown please have a look at the following <a href="http://stackoverflow.com/editing-help">link</a>.</p>');

  $("input[type=text]").focus(function () {
    $(this).next("p").css('display','inline').fadeOut(1000);
});
});
