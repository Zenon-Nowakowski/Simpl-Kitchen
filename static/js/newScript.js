form = document.getElementById("updateForm");

function updateRecipe(id, name, instructions) {
    fetch("/recipe/" + id, {
        method: "PATCH",
        body: JSON.stringify({
            name,
            instructions
        }),
    }).then((response) => response.json());
    window.location.reload();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const instructions = document.getElementById("name").value;
    const id = document.getElementById("id").value;


    updateMovie(id, name, instructions);
});

async function deleteRecipe(id) {
    const res = await fetch("/movie/" + id, {
        method: "DELETE",
    }).then((response) => response.json());
    window.location.reload();
}
