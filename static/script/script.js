document.addEventListener("DOMContentLoaded", function () {
    const profiles = document.querySelectorAll('.profile');

    profiles.forEach(profile => {
        let isOriginalState = true;

        profile.addEventListener('click', function () {
            const image = profile.querySelector('img');
            const originalImageSrc = profile.getAttribute('data-original-src');
            const newImageSrc = profile.getAttribute('data-new-src');

            if (newImageSrc) {
                if (isOriginalState) {
                    image.src = newImageSrc;
                } else {
                    image.src = originalImageSrc;
                }

                isOriginalState = !isOriginalState;
            }
        });
    });
});
