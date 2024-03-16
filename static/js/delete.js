console.log("delete.js loaded");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let productId = e.target.dataset.productId;
        deleteConfirm.href = `/product/delete/${productId}/`;
        deleteModal.show();
    });
}
