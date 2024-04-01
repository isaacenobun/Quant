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

// Delete element types
var deleteBtns = document.querySelectorAll('.delete-btn');

if (deleteBtns){
    for (let i = 0; i < deleteBtns.length; i++) {
        deleteBtns[i].addEventListener('click', function(event) {
            var label = event.target.closest('.tag-label');
            if (label) {
                label.remove();
            }
        });
    }
}

// Add element types
var addBlockBtn = document.getElementById('add-block-type-btn');
var TypesContainer = document.querySelector('.element-types');

var addDoorBtn = document.getElementById('add-door-type-btn');

var addWindowBtn = document.getElementById('add-window-type-btn');

var addOpeningBtn = document.getElementById('add-opening-type-btn');

if (addBlockBtn){
    addBlockBtn.addEventListener('click', function() {
        // Check if all required fields are filled
        var widthInput = document.getElementById('block-width');
        var heightInput = document.getElementById('block-height');
        var lengthInput = document.getElementById('block-length');
        var layerInput = document.getElementById('layer');
    
        if (widthInput.value && heightInput.value && lengthInput.value && layerInput.value) {
            // Create a new label element
            var label = document.createElement('label');
            label.textContent = 'Block type ' + blockTypeCounter;
            label.setAttribute('class', 'block-tag-label');
        
            // Create the delete button span element
            var deleteBtn = document.createElement('span');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'x';
        
            // Create the delete button link element
            var deleteLink = document.createElement('a');
            deleteLink.setAttribute('href', '{% url "delete-block-type" block.id %}');
        
            // Append the delete button to the link
            deleteLink.appendChild(deleteBtn);
        
            // Append the link to the label
            label.appendChild(deleteLink);
        
            // Append the label to the block types container
            TypesContainer.appendChild(label);
        
            // Increment the block type counter for the next block
            blockTypeCounter++;
        } else{
            // Alert the user to fill in all required fields
            alert('Please fill in all required fields before adding block types.');
        }
    });
}

if (addDoorBtn){
    addDoorBtn.addEventListener('click', function() {
        // Check if all required fields are filled
        var widthInput = document.getElementById('door-width');
        var heightInput = document.getElementById('door-height');
        var quantityInput = document.getElementById('door-quantity');
    
        if (widthInput.value && heightInput.value && quantityInput.value) {
            // Create a new label element
            var label = document.createElement('label');
            label.textContent = 'Door type ' + doorTypeCounter;
            label.setAttribute('class', 'door-tag-label');
        
            // Create the delete button span element
            var deleteBtn = document.createElement('span');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'x';
        
            // Create the delete button link element
            var deleteLink = document.createElement('a');
            deleteLink.setAttribute('href', '{% url "delete-door-type" door.id %}');
        
            // Append the delete button to the link
            deleteLink.appendChild(deleteBtn);
        
            // Append the link to the label
            label.appendChild(deleteLink);
        
            // Append the label to the block types container
            TypesContainer.appendChild(label);
        
            // Increment the block type counter for the next block
            doorTypeCounter++;
        } else{
            // Alert the user to fill in all required fields
            alert('Please fill in all required fields before adding door types.');
        }
    });
}

if (addWindowBtn){
    addWindowBtn.addEventListener('click', function() {
        // Check if all required fields are filled
        var widthInput = document.getElementById('window-width');
        var heightInput = document.getElementById('window-height');
        var quantityInput = document.getElementById('window-quantity');
    
        if (widthInput.value && heightInput.value && quantityInput.value) {
            // Create a new label element
            var label = document.createElement('label');
            label.textContent = 'Window type ' + windowTypeCounter;
            label.setAttribute('class', 'window-tag-label');
        
            // Create the delete button span element
            var deleteBtn = document.createElement('span');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'x';
        
            // Create the delete button link element
            var deleteLink = document.createElement('a');
            deleteLink.setAttribute('href', '{% url "delete-window-type" window.id %}');
        
            // Append the delete button to the link
            deleteLink.appendChild(deleteBtn);
        
            // Append the link to the label
            label.appendChild(deleteLink);
        
            // Append the label to the block types container
            TypesContainer.appendChild(label);
        
            // Increment the block type counter for the next block
            windowTypeCounter++;
        } else{
            // Alert the user to fill in all required fields
            alert('Please fill in all required fields before adding window types.');
        }
    });
}

if (addOpeningBtn){
    addOpeningBtn.addEventListener('click', function() {
        // Check if all required fields are filled
        var areaInput = document.getElementById('opening-area');
        var quantityInput = document.getElementById('opening-quantity');
    
        if (areaInput.value && quantityInput.value) {
            // Create a new label element
            var label = document.createElement('label');
            label.textContent = 'Opening type ' + openingTypeCounter;
            label.setAttribute('class', 'opening-tag-label');
        
            // Create the delete button span element
            var deleteBtn = document.createElement('span');
            deleteBtn.className = 'delete-btn';
            deleteBtn.textContent = 'x';
        
            // Create the delete button link element
            var deleteLink = document.createElement('a');
            deleteLink.setAttribute('href', '{% url "delete-opening-type" opening.id %}');
        
            // Append the delete button to the link
            deleteLink.appendChild(deleteBtn);
        
            // Append the link to the label
            label.appendChild(deleteLink);
        
            // Append the label to the block types container
            TypesContainer.appendChild(label);
        
            // Increment the block type counter for the next block
            openingTypeCounter++;
        } else{
            // Alert the user to fill in all required fields
            alert('Please fill in all required fields before adding opening types.');
        }
    });
}