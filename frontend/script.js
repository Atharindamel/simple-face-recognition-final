const imageInput = document.getElementById('image-input');
const imagePreview = document.getElementById('preview-image');
const recongnizeButton = document.getElementById('recognize-button');

imageInput.addEventListener("change", function() {
    const file = imageInput.files[0];
    if (!file) {
        return;
    }

    const imageUrl = URL.createObjectURL(file);
    imagePreview.src = imageUrl;

})  

recongnizeButton.addEventListener("click", function() {
    console.log("Botón reconocer presionado")
});