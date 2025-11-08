const itemInput = document.getElementById('itemInput');
const addItemBtn = document.getElementById('addItemBtn');
const shoppingList = document.getElementById('shoppingList');

let items = []; // Array to store shopping list items

// Function to render the shopping list
function renderList() {
    shoppingList.innerHTML = ''; // Clear existing list
    items.forEach((item, index) => {
        const listItem = document.createElement('li');
        listItem.textContent = item;

        const deleteButton = document.createElement('button');
        deleteButton.textContent = 'Remove';
        deleteButton.onclick = () => removeItem(index); // Add click handler to remove item

        listItem.appendChild(deleteButton);
        shoppingList.appendChild(listItem);
    });
}

// Function to add an item
function addItem() {
    const newItem = itemInput.value.trim();
    if (newItem) {
        items.push(newItem);
        itemInput.value = ''; // Clear input field
        renderList();
    }
}

// Function to remove an item
function removeItem(index) {
    items.splice(index, 1); // Remove item at the given index
    renderList();
}

// Event listeners
addItemBtn.addEventListener('click', addItem);
itemInput.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        addItem();
    }
});

// Initial rendering of the list (in case of pre-defined items or loaded from storage)
renderList();