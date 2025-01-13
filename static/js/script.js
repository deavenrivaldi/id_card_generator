function restrictNonLetters(event) {
  // remove any non-letter characters (incl numbers, punctuations, etc.)
  event.target.value = event.target.value.replace(/[^A-Za-z\s]/g, "");

  // remove leading space if it exists
  if (event.target.value.startsWith(" ")) {
    event.target.value = event.target.value.substring(1);
  }
}

//* NIK validation
function inputNIK(event) {
  // remove any non-numeric characters
  event.target.value = event.target.value.replace(/[^0-9]/g, "");

  // remove lieading zero if it exists
  if (event.target.value.startsWith("0")) {
    event.target.value = event.target.value.substring(1);
  }
}

function validateNIK(event) {
  const nikInput = document.getElementById("nik");
  const errorMessage = document.getElementById("nik-error");
  const submitButton = document.getElementById("generate_btn");

  //check if NIK is exactly 16-digits
  if (nikInput.value.length !== 16 || isNaN(nikInput.value)) {
    errorMessage.textContent = "NIK must be 16 digits long";
    nikInput.focus(); // bring focus back to the NIK field
    submitButton.disabled = true; // Disable the submit button
    if (event) event.preventDefault(); // Prevent form submission
  } else {
    errorMessage.textContent = ""; // clear error message if valid
    submitButton.disabled = false; // enable the submit button
  }
}

//* DOB validation

//? Set the maximum allowable date to today
document.addEventListener("DOMContentLoaded", () => {
  const dobInput = document.getElementById("dob");
  const today = new Date().toISOString().split("T")[0]; // Get today's date in YYYY-MM-DD format
  dobInput.setAttribute("max", today); // Set the max attribute to today's date
});

//? Optional: Validate DOB on form submission
function validateDOB(event) {
  const dobInput = document.getElementById("dob");
  const dobError = document.getElementById("dob-error");

  // Check if the selected date is valid
  if (new Date(dobInput.value) > new Date()) {
    dobError.textContent = "Date of Birth cannot be today or in the future.";
    dobInput.focus();
    event.preventDefault(); // Prevent form submission
  } else {
    dobError.textContent = ""; // Clear error message if valid
  }
}

//* RTRW validation
function inputRTRW(event) {
  let input = event.target; // The input field
  let value = input.value.replace(/[^0-9]/g, ""); // Allow only numbers

  // Limit to a maximum of 3 digits
  value = value.slice(0, 3);

  // Update the input value
  input.value = value;
}

function autoPadRTRW(event) {
  if (event.target.value === "") {
    //if the input is empty, default to '000'
    event.target.value = "000";
  } else {
    // pad value to 3 digits
    event.target.value = event.target.value.padStart(3, "0");
  }
}

//? Reset the value on focus to prepare for new input
function resetRTRW(event) {
  let input = event.target; // The input field
  let value = input.value;

  // Remove leading zeros for clean editing
  if (value === "000") {
    input.value = ""; // Clear the input if it was '000'
  } else {
    input.value = value.replace(/^0+/, ""); // Remove leading zeros
  }
}

//* Result Expand
document
  .getElementById("idCardForm")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    let formData = new FormData(this);

    // Make the AJAX request to the Flask backend
    fetch("/generate", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.image) {
          // Show the generated ID card in the expanded section
          document.getElementById("generatedCardSection").style.display =
            "block";
          document.getElementById("generatedCardImage").src =
            "data:image/jpeg;base64," + data.image;

          // Enable buttons
          document.getElementById("saveImageBtn").disabled = false;
          document.getElementById("generateNewCardBtn").disabled = false;
        }
        // hide the generate button upon submission
        document.getElementById("generate_btn").style.display = "none";
      })
      .catch((error) => console.error("Error generating ID card:", error));
  });

// Save image button
document.getElementById("saveImageBtn").addEventListener("click", function () {
  let link = document.createElement("a");
  link.href = document.getElementById("generatedCardImage").src;
  link.download = "id_card.jpg";
  link.click();
});

// Generate new image button
document
  .getElementById("generateNewCardBtn")
  .addEventListener("click", function () {
    // Hide the generated card and reset the form
    document.getElementById("generatedCardSection").style.display = "none";
    document.getElementById("idCardForm").reset();

    //show the generate id button
    document.getElementById("generate_btn").style.display = "block";
  });
