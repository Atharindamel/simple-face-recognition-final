const imageInput = document.getElementById('image-input');
const imagePreview = document.getElementById('preview-image');
const recongnizeButton = document.getElementById('recognize-button');

const personName = document.getElementById("person-name");
const scoreValue = document.getElementById("score-value")

imageInput.addEventListener("change", function() {
    const file = imageInput.files[0];
    if (!file) {
        return;
    }

    const imageUrl = URL.createObjectURL(file);
    imagePreview.src = imageUrl;

})

recongnizeButton.addEventListener("click", async function() {
    const file = imageInput.files[0];

    if (!file) {
        console.log("No hay imagen seleccionada");
        return;
    }

    const formData = new FormData();
    formData.append("image", file);

    const response = await fetch(
        "http://127.0.0.1:8000/recognize",
        {
            method: "POST",
            body: formData
        }
    );

    const result = await response.json();

    personName.textContent = 
        "Nombre: " + result.person_name;

    scoreValue.textContent =
        "Score: " + result.score.toFixed(4);
});