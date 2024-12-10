// Seleciona os passos e os botões
const steps = document.querySelectorAll('.form-step');
const nextButtons = document.querySelectorAll('.next');
const prevButtons = document.querySelectorAll('.prev');

// Índice do passo atual
let currentStep = 1;

// Função para mostrar o passo atual
function showStep(stepIndex) {
    steps.forEach((step, index) => {
        if (index === stepIndex) {
            step.classList.add('form-step-active');
        } else {
            step.classList.remove('form-step-active');
        }
    });
}

// Navegar para o próximo passo
nextButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();  
        if (currentStep < steps.length - 1) {
            currentStep++;
            showStep(currentStep);
            alert(currentStep)
        }
    });
});

// Navegar para o passo anterior
prevButtons.forEach(button => {
    button.addEventListener('click', (event) => {
        event.preventDefault();
        if (currentStep > 0) {
            currentStep--;
            showStep(currentStep);  
        }
    });
});

// Inicializa o formulário mostrando o primeiro passo
showStep(currentStep);
