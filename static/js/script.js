form = document.getElementById("updateForm");

function updateRecipe(id, name, direction, picture_url) {
    fetch("/recipe/" + id, {
        method: "PATCH",
        body: JSON.stringify({
            name,
            direction,
            picture_url,
        }),
    }).then((response) => response.json());
    window.location.reload();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const di = document.getElementById("direction").value;
    const url = document.getElementById("picture_url").value;
    const id = document.getElementById("id").value;


    updateRecipe(id, name, di, url);
});


async function deleteRecipe(id) {
    const res = await fetch("/recipe/" + id, {
        method: "DELETE",
    }).then((response) => response.json());
    window.location.reload();
}
