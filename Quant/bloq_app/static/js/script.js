var blockWidthDim = document.getElementById("block-width-dim")
var blockHeightDim = document.getElementById("block-height-dim")
var blockLengthDim = document.getElementById("block-length-dim")

var blockWidthInput = document.getElementById("block-width")
var blockHeightInput = document.getElementById("block-height")
var blockLengthInput = document.getElementById("block-length")

var doorWidthDim = document.getElementById("door-width-dim")
var doorHeightDim = document.getElementById("door-height-dim")

var doorWidthInput = document.getElementById("door-width")
var doorHeightInput = document.getElementById("door-height")

var windowWidthDim = document.getElementById("window-width-dim")
var windowHeightDim = document.getElementById("window-height-dim")

var windowWidthInput = document.getElementById("window-width")
var windowHeightInput = document.getElementById("window-height")

var unitData = document.getElementById('unit-data');
var currentUnit = unitData.getAttribute('data-unit');

// Add event listeners for input changes
if (blockWidthInput){
    blockWidthInput.addEventListener('input', function() {
        updateDimension(blockWidthInput.value, blockWidthDim, currentUnit);
    });
}

if (blockHeightInput){
    blockHeightInput.addEventListener('input', function() {
        updateDimension(blockHeightInput.value, blockHeightDim, currentUnit);
    });
}

if (blockLengthInput){
    blockLengthInput.addEventListener('input', function() {
        updateDimension(blockLengthInput.value, blockLengthDim, currentUnit);
    });
}

if (doorWidthInput){
    doorWidthInput.addEventListener('input', function() {
        updateDimension(doorWidthInput.value, doorWidthDim, currentUnit);
    });
}

if (doorHeightInput){
    doorHeightInput.addEventListener('input', function() {
        updateDimension(doorHeightInput.value, doorHeightDim, currentUnit);
    });
}

if (windowWidthInput){
    windowWidthInput.addEventListener('input', function() {
        updateDimension(windowWidthInput.value, windowWidthDim, currentUnit);
    });
}

if (windowHeightInput){
    windowHeightInput.addEventListener('input', function() {
        updateDimension(windowHeightInput.value, windowHeightDim, currentUnit);
    });
}

// Function to update dimensions
function updateDimension(value, dimElement, unit) {
    dimElement.innerText = `${value} ${unit}`;
}

// Add element types
var addBlockBtn = document.getElementById('add-type-btn');
var blockTypesContainer = document.querySelector('.element-types');

var blockTypeCounter = 1;

addBlockBtn.addEventListener('click', function() {
    // Create a new label element
    var label = document.createElement('label');
    label.textContent = 'Type ' + blockTypeCounter;
    label.setAttribute('for', 'block-type-' + blockTypeCounter);
    label.setAttribute('id', 'block-type-label');
    label.setAttribute('class', 'tag-label');

    // Create the delete button span element
    var deleteBtn = document.createElement('span');
    deleteBtn.className = 'delete-btn';
    deleteBtn.textContent = 'x';

    // Append the delete button to the label
    label.appendChild(deleteBtn);

    // Append the label to the block types container
    blockTypesContainer.appendChild(label);

    // Increment the block type counter for the next block
    blockTypeCounter++;
});

// Remove element type
document.querySelector('.element-types').addEventListener('click', function(event) {
    if (event.target.classList.contains('delete-btn')) {
        event.target.closest('.tag-label').remove();
    }
})