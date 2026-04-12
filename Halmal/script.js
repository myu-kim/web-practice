const topicForm = document.getElementById('topic-form');
const topicBar = document.getElementById('topic-bar');

const optionInst = document.querySelector('.option .instruction');
const option1Form = document.getElementById('option1-form');
const option1Bar = document.getElementById('option1-bar');
const option2Form = document.getElementById('option2-form');
const option2Bar = document.getElementById('option2-bar');

const rangeSection = document.querySelector('.range');
const rangeBar = document.querySelector('.range-bar');

const submitSection = document.querySelector('.submit');
const submitButton = document.querySelector('.submit-button');
const retryButton = document.querySelector('.retry-button');


function showElement(element) {
    element.classList.remove('hidden');
}

function hideElement(element) {
    element.classList.add('hidden');
}

function resetApp() {
    topicBar.value = '';
    option1Bar.value = '';
    option2Bar.value = '';
    rangeBar.value = '5';

    hideElement(optionInst);
    hideElement(option1Form);
    hideElement(option2Form);
    hideElement(rangeSection);
    hideElement(submitSection);
    hideElement(retryButton);

    submitButton.textContent = '결과';
    submitButton.disabled = false;
    submitButton.classList.remove('is-loading');

    topicBar.focus();
}

function selectResult() {
    const option1Text = option1Bar.value.trim();
    const option2Text = option2Bar.value.trim();
    const weight = Number(rangeBar.value);
    let randomNumber = Math.floor(Math.random() * 11);

    while (randomNumber === weight) {
        randomNumber = Math.floor(Math.random() * 11);
    }

    return weight < randomNumber ? option1Text : option2Text;
}


topicForm.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!topicBar.value.trim()) {
        topicBar.focus();
        return;
    }

    showElement(optionInst);
    showElement(option1Form);
    option1Bar.focus();
});

option1Form.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!option1Bar.value.trim()) {
        option1Bar.focus();
        return;
    }

    showElement(option2Form);
    option2Bar.focus();
});

option2Form.addEventListener('submit', (event) => {
    event.preventDefault();

    if (!option2Bar.value.trim()) {
        option2Bar.focus();
        return;
    }

    showElement(rangeSection);
    showElement(submitSection);
});

submitButton.addEventListener('click', () => {
    if (!option1Bar.value.trim()) {
        showElement(optionInst);
        showElement(option1Form);
        option1Bar.focus();
        return;
    }

    if (!option2Bar.value.trim()) {
        showElement(option2Form);
        option2Bar.focus();
        return;
    }

    submitButton.disabled = true;
    submitButton.classList.add('is-loading');
    submitButton.textContent = '고민 중';

    window.setTimeout(() => {
        submitButton.classList.remove('is-loading');
        submitButton.textContent = selectResult();
        submitButton.disabled = false;
        showElement(retryButton);
    }, 1200);
});

retryButton.addEventListener('click', resetApp);