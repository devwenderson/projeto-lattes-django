var currentTab = 0;
showTab(currentTab);

function showTab(indexTab) {
    var tabs = document.getElementsByClassName('tab');
    tabs[indexTab].style.display = 'block';

    // Se estiver na primeira aba
    if (indexTab == 0) {
        document.getElementById('prevBtn').style.display = 'none';
    } else {
        document.getElementById('prevBtn').style.display = 'inline';
    }

    // Se não estiver na primeira aba
    if (indexTab == (tabs.length - 1)) {
        document.getElementById('nextBtn').innerHTML = 'Cadastrar'
    } else {
        document.getElementById('nextBtn').innerHTML = 'Avançar'
    }

    changeStepIndicator(indexTab);
}

function nextPrev(n) {
    // Todas as tabs 
    let tabs = document.getElementsByClassName('tab');
    // Caso algum campo seja inválido
    if (n == 1 && !validadeForm()) return false

    // Esconde a aba atual
    tabs[currentTab].style.display = 'none'

    // Aumenta ou diminui o current tab em 1
    currentTab = currentTab + n

    // Se chegar na última aba
    if (currentTab >= tabs.length) {
        document.getElementById('create-form').submit();
        return false;
    }
    showTab(currentTab);
};

function validadeForm() {
    let tabs = document.getElementsByClassName('tab');
    let inputs = tabs[currentTab].getElementsByTagName('input');
    let valid = true

    // Loop para verificar os inputs
    for (i = 0; i < inputs.length; i++) {
        // Se o campo estiver vazio
        if (inputs[i].value == '') {
            inputs[i].className = 'form-control invalid';
            valid = false
        }
    };
    return valid;
}

function changeStepIndicator (indexTab) {
    let steps = document.getElementsByClassName('step');
    console.log(steps)
    for (i = 0; i < steps.length; i++) {
        steps[i].className = steps[i].className.replace('step active', 'step'); 
    }
    steps[indexTab].className = 'step active';
}