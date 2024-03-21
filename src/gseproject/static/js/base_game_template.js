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
        alert("Profile Reset")
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



//------------------Location Scanner----------------------

// Function to calculate the distance between two points
function calculateDistance(lat1, lon1, lat2, lon2) {
const R = 6371000; // Radius of the Earth in meters
const dLat = (lat2 - lat1) * (Math.PI / 180); // Convert degrees to radians
const dLon = (lon2 - lon1) * (Math.PI / 180);
const a =
  Math.sin(dLat / 2) * Math.sin(dLat / 2) +
  Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
  Math.sin(dLon / 2) * Math.sin(dLon / 2);
const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
const distance = R * c; // Distance in meters
return distance;
}

// Function to find buildings within the specified range
function findBuildingsWithinRange(latitude, longitude, maxRange) {
  const userLocation = { lat: latitude, lng: longitude };
  const buildingsWithinRange = [];

  buildings.forEach((building) => {
    const distance = calculateDistance(
      userLocation.lat,
      userLocation.lng,
      building.location.lat,
      building.location.lng
    );

    if (distance <= maxRange) {
      buildingsWithinRange.push(building);
    }
  });

  return buildingsWithinRange;
}

// Function to handle scanning and checking location
function scanAndCheckLocation() {
// Check if geolocation is supported
if (navigator.geolocation) {
  // Get the current position
  navigator.geolocation.getCurrentPosition(
    (position) => {
      // Extract latitude and longitude from the position object
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;

      console.log("Latitude: " + latitude);
      console.log("Longitude: " + longitude);
      // Define the maximum range in meters
      const maxRange = 25; // Maximum range in meters

      // Find buildings within the specified range
      const buildingsInRange = findBuildingsWithinRange(latitude, longitude, maxRange);

      if (buildingsInRange.length > 0) {
        // Show the name of the nearest building
        const nearestBuilding = buildingsInRange[0];

        // Check if the building is the same as the last one
        if (checkQRCodeInCookies(nearestBuilding.name)) {
          // If the building has been scanned before, show a message
          alert("Nearest Building: " + nearestBuilding.name  + " has been scanned before. Please try again later.");
        } else {
          // Add 10 to cherry_num_value
          cherry_num_value += 10;
          // Add nearestBuilding.name to cookies
          document.cookie = nearestBuilding.name;

          // Update the cherry_num_element on the page
          cherry_num_element.textContent = cherry_num_value;

          // Show a success message
          alert("Nearest Building: " + nearestBuilding.name + "\n" + "Exeter Green POWER absorbed: 10");
        }
      } else {
        // If no buildings are within range, show a message
        alert("Your location is too far from any building.");
      }
    },
    (error) => {
      // Handle any errors that may occur
      console.error("Error getting location:", error.message);
    }
  );
} else {
  // Geolocation is not supported by the browser
  console.error("Geolocation is not supported by your browser.");
}
}


// Function to check if building exists in cookies
function checkQRCodeInCookies(buildingName) {
var cookies = document.cookie.split(';');
for (var i = 0; i < cookies.length; i++) {
  var cookie = cookies[i].trim();
  if (cookie.indexOf(buildingName) === 0) {
    return true; // buildingName found in cookies
  }
}
return false; // buildingName not found in cookies
}

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