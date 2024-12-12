$(document).ready(function(){

    $('#tipoBuscaCnpj').click(() => {
        $('#instituicaoIdentificador').mask('00.000.000/0000-00', {reverse: true})
    })

    $('#tipoBuscaNome').click(() => {
        $('#instituicaoIdentificador').unmask();
        $('#instituicaoIdentificador').val('');
    })

    $('#cnpj').mask('00.000.000/0000-00', {reverse: true});
    $('#cpf_socio').mask('000.000.000-00', {reverse: true});
    $('#cpf_representante').mask('000.000.000-00', {reverse: true});
    $('#cep').mask('00000-000', {reverse: true});
    $('#telefone1').mask('(00)00000-0000', {reverse: true});
    $('#telefone2').mask('(00)00000-0000', {reverse: true});
});