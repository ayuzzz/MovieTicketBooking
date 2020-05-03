$(document).ready(function () {

  $('#preview-button').on('click', function () {
    if(validate_Time_Data())
    {
        $(".alert").alert('close');
        $('#save-button').attr("disabled", false);
        let divElement = '';
        let interval = Math.ceil($('#movie-duration').text()/60);
        let startTime = Math.ceil($('#start-time').val());
        let endTime = Math.ceil($('#end-time').val());
        let startTimeDropdown = $('#start-dropdown').val();
        let endTimeDropdown = $('#end-dropdown').val();

        let standardStartTime = convertToStandardTime(startTime, startTimeDropdown);
        let standardEndTime = convertToStandardTime(endTime, endTimeDropdown);
        let slots = new Array();
        let timeCounter = standardStartTime;

        while (timeCounter <= standardEndTime)
        {
            slots.push(convertFromStandardTime(timeCounter));
            timeCounter = timeCounter + interval;
        }

        for(let i = 0; i < slots.length; i++)
        {
            if(i < slots.length - 1)
                divElement = divElement + '<li><h6>' + slots[i].Time.toString() + ' ' + slots[i].TimeDropdown + ' - ' + slots[i+1].Time.toString() + ' ' + slots[i+1].TimeDropdown + '</h6></li>';
            else
                break;
        }

        let htmlString =  '<div class="col mx-auto">Slots Available : <ul id="slotsList">' + divElement  + '</ul></div>';
        $('#preview-slots').empty();
        $('#preview-slots').append(htmlString);
    }
    else
    {
        $(".alert").alert('close');
        $('#preview-slots').append('<div class="alert alert-danger mx-auto" role="alert">' +
                                    '<p>Please check the time and AM/PM properly <br>' +
                                    '- Both Start Time and End Time should be greater than or equal to 1 and less than 12<br>' +
                                    '- If AM/PM are same for start and end times, check if start time is smaller than end time<br>' +
                                    '- Time inserted will be converted to nearest higher value of hour<br>' +
                                    '- Time interval between start and end time should be at least equal to movie duration<br></p>' +
                                    '</div>');
    }
  });

  $('#save-button').on('click', function ()
  {
    if (validate_Time_Data() && validate_Data())
    {
        $('#save-button').attr("disabled", true);
        let rateOfTickets = $('#rate').val();
        let theatreId = $('#theatreDetails').children(":selected").attr("id");
        let movieId = $('#movie-id').text();
        let slots = $('#slotsList').children();
        let slotArray = new Array();

        for(let i = 0; i < slots.length; i++)
        {
            let slotObject = new Object();
            let slotStartEndTime = slots[i].innerText.trim().split("-");

            slotObject.MovieId = movieId;
            slotObject.TheatreId = theatreId;
            slotObject.RateOfTickets = Math.ceil(rateOfTickets);
            slotObject.StartTime = slotStartEndTime[0].trim();
            slotObject.EndTime = slotStartEndTime[1].trim();

            slotArray.push(slotObject);
        }

        $.ajax({
            url: "http://127.0.0.1:5000/insertSlots",
            type: "POST",
            data: JSON.stringify(slotArray),
            contentType: "application/json",
            success: function (data)
                    {
                        window.location.href = "/slots";
                    }
        });
    }
  });
});

function validate_Time_Data()
{
    let flag = true;
    let startTime = Math.ceil($('#start-time').val());
    let endTime = Math.ceil($('#end-time').val());
    let startTimeDropdown = $('#start-dropdown').val();
    let endTimeDropdown = $('#end-dropdown').val();
    let movieDuration = $('#movie-duration').text();
    let interval = Math.ceil(movieDuration/60);

    if($('#start-time').val().length < 0 || $('#end-time').val().length < 0)
    {
        flag = false;
    }

    if(startTimeDropdown === endTimeDropdown && (startTime >= endTime))
    {
        flag = false;
    }

    if(startTime > 12 || startTime < 1 || endTime > 12 || endTime < 1)
    {
        flag = false;
    }

    if(convertToStandardTime(endTime, endTimeDropdown) - convertToStandardTime(startTime, startTimeDropdown) < interval)
    {
        flag = false;
    }

    return flag;
}


function validate_Data()
{
    let rateOfTickets = $('#rate').val();

    if(rateOfTickets > 0)
        return true;
    else
        return false;
}

function convertToStandardTime(time, timeDropdown)
{
    if(timeDropdown == "AM")
    {
        return time;
    }
    else
    {
        return (12 + time);
    }
}

function convertFromStandardTime(time)
{
    let timeObject = new Object();

    if(time <= 12)
    {
        timeObject.Time = time;
        timeObject.TimeDropdown = "AM";
        return timeObject;
    }
    else
    {
        timeObject.Time = time - 12;
        timeObject.TimeDropdown = "PM";
        return timeObject;
    }
}