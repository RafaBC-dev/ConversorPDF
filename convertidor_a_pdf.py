import customtkinter as ctk
import tkinter.filedialog as fd
from pathlib import Path
import sys

# --- Importar las librerías de conversión ---
# Trata de importar 'Pillow' y 'docx2pdf'. Si falla, muestra error y pide que las instales.
try:
    from PIL import Image
    from docx2pdf import convert
except ImportError as err:
    print(f"Error: Faltan librerías. {err}")
    print("Por favor, ejecuta en tu terminal:")
    print("pip install customtkinter Pillow docx2pdf")
    sys.exit(1)


# ===============================================
# === CONVERSIONES ===
# ===============================================

def convertir_imagen_a_pdf(ruta_entrada: Path):
    """Convierte un archivo de imagen (JPG, PNG) a PDF."""
    try:
        # Define la ruta de salida (mismo nombre, extensión .pdf)
        ruta_salida = ruta_entrada.with_suffix(".pdf")

        # Abre la imagen de entrada
        with Image.open(ruta_entrada) as img:

            # Convierte modos 'RGBA' o 'P' a 'RGB' para compatibilidad con PDF
            if img.mode == 'RGBA' or img.mode == 'P':
                img = img.convert('RGB')

            # Guarda la imagen convertida en la ruta de salida como PDF
            img.save(ruta_salida, "PDF", resolution=100.0)

        # Devuelve éxito (True) y el mensaje
        return True, f"Convertido con éxito a {ruta_salida.name}"

    except Exception as e:
        # Devuelve fallo (False) y el mensaje de error
        return False, f"Error al convertir imagen: {e}"


def convertir_docx_a_pdf(ruta_entrada: Path):
    """Convierte un archivo de docx a PDF."""
    try:
        # Define la ruta de salida
        ruta_salida = ruta_entrada.with_suffix(".pdf")

        # Llama a la función de la librería 'docx2pdf'
        convert(ruta_entrada, ruta_salida)

        # Devuelve éxito
        return True, f"Convertido con éxito a {ruta_salida.name}"

    except Exception as e:
        # Devuelve fallo
        return False, f"Error al convertir docx: {e}"


# ================================================
# === INTERFAZ ===
# ===============================================?

def seleccionar_y_convertir():
    """Función principal del botón: pide archivo, llama al backend y muestra resultado."""

    # Muestra el diálogo "Abrir Archivo" y guarda la ruta (string)
    ruta_archivo_str = fd.askopenfilename(
        title="Seleccionar el archivo para convertir a PDF",
        # Filtra los tipos de archivo mostrados en el diálogo
        filetypes=(("Documentos Word", "*.docx"),
                   ("Imágenes", "*.jpg *.jpeg *.png"),
                   ("Todos los archivos", "*.*"))
    )

    # Si el usuario cancela, 'ruta_archivo_str' estará vacío.
    if not ruta_archivo_str:
        label_feedback.configure(text="Operación cancelada.")
        return  # Detiene la función

    # Convierte el string de la ruta a un objeto Path
    ruta_path = Path(ruta_archivo_str)
    # Obtiene la extensión en minúsculas (ej: ".jpg") -> evitas errores
    extension = ruta_path.suffix.lower()

    # lógica ejecución según tipo archivo
    if extension == ".docx":
        # Llama al backend de DOCX
        exito, mensaje = convertir_docx_a_pdf(ruta_path)

    elif extension in [".jpg", ".jpeg", ".png"]:
        exito, mensaje = convertir_imagen_a_pdf(ruta_path)

    else:
        # Archivo no soportado
        exito, mensaje = False, "Error: Tipo de archivo no soportado."

    # Mostrar el resultado en la etiqueta con color
    if exito:
        label_feedback.configure(text=mensaje, text_color="green")
    else:
        label_feedback.configure(text=mensaje, text_color="red")


# ===============================================
# === CONFIGURACIÓN APLICACIÓN ===
# ===============================================

# 1. Configuración de apariencia (Modo Sistema, Tema Azul)
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# 2. Creación de la ventana principal
app = ctk.CTk()
app.title("Conversor a PDF")
app.geometry("500x300")  # Define el tamaño fijo: Ancho x Alto

# 3. Creación de un Frame (contenedor)
frame = ctk.CTkFrame(master=app)
# .pack() "dibuja" el frame y hace que ocupe todo el espacio
frame.pack(pady=20, padx=20, fill="both", expand=True)

# 4. Creación de Widgets (elementos)

# Etiqueta de instrucciones
label_info = ctk.CTkLabel(master=frame, text="Selecciona un archivo (DOCX, JPG, PNG)\npara convertir a PDF.",
                          font=("Arial", 14))
label_info.pack(pady=20)

# Botón que llama a la función 'seleccionar_y_convertir' al hacer clic
boton_abrir = ctk.CTkButton(master=frame, text="Seleccionar Archivo...", command=seleccionar_y_convertir)
boton_abrir.pack(pady=15)

# Etiqueta para mostrar mensajes de éxito/error
label_feedback = ctk.CTkLabel(master=frame, text="Esperando archivo...", font=("Arial", 12))
label_feedback.pack(pady=10)

# 5. Inicia el bucle de la aplicación (la mantiene abierta)
app.mainloop()