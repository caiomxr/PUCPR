document.addEventListener('DOMContentLoaded', function () {
    const celularElement = document.querySelector('.celular');
    const notificacoesToggle = document.getElementById('notificacoes-toggle');
    const temaToggle = document.getElementById('tema-toggle');

    notificacoesToggle.addEventListener('change', function () {
        if (this.checked) {
            
        } else {
            
        }
    });

    temaToggle.addEventListener('change', function () {
        celularElement.classList.toggle('tema-escuro-global');
    });
});