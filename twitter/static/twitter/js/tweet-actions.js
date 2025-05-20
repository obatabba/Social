let csrf_token;

function like(tweet_id) {
    event.preventDefault()
    const url = `/tweet_like/${tweet_id}/`
    
    let like_button = `<i class="bi bi-hand-thumbs-up" style="float: right; margin: -3px 3px 0 0;"></i>`

    let unlike_button = `<i class="bi bi-hand-thumbs-up-fill" style="float: right; margin: -3px 3px 0 0;"></i>`

    $.ajax({
        type: 'POST',
        url: url,
        // data: {
        // },
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function (response) {
            if (response.action === 'like') {
                document.getElementById(`like-btn${tweet_id}`).innerHTML = unlike_button;
                document.getElementById(`likes-count${tweet_id}`).innerHTML = response.likes
            } else {
                document.getElementById(`like-btn${tweet_id}`).innerHTML = like_button;
                document.getElementById(`likes-count${tweet_id}`).innerHTML = response.likes
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


document.getElementById("confirmDeleteBtn").addEventListener("click", deleteTweet);

function showDeleteModal(tweetId) {
    currentTweetId = tweetId; // Store the ID for later use.
    document.getElementById("tweetDeleteModal").style.display = "block";
}

function deleteTweet() {

    const deleteUrl = `/delete_tweet/${currentTweetId}/`;

    $.ajax({
        type: 'DELETE',
        url: deleteUrl,
        headers: {
            'X-CSRFToken': csrf_token
        },
        success: function(response) {
            // Hide tweet delete modal
            document.getElementById("tweetDeleteModal").style.display = "none";

            // Add fade-out effect to the tweet
            $(`#tweet${currentTweetId}`).fadeOut(500, function() {
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

            currentTweetId = null;
        },
        error: function (xhr) {
            console.error('Failed to delete the tweet.');
        } 
    })
}

function showEditModal(tweetId) {

    // Display the modal
    document.getElementById("tweetEditModal").style.display = "block";
    document.getElementById("tweetEditModal").setAttribute('data-tweetId', tweetId);

    const tweetBody = document.getElementById(`tweetBody${tweetId}`).innerText;
    document.getElementById("tweetEditText").value = tweetBody;
}

document.getElementById('tweetEditForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    const form = document.getElementById('tweetEditForm');
    const formData = new FormData(form); // Create FormData object from form

    formData.append('csrfmiddlewaretoken', csrf_token);

    const tweetId = document.getElementById('tweetEditModal').getAttribute('data-tweetId');
    const url = `/edit_tweet/${tweetId}/`

    $.ajax({
        url: url,
        type: 'POST',
        data: formData,
        processData: false, // Prevent jQuery from processing the data
        contentType: false, // Prevent jQuery from setting a content type

        success: function (response) {
            document.getElementById("tweetEditModal").style.display = "none";
            document.getElementById(`tweetBody${tweetId}`).innerHTML = response['modified_tweet']
                            
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
