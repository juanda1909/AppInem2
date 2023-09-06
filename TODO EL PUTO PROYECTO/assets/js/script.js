(function ($) {
    "use strict";

    /*==================================================================
    [ Focus Contact2 ]*/
    $('.input100').each(function () {
        $(this).on('blur', function () {
            if ($(this).val().trim() != "") {
                $(this).addClass('has-val');
            } else {
                $(this).removeClass('has-val');
            }
        });
    });

    /*==================================================================
    [ Validación ]*/
    var loginForm = $('#loginForm'); // Selecciona el formulario de inicio de sesión

    loginForm.on('submit', function () {
        var check = true;
        var input = $(this).find('.input100'); // Busca los campos de entrada solo dentro del formulario de inicio de sesión

        input.each(function () {
            if (validate(this) == false) {
                showValidate(this);
                check = false;
            }
        });

        if (check) {
            // Si la validación es exitosa, puedes enviar el formulario aquí
            // loginForm.submit();
        } else {
            return false; // Evita el envío del formulario si la validación falla
        }
    });

    loginForm.find('.input100').each(function () {
        $(this).focus(function () {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zAZ]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
        return true; // Cambio: siempre retorna verdadero para permitir el envío del formulario
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
    }

    /* Funcionalidad para redirigir al usuario a la página de Registro */
    $('#registroButton').click(function (e) {
        e.preventDefault(); // Evita el envío del formulario
        window.location.href = $(this).attr('href'); // Redirige a registro.html
    });
})(jQuery);
