# pip install --upgrade pymupdf
import fitz
def main():
    file_path = "test.pdf"
    dpi = 300  # choose desired dpi here
    zoom = dpi / 72  # zoom factor, standard: 72 dpi
    magnify = fitz.Matrix(zoom, zoom)  # magnifies in x, resp. y direction
    doc = fitz.open(file_path)  # open document
    for page in doc[:2]:
        pix = page.get_pixmap(matrix=magnify)  # render page to an image
        pix.save(f"page-{page.number}.png")

if __name__ == "__main__":
    main()