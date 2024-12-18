// Search Functionality
document.addEventListener("DOMContentLoaded", () => {
    const searchBox = document.getElementById("searchBox");
    const tableRows = document.querySelectorAll("tbody tr");

    searchBox.addEventListener("input", () => {
        const searchText = searchBox.value.toLowerCase();

        tableRows.forEach(row => {
            const name = row.children[0].textContent.toLowerCase();
            if (name.includes(searchText)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    });

    // Add an alert on image click
    const images = document.querySelectorAll("img");
    images.forEach(img => {
        img.addEventListener("click", () => {
            alert("You clicked on " + img.alt);
        });
    });
});
