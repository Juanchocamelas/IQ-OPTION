
// Esperar que el DOM se cargue completamente
document.addEventListener('DOMContentLoaded', () => {
  const uploadBox = document.getElementById('uploadBox'); // Obtencion de la caja de subida
  const fileInput = document.getElementById('fileInput'); // Obtencion del input de subida de imagenes
  const clearButton = document.getElementById('clearBtn'); // Obtencion del boton de limpiar

// Limpiar el estado inicial de la caja de subida

  const setInitialState = () => {
    uploadBox.innerHTML = '';  // Limpiar el contenido de la caja de subida
    uploadBox.appendChild(fileInput); 
    const icon = document.createElement('img');
    icon.src = 'images/guardar.png';
    icon.alt = 'Cargar imagen';
    icon.className = 'upload-icon';
    uploadBox.appendChild(icon); // Estado inicial con el icono de carga
  };

  setInitialState(); 

  // Hacer que toda la caja sea clickeable para abrir el selector de archivos
  if (uploadBox) {
    uploadBox.addEventListener('click', () => {
      fileInput.click();
    });
  }

  // Mostrar vista previa de la imagen al seleccionar un archivo
  if (fileInput) {
    fileInput.addEventListener('change', () => {
      const file = fileInput.files[0];
      if (file) {
        const reader = new FileReader(); // Leer el archivo seleccionado
        reader.onload = (e) => { // luego de leerlo haz lo siguiente, e contiene la informacion del archivo leido
          uploadBox.innerHTML = `<img src="${e.target.result}" alt="Vista previa" class="image-preview">`;
        };
        reader.readAsDataURL(file);  // leer archivo como codigo para visualizarla en el navegador
      }
    });
  }

  // Funcionalidad del botón de limpiar
  if (clearButton) {
    clearButton.addEventListener('click', setInitialState);  // Al hacer clic en el botón de limpiar, restablece el estado inicial
  }
});