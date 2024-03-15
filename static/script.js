document.addEventListener("DOMContentLoaded", function () {
  var dropzone = document.getElementById("dropzone");

  dropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropzone.classList.remove("border-indigo-600");
    var file = e.dataTransfer.files[0];

    // Save the file to the input
    var input = document.getElementById("file");
    input.files = e.dataTransfer.files;

    displayPreview(file);
  });

  var input = document.getElementById("file");

  input.addEventListener("change", (e) => {
    var file = e.target.files[0];

    displayPreview(file);
  });

  function displayPreview(file) {
    if (file.type !== "image/png" && file.type !== "image/jpeg") {
      alert("Only PNG and JPEG files are allowed.");
      return;
    }

    var reader = new FileReader();

    reader.onload = () => {
      var preview = document.getElementById("preview");
      preview.src = reader.result;
      preview.classList.remove("hidden");

      // Display file name
      var fileNameDisplay = document.getElementById("file-name");
      fileNameDisplay.textContent = file.name;
    };

    reader.readAsDataURL(file);
  }

  document.querySelector("#scan").addEventListener("submit", (e) => {
    e.preventDefault();

    var fileInput = document.querySelector("input#file");

    if (fileInput.files.length > 0) {
      var file = fileInput.files[0];

      var reader = new FileReader();
      reader.onloadend = function () {
        var base64 = reader.result;

        fetch("/api/scan", {
          method: "POST",
          body: JSON.stringify({ image: base64 }),
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            let name = data.message.name;
            let description = data.message.description;

            let nameElem = document.getElementById("shark-name");
            let descElem = document.getElementById("shark-desc");
            let resultsElem = document.getElementById("results");

            resultsElem.classList.remove("hidden");

            nameElem.textContent = name;
            descElem.textContent = description;
          })
          .catch((error) => {
            console.error("Error:", error);
            alert("An error occurred while uploading the file.");
          });
      };
      reader.readAsDataURL(file); // Converts the file to Base64
    }
  });
});
