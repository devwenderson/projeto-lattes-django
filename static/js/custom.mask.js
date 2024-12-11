$(document).ready(function(){

    $('#tipoBuscaCnpj').click(() => {
        $('#instituicaoIdentificador').mask('00.000.000/0000-00', {reverse: true})
    })

    $('#tipoBuscaNome').click(() => {
        $('#instituicaoIdentificador').unmask();
        $('#instituicaoIdentificador').val('');
    })

    $('#cnpj').mask('00.000.000/0000-00', {reverse: true});
});