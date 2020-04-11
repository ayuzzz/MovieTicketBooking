$(document).ready(function () {

  $('.second-button').on('click', function () {

    $('.animated-icon2').toggleClass('open');
  });

  $('.nav-item').on('click',function(){

  //Remove any previous active classes
  $('.nav-item').removeClass('active');

  //Add active class to the clicked item
  $(this).addClass('active');
  });
});



