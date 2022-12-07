form = document.getElementById("updateForm");

function updateRecipe(id, name, direction) {
    fetch("/recipe/" + id, {
        method: "PATCH",
        body: JSON.stringify({
            name,
            direction
        }),
    }).then((response) => response.json());
    window.location.reload();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const direction = document.getElementById("direction").value;
    const id = document.getElementById("id").value;


    updateRecipe(id, name, direction);
});

async function deleteRecipe(id) {
    const res = await fetch("/recipe/" + id, {
        method: "DELETE",
    }).then((response) => response.json());
    window.location.reload();
}
