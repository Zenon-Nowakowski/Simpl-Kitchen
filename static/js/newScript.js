form = document.getElementById("updateForm");

function updateRecipe(id, name) {
    fetch("/recipe/" + id, {
        method: "PATCH",
        body: JSON.stringify({
            name
        }),
    }).then((response) => response.json());
    window.location.reload();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const id = document.getElementById("id").value;

    updateMovie(id, name);
});

async function deleteRecipe(id) {
    const res = await fetch("/movie/" + id, {
        method: "DELETE",
    }).then((response) => response.json());
    window.location.reload();
}
