# Conversor a PDF (DOCX, JPG, PNG)

Una sencilla aplicación de escritorio que convierte archivos `.docx`, `.jpg`, `.jpeg` y `.png` a formato `.pdf` con un solo clic.

La aplicación detecta automáticamente el tipo de archivo y realiza la conversión, guardando el nuevo PDF en la **misma carpeta** que el archivo original.

---

##  Instalación

La forma más sencilla de usar la aplicación es descargar el ejecutable (`.exe`) para Windows.

1.  Ve a la sección de **[Releases](https://github.com/RafaBC-dev/ConversorPDF.git/Releases)** en este repositorio.
2.  Descarga el archivo `ConversorPDF.exe` de la última versión.
3.  Guarda el archivo donde quieras (ej. en tu Escritorio) y haz doble clic para ejecutarlo. No requiere instalación.

---

##  Directamente desde el código

Si prefieres ejecutar el script directamente desde el código fuente, necesitarás Python 3.

1.  **Clona el repositorio:**
    ```bash
    git clone https://github.com/RafaBC-dev/ConversorPDF.git
    cd tu-repositorio
    ```

2.  **Crea y activa un entorno virtual:** (Recomendado)
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ejecuta la aplicación:**
    ```bash
    python convertidor_a_pdf.py
    ```

---

## Librerías Utilizadas

* **[CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)** - Para la interfaz gráfica moderna.
* **[Pillow](https://python-pillow.org/)** - Para la conversión de imágenes.
* **[docx2pdf](https://github.com/AlJohri/docx2pdf)** - Para la conversión de documentos Word.