const userFolder = document.getElementById("user-folder");
const registerButton = document.getElementById("register-button");
const imageInput = document.getElementById("image-input");
const imagePreview = document.getElementById("preview-image");
const recongnizeButton = document.getElementById("recognize-button");

const personName = document.getElementById("person-name");
const scoreValue = document.getElementById("score-value");

let selectedFiles = [];
let selectedPersonName = "";

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

    if (result.personName === null) {
        personName.textContent = "Nombre: No reconocido";
    } else {    
        personName.textContent = 
            "Nombre: " + result.person_name;
    }

    scoreValue.textContent =
        "Score: " + result.score.toFixed(4);
});

userFolder.addEventListener("change", function () {
    selectedFiles = [...userFolder.files];

    if (selectedFiles.length === 0) {
        return;
    }

    selectedPersonName = selectedFiles[0].webkitRelativePath.split("/")[0];

    console.log("Persona:", selectedPersonName);
    console.log("Cantidad:", selectedFiles.length);
});

registerButton.addEventListener("click", async function () {

    if (selectedFiles.length === 0){
        console.log("No hay carpeta seleccionada");
        return;
    }

    const formData = new FormData();

    formData.append(
        "person_name",
        selectedPersonName
    );

    selectedFiles.forEach(file => {
        formData.append(
            "images",
            file
        );
    });
    
    const response = await fetch(
        "http://127.0.0.1:8000/add-person",
        {
            method: "POST",
            body: formData
        }
    );

    const result = await response.json();

    console.log(result);
    
});