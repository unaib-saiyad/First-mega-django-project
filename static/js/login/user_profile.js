$('#bio-details-edit-mode').ready(function () {
    fullname = document.getElementById("pre-fullname").innerHTML.replace(/\s+/g, ' ').trim();
    if (fullname === "") {
        BioMode();
    }
});

var upload_img_trigger = false;
let list_of_para = ['first', 'second', 'third', 'fourth', 'fifth'];
function BioMode() {
    if ($('#bio-details').hasClass('d-none')) {
        upload_img_trigger = false;
        let list_of_title_obj = [];
        let list_of_progress_obj = [];

        let username = document.getElementById("post-username").value;
        let fullname = document.getElementById("post-fullname").value;
        let email = document.getElementById("post-email").value;
        let mobile = document.getElementById("post-mobile").value;
        let address = document.getElementById("post-address").value;
        let tag = document.getElementById("post-tag").value;

        document.getElementById("post-username").required = false;
        document.getElementById("post-fullname").required = false;
        document.getElementById("post-email").required = false;
        document.getElementById("post-mobile").required = false;
        document.getElementById("post-address").required = false;

        let website = document.getElementById("website").value;
        let github = document.getElementById("github").value;
        let twitter = document.getElementById("twitter").value;
        let instagram = document.getElementById("instagram").value;
        let facebook = document.getElementById("facebook").value;

        for (var i = 0; i < 5; i++) {
            list_of_title_obj[i] = document.getElementById("post-" + list_of_para[i] + "-para-title").value;
            list_of_progress_obj[i] = document.getElementById("post-" + list_of_para[i] + "-para-progress").value;
        }

        for (var i = 0; i < 5; i++) {
            document.getElementById(list_of_para[i] + "-para-title").innerHTML = list_of_title_obj[i];
            $('#' + list_of_para[i] + '-para-progress').attr('aria-valuenow', list_of_progress_obj[i]).css('width', list_of_progress_obj[i] + '%');
        }


        document.getElementById("big-case-username").innerHTML = username;
        // document.getElementById("big-case-address").innerHTML = address;
        document.getElementById("pre-tag").innerHTML = tag;
        document.getElementById("pre-username").innerHTML = username;
        document.getElementById("pre-fullname").innerHTML = fullname;
        document.getElementById("pre-email").innerHTML = email;
        document.getElementById("pre-mobile").innerHTML = mobile;
        document.getElementById("pre-address").innerHTML = address;

        document.getElementById("pre-website-url").innerHTML = website;
        document.getElementById("pre-github-url").innerHTML = github;
        document.getElementById("pre-twitter-url").innerHTML = twitter;
        document.getElementById("pre-instagram-url").innerHTML = instagram;
        document.getElementById("pre-facebook-url").innerHTML = facebook;


        $('#bio-details').removeClass('d-none');
        $('#bio-details-edit-mode').addClass('d-none');
        $('#post-tag').addClass('d-none');
        $('#pre-tag').removeClass('d-none');
        $('#user-img').removeClass('hovor-effect');

        $('#hidden-progression').addClass('d-none');
        $('#progression').removeClass('d-none');
        $('#hidden-links').addClass('d-none');
        $('#links').removeClass('d-none');

        // $('#pre-website-url').removeClass('d-none');
        // $('#pre-github-url').removeClass('d-none');
        // $('#pre-twitter-url').removeClass('d-none');
        // $('#pre-instagram-url').removeClass('d-none');
        // $('#pre-facebook-url').removeClass('d-none');

        // $('#post-website-url').addClass('d-none');
        // $('#post-github-url').addClass('d-none');
        // $('#post-twitter-url').addClass('d-none');
        // $('#post-instagram-url').addClass('d-none');
        // $('#post-facebook-url').addClass('d-none');

    }
    else {
        upload_img_trigger = true;
        let list_of_title_obj = [];
        let list_of_progress_obj = [];

        let username = document.getElementById("pre-username").innerHTML.replace(/\s+/g, ' ').trim();
        let fullname = document.getElementById("pre-fullname").innerHTML.replace(/\s+/g, ' ').trim();
        let email = document.getElementById("pre-email").innerHTML.replace(/\s+/g, ' ').trim();
        let mobile = document.getElementById("pre-mobile").innerHTML.replace(/\s+/g, ' ').trim();
        let address = document.getElementById("pre-address").innerHTML.replace(/\s+/g, ' ').trim();
        let tag = document.getElementById("pre-tag").innerHTML.replace(/\s+/g, ' ').trim();

        let website = document.getElementById("pre-website-url").innerHTML.replace(/\s+/g, ' ').trim();
        let github = document.getElementById("pre-github-url").innerHTML.replace(/\s+/g, ' ').trim();
        let twitter = document.getElementById("pre-twitter-url").innerHTML.replace(/\s+/g, ' ').trim();
        let instagram = document.getElementById("pre-instagram-url").innerHTML.replace(/\s+/g, ' ').trim();
        let facebook = document.getElementById("pre-facebook-url").innerHTML.replace(/\s+/g, ' ').trim();

        for (var i = 0; i < 5; i++) {
            list_of_title_obj[i] = document.getElementById(list_of_para[i] + "-para-title").innerHTML;
            list_of_progress_obj[i] = document.getElementById(list_of_para[i] + "-para-progress").style.width;
        }
        for (var i = 0; i < 5; i++) {
            document.getElementById("post-" + list_of_para[i] + "-para-title").defaultValue = list_of_title_obj[i];
            document.getElementById("post-" + list_of_para[i] + "-para-progress").defaultValue = parseInt(list_of_progress_obj[i], 10);
        }

        $('#bio-details').addClass('d-none');
        $('#bio-details-edit-mode').removeClass('d-none');
        $('#pre-tag').addClass('d-none');
        $('#post-tag').removeClass('d-none');
        $('#user-img').addClass('hovor-effect');

        // $('#pre-website-url').addClass('d-none');
        // $('#pre-github-url').addClass('d-none');
        // $('#pre-twitter-url').addClass('d-none');
        // $('#pre-instagram-url').addClass('d-none');
        // $('#pre-facebook-url').addClass('d-none');

        // $('#post-website-url').removeClass('d-none');
        // $('#post-github-url').removeClass('d-none');
        // $('#post-twitter-url').removeClass('d-none');
        // $('#post-instagram-url').removeClass('d-none');
        // $('#post-facebook-url').removeClass('d-none');

        $('#progression').addClass('d-none');
        $('#hidden-progression').removeClass('d-none');
        $('#links').addClass('d-none');
        $('#hidden-links').removeClass('d-none');

        document.getElementById("big-case-username").innerHTML = username;
        // document.getElementById("big-case-address").innerHTML = address;
        document.getElementById("post-tag").defaultValue = tag;
        document.getElementById("post-username").defaultValue = username;
        document.getElementById("post-fullname").defaultValue = fullname;
        document.getElementById("post-email").defaultValue = email;
        document.getElementById("post-mobile").defaultValue = parseInt(mobile);
        document.getElementById("post-address").defaultValue = address;

        document.getElementById("post-username").required = true;
        document.getElementById("post-fullname").required = true;
        document.getElementById("post-email").required = true;
        document.getElementById("post-mobile").required = true;
        document.getElementById("post-address").required = true;

        document.getElementById("website").defaultValue = website;
        document.getElementById("github").defaultValue = github;
        document.getElementById("twitter").defaultValue = twitter;
        document.getElementById("instagram").defaultValue = instagram;
        document.getElementById("facebook").defaultValue = facebook;
        document.getElementById("website").required = false;
    }
}

window.element = document.getElementById('user-img');
element.addEventListener("click", () => {
    if (upload_img_trigger) {
        UplaodImg();
    }
});


function UplaodImg() {
    if ($('#add-file-div').hasClass('d-none')) {
        $('#add-file-div').removeClass('d-none');
        $('#main-page').addClass('d-none');
        $('#footer').addClass('d-none');
    }
    else {
        $('#add-file-div').addClass('d-none');
        $('#main-page').removeClass('d-none');
        $('#footer').removeClass('d-none');
    }
}


