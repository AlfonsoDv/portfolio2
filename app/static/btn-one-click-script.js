document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.contact-form');
    const sendButton = document.getElementById('sendButton');

    form.addEventListener('submit', function(e) {
        // Prevenir el envío del formulario por defecto
        e.preventDefault();

        // Deshabilitar el botón y cambiar el texto
        sendButton.disabled = true;
        sendButton.textContent = 'Enviando...';

        // Enviar el formulario
        this.submit();
    });
});