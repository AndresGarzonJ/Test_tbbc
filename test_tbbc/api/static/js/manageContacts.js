(function () {
    const btnDelete = document.querySelectorAll(".btnDelete");

    btnDelete.forEach((btn) => {
        btn.addEventListener("click", (e) => {
            const confirmation = confirm("Are you sure to delete the contact?");
            if (!confirmation) {
                e.preventDefault();
            }
        });
    });
})();
