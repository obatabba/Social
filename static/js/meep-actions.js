let csrf_token;

function like(meep_id) {
    event.preventDefault()
    const url = `/meep_like/${meep_id}/`
    
    let like_button = `<i class="bi bi-hand-thumbs-up" style="float: right; margin: -3px 3px 0 0;"></i>`

    let unlike_button = `<i class="bi bi-hand-thumbs-up-fill" style="float: right; margin: -3px 3px 0 0;"></i>`

    $.ajax({
        type: 'POST',
        url: url,
        data: {
                
        },    
        success: function (response) {
            if (response.action === 'like') {
                document.getElementById(`like-btn${meep_id}`).innerHTML = unlike_button;
                document.getElementById(`likes-count${meep_id}`).innerHTML = response.likes
            } else {
                document.getElementById(`like-btn${meep_id}`).innerHTML = like_button;
                document.getElementById(`likes-count${meep_id}`).innerHTML = response.likes
            }    
        },    
        error: function (xhr) {
            if (xhr.status === 403) {
                // Show the login modal when the user is not logged in
                document.getElementById("loginModal").style.display = "block";
            }   
        } 
    })
}


document.getElementById("confirmDeleteBtn").addEventListener("click", deleteMeep);

function showDeleteModal(meepId) {
    currentMeepId = meepId; // Store the ID for later use.
    document.getElementById("meepDeleteModal").style.display = "block";
}

function deleteMeep() {

    const deleteUrl = `/delete_meep/${currentMeepId}/`;

    $.ajax({
        type: 'DELETE',
        url: deleteUrl,
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function(response) {
            // Hide meep delete modal
            document.getElementById("meepDeleteModal").style.display = "none";

            // Add fade-out effect to the Meep
            $(`#meep${currentMeepId}`).fadeOut(500, function() {
                // Remove the element from DOM after the fade-out
                $(this).remove();
            });
            
            // Show success message dynamically
            const messageContainer = document.getElementById('message-container');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'alert alert-primary alert-dismissible fade show col-md-8 offset-md-2 mt-3';
            messageDiv.role = 'alert';
            messageDiv.innerHTML = `
                ${response.message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            `;

            messageContainer.appendChild(messageDiv);
            
            setTimeout(() => {
                const alert = document.querySelector('.alert');
                if (alert) {
                    $(alert).fadeOut(500, function() {
                        $(alert).remove();
                    });
                }
            }, 5000); // 5 seconds

            currentMeepId = null;
        },
        error: function (xhr) {
            console.error('Failed to delete the meep.');
        } 
    })
}

function showEditModal(meepId) {

    // Display the modal
    document.getElementById("meepEditModal").style.display = "block";
    document.getElementById("meepEditModal").setAttribute('data-meepId', meepId);

    const meepBody = document.getElementById(`meepBody${meepId}`).innerText;
    document.getElementById("meepEditText").value = meepBody;
}

document.getElementById('meepEditForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const form = document.getElementById('meepEditForm');
    const formData = new FormData(form); // Create FormData object from form

    formData.append('csrfmiddlewaretoken', csrf_token);

    const meepId = document.getElementById('meepEditModal').getAttribute('data-meepId');
    const url = `/edit_meep/${meepId}/`

    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false, // Prevent jQuery from processing the data
        contentType: false, // Prevent jQuery from setting a content type

        success: function (response) {
            document.getElementById("meepEditModal").style.display = "none";
            document.getElementById(`meepBody${meepId}`).innerHTML = response['modified_meep']
                            
            // Show success message dynamically
            const messageContainer = document.getElementById('message-container');
            const messageDiv = document.createElement('div');
            messageDiv.className = 'alert alert-primary alert-dismissible fade show col-md-8 offset-md-2 mt-3';
            messageDiv.role = 'alert';
            messageDiv.innerHTML = `
                ${response.message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            `;
                            
            setTimeout(() => {
                const alert = document.querySelector('.alert');
                if (alert) {
                    $(alert).fadeOut(500, function() {
                        $(alert).remove();
                    });
                }
            }, 5000); // 5 seconds

            messageContainer.appendChild(messageDiv);
        },
        error: function (xhr, status, error) {
            console.error(error);
        },
    });

})
