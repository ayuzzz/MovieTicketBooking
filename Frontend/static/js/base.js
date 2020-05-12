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

  let ticketCost = Math.ceil($('#rate-of-ticket').text());
  $('#amount').val(ticketCost);

  $('#number-of-tickets').on('change',
      function()
      {
        let numTickets = $('#number-of-tickets').val();
        let ticketCost = Math.ceil($('#rate-of-ticket').text());

        let amount = numTickets * ticketCost;

        $('#amount').val(amount)
      }
  );
});



