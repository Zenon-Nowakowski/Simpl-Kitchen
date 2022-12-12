form = document.getElementById("updateForm");

// function updateRecipe(id, name, direction, url) {
//     fetch("/recipe/" + id, {
//         method: "PATCH",
//         body: JSON.stringify({
//             name,
//             direction,
//             url,
//         }),
//     }).then((response) => response.json());
//     window.location.reload();
// }
function updateRecipe(id, name, direction, picture) {
    fetch("/recipe/" + id, {
        method: "PATCH",
        body: JSON.stringify({
            name,
            picture,
            direction,
        }),
    }).then((response) => response.json());
    window.location.reload();
}

form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const di = document.getElementById("direction").value;
    const pi = document.getElementById("picture").value;
    const id = document.getElementById("id").value;


    updateRecipe(id, name, di, pi);
});


async function deleteRecipe(id) {
    const res = await fetch("/recipe/" + id, {
        method: "DELETE",
    }).then((response) => response.json());
    window.location.reload();
}
