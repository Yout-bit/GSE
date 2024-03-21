function toggleSubSession() {
    var subSession = document.getElementById("subSession");
    var overlay = document.getElementById("overlay");
    subSession.classList.toggle("open");
    overlay.classList.toggle("active");
}
function refreshPage() {
    location.reload(); 
}
function goBack() {
  window.history.back();
}

function resetUserProfile() {
    // Get the CSRF token from the cookie
    const csrftoken = getCookie('csrftoken');
        fetch('/reset_user_profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                // Add any other headers if needed
                'X-CSRFToken': csrftoken  // Include the CSRF token in the headers
            },
            // Add body if needed
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            // Handle response data as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
          
//-----------------updateCherriesValue-----------------------------------------------------------------
// Function to fetch and update cherries value from the server
function updateCherriesValue() {
    // Send an AJAX request to fetch the updated cherries value
    $.ajax({
        url: '/api/get_cherries_value/',  // URL to your API endpoint that returns the cherries value
        type: 'GET',
        success: function(response) {
            // Update the displayed cherries value with the fetched value
            var cherry_num_element = document.getElementById("cherry_num");
            cherry_num_element.textContent = response.cherries_value;
        },
        error: function(xhr, errmsg, err) {
            // Handle errors if any
            console.log(xhr.status + ": " + xhr.responseText); // Log the error message
        }
    });
}
//-----------------update carbon footprint-----------------------------------------------------------------
// Function to fetch and update carbon footprint value from the server
function updateCarbonFootprint() {
    // Send an AJAX request to fetch the updated carbon footprint value
    $.ajax({
        url: '/api/get_carbon_footprint_value/',  // URL to your API endpoint that returns the carbon footprint value
        type: 'GET',
        success: function(response) {
            // Update the displayed carbon footprint value with the fetched value
            var carbon_footprint_element = document.getElementById("carbon-footprint");
            carbon_footprint_element.textContent = "CarbonFootprint: " + response.carbon_footprint_value+"/10";
        },
        error: function(xhr, errmsg, err) {
            // Handle errors if any
            console.log(xhr.status + ": " + xhr.responseText); // Log the error message
        }
    });
}
//-----------------carbon footprint-----------------------------------------------------------------
// Function to increment carbon footprint value

$(document).ready(function() {
  setInterval(function() {
      $.ajax({
          url: '/api/increment_carbon_footprint/',
          type: 'POST',
          dataType: 'json',
          success: function(response) {
              if (response.success) {
                  $('#carbon-footprint').text("Carbon Footprint: " + response.new_carbon_footprint_value + "/10");
              } else {
                  console.error('Failed to increment carbon footprint value:', response.error);
                  // Optionally, display an error message to the user
                  // $('#error-message').text('Failed to increment carbon footprint value. Please try again later.');
              }
          },
          error: function(xhr, errmsg, err) {
              console.error(xhr.status + ": " + xhr.responseText);
              // Optionally, display an error message to the user
              // $('#error-message').text('An error occurred while communicating with the server. Please try again later.');
          }
      });
  }, 10000); // Repeat every 10 seconds
});


// Function to retrieve the CSRF token from cookies
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie name matches the CSRF token pattern
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
// Include the CSRF token in AJAX requests
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});


function toggleSubSession() {
    var subSession = document.getElementById("subSession");
    var overlay = document.getElementById("overlay");
    subSession.classList.toggle("open");
    overlay.classList.toggle("active");
}

function redirectToPage(pageUrl) {
  var currentPageUrl = window.location.href;
  if (currentPageUrl.indexOf(pageUrl) === -1) {
      window.location.href = pageUrl;
  }
}
// Define a JavaScript variable
var cherry_num_value = 2; // Initialize to 0

// Access the <p> element using its ID
var cherry_num_element = document.getElementById("cherry_num");
// Set the content of the <p> element to the value of the JavaScript variable
cherry_num_element.textContent = cherry_num_value;

function sendDataToDjango(scannedNumber) {
  var xhr = new XMLHttpRequest();
  xhr.open("POST", handleScannedNumberUrl, true); // Use the URL from the global variable
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

  // Include CSRF token in the request headers
  var csrftoken = getCookie("csrftoken");
  xhr.setRequestHeader("X-CSRFToken", csrftoken);

  xhr.onreadystatechange = function () {
    if (xhr.readyState === XMLHttpRequest.DONE) {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        if (response.increaseCherryCount) {
          increaseCherryCount(); // Call function to increase cherry count
        }
        console.log("Data sent successfully");
      } else {
        console.error("Error sending data:", xhr.statusText);
      }
    }
  };
  xhr.send("scanned_number=" + encodeURIComponent(scannedNumber));
}

function increaseCherryCount() {
  var cherryNumElement = document.getElementById("cherry_num");
  var cherryNumValue = parseInt(cherryNumElement.textContent);
  cherryNumValue = +10; // Increase cherry count by 1
  cherryNumElement.textContent = cherryNumValue; // Update the cherry count in the DOM
}