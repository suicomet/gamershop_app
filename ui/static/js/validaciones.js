document.addEventListener('DOMContentLoaded', function () {
    console.log("Validaciones cargadas correctamente");

    const form = document.getElementById('formulario');

    form.addEventListener('submit', function (e) {
        let errores = [];

        const nombre = form.nombre.value.trim();
        const username = form.username.value.trim();
        const contra = form.contra.value;
        const recontra = form.recontra.value;
        const email = form.email.value.trim();
        const fecha = form['fecha-nacimiento'].value;

        // Validación nombre
        if (nombre.length < 3) {
            errores.push("El nombre debe tener al menos 3 caracteres.");
        }
        if (/\d/.test(nombre)) {
            errores.push("El nombre no debe contener números.");
        }

        // Validación usuario
        if (username.length < 4) {
            errores.push("El nombre de usuario debe tener al menos 4 caracteres.");
        }

        // Validaciones de contraseña
        if (contra.length < 6) {
            errores.push("La contraseña debe tener al menos 6 caracteres.");
        }
        if (contra.length > 15) {
            errores.push("La contraseña no debe tener más de 15 caracteres.");
        }
        if (!/[A-Za-z]/.test(contra)) {
            errores.push("La contraseña debe contener al menos una letra.");
        }
        if (!/\d/.test(contra)) {
            errores.push("La contraseña debe contener al menos un número.");
        }
        if (!/[!@#$%^&*(),.?":{}|<>]/.test(contra)) {
            errores.push("La contraseña debe contener al menos un carácter especial.");
        }

        if (contra !== recontra) {
            errores.push("Las contraseñas no coinciden.");
        }

        // Email básico
        if (!email.includes('@') || !email.includes('.')) {
            errores.push("El correo electrónico no es válido.");
        }

        // Fecha
        if (!fecha) {
            errores.push("Debes ingresar tu fecha de nacimiento.");
        }

        if (errores.length > 0) {
            e.preventDefault();
            alert(errores.join("\n"));
        }
    });
});
