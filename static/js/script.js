var currentTab = 0;
showTab(currentTab);

let nextSvgArrow = 'Avançar '

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
        document.getElementById('nextBtn').innerHTML = `Avançar  <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg"
        xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="30" height="30" fill="url(#pattern0_167_55)" />
        <defs>
            <pattern id="pattern0_167_55" patternContentUnits="objectBoundingBox" width="1" height="1">
                <use xlink:href="#image0_167_55" transform="scale(0.0111111)" />
            </pattern>
            <image id="image0_167_55" width="90" height="90"
                xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFLUlEQVR4nO2du2/cRRDHVzKPoCAoeUVyfLNHohQpCFSAjBDPAgHFb+eIjUJISAOSCVFw6OiAVMgS/4QLwkMCQgor+s2cDTKCJBQ0gYbwdLCpMJLtQ/O7I7zs04nb387+7vYjjXSyz+fdr9e7O7Oz8zMmkUgkEolEIpFIJBI9ks2OjDm+y2J+CByftI7fsUjnwfFF6/gXQPpdrHgtX0M6L+8B5DfkZ2oNulM+o9dfN1TYiYUd1jVfBEfvg6NfLXKrP6MVQH7PIk/Vs+ZtZpjZkTWvA+SnAemMdbTev7hb2ho4/thmNDl6YG6bGRb2ZHPXy0gDx5dKFHdTA+SfAPnVWrZ4oxlU9h1ZvLqOdByQLocW+L+C02VwfEzaZAaJOtK9FumCtsCbjPCv6q75gKk6MicC0lsWaUNb1K2taNuMfeSDa00V2YXzO8Hxgr6Q3Kvgn0HWtKZKyL+jn20ahxZ7pdbg+00VqDWaT1rHv+mLxv/LOg4RmpgB5CMl74lbQczROmT0nIkRcPyEOAfqIqFPsXNnYkLmNUBeVRcH/VoRU0F6yMRA7an5ejUXPu7RaMUigarIsveUbZG+GFy2Larus9vOiLoIrUA2o+lWR+zxsWejDZs1x4OKPD4+d5V1dE6/8xxa7AtBA1EShdPvNOtYg44GiycD0pJ6h1HHpO+iQelCW+Rp7c5abbEdHyv9+Mk6+iEOR4KnR7NPbhaT1yEdJnD8XanHYnLGpy2ybdv0v9tWw/zRoN6po4kShaYzEYjcklG8afscPxwscujow1JElmP7WIJGo1sIHVRsR+ulpDJI3oW2wPYvO9GtraGmEcD8Be9CS3JLBAK32h3kVRFTX2w65VflbHbEIi9rC2z/IbakheWPdR8cpU8jy17Tz9q5cPri2ghHNmT5Pm9Cg6PD2qLaWEe244MeheaT2oLaSMUGR695E9o6fldbTBur2I7e9ih0NUKioDBnA/Ln3oQGR9/4GnV1pOO7J87eYhTxKTYgf+2tYd7Coo5eNpEgTo8XoR3/7K1RnWhZ343arTyS/85YY/4mX9NVdELvatCtJhKkLTEKvVRWeFMLcPkr8U0dHhdDizytPbKjXQzT9o7DbO+Sw8JhHJbkgnMgFxzzQ54Ww9agBZXqSM94EzqFSbnLiG7e4U3oFPjnMIF/oXO3Wn2qsJEE/L0vhH8i14q1BbY9Oj7BDmcb/HxZLmtKN8ArQq91S3voi6JKgP5obg10Ao0gpRi0RbZb5HUETwnD5v5ykxyRvtcWGtoxkxMSdhWT14GTHC+VXvtjqJPQ8cof+iVTNnsnT2+X0OAQi7wUJBFdkERs7Q5bPZsyIS8LAfIXEXS6NdCXhYRalt+Trr8Foqjcoj7KOIiBozdD6brFFWVeHIIp49M92ZfXqAldiI0E7Yvp2mJwWbZ8e3Z2zMQAYH5flavO2G6OUSN/0MQEID0eS9DJ+rCikk4zMzEi5XEGotQPSplNOmxipij5U+FpBJBXoyvx0630T0UXyGVZb0yV2LmfRwF5PgLxWj3aonpJnz732TNxe5C0Ic6I+j7Zm7vuIrw14OhczTXvNoPEuFStadDRGEKsnTZMSZvMoLJ38vT2olA30rcKI/hHKdRtJxZuMMPC6IG5bVKKwSJ9VLKjsyYHqXLGN1Sl5zdDzv3kArvcrZanUfQ/cuUz6JTkXZSWElB5stkRyWezGT8Ljl6XbCDJQZZHgRQl4zuPB+mUj78o3yveU7yXDxa5cOnxIIlEIpFIJBKJRCJheuYPiEwcRMVIe48AAAAASUVORK5CYII=" />
        </defs>
    </svg>`
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

function changeStepIndicator(indexTab) {
    let steps = document.getElementsByClassName('step');
    console.log(steps)
    for (i = 0; i < steps.length; i++) {
        steps[i].className = steps[i].className.replace('step active', 'step');
    }
    steps[indexTab].className = 'step active';
}