const dropZone = document.getElementById("dropZone");
const fileInput = document.getElementById("fileInput");
const fileList = document.getElementById("file-list");

dropZone.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropZone.classList.add("drag-over");
});

dropZone.addEventListener("dragleave", () => {
  dropZone.classList.remove("drag-over");
});

dropZone.addEventListener("drop", (event) => {
  event.preventDefault();
  dropZone.classList.remove("drag-over");
  const files = event.dataTransfer.files;
  handleFiles(files);
});

fileInput.addEventListener("change", (event) => {
  const files = event.target.files;
  handleFiles(files);
});

function handleFiles(files) {
  fileList.innerHTML = "";
  for (const file of files) {
    const fileEntry = document.createElement("div");
    fileEntry.classList.add("file-entry");
    fileEntry.textContent = `${file.name} (${formatBytes(file.size)})`;
    fileList.appendChild(fileEntry);
  }
}

function formatBytes(bytes, decimals = 2) {
  if (bytes === 0) return "0 Bytes";
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + " " + sizes[i];
}
