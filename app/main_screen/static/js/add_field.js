document.getElementById('add-input-btn').addEventListener('click', addInputField);

function addInputField() {
    const elements = document.querySelectorAll('input[name="additional_input"]')
    if (elements.length <= 7){
        const container = document.getElementById('two-input-container');
        const input = document.createElement('input');
        input.type = 'text';
        input.name = 'additional_input';
        input.placeholder = 'Данные';
        input.classList.add('form-control');
        input.classList.add('w-100');
        input.classList.add('mt-2');
        input.classList.add('rounded'); 
    
        container.appendChild(input);
        console.log('Input field added');
        console.log(elements)
        window.scrollTo(0, document.body.scrollHeight)
    }
    else {
        alert('Достигнуто максимальное количество полей');
    }
}

document.addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        addInputField();
        console.log('Enter key pressed');
        // Дополнительные действия при нажатии Enter
    }
});