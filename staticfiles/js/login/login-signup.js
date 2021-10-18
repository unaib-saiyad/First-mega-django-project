var windowWidth = $(window).width();

if (windowWidth < 601) {
    $("#container").removeClass("row");
    $("#container").removeClass("h-75");
    $("#container").removeClass("w-75");

    $("#container").addClass("col");
    $("#container").addClass("h-100");
    $("#container").addClass("w-100");

    $("#left").removeClass("col-4");
    $("#right").removeClass("col-8");

    $("#left").addClass("row");
    $("#right").addClass("row");
}

function lhstorhs() {
    if (windowWidth > 600) {
        $("#h2-left").addClass("d-none");
        $("#p-left").addClass("d-none");
        $("#btn-left").addClass("d-none");

        $("#h1-right").addClass("d-none");
        $("#user-right").addClass("d-none");
        $("#email-right").addClass("d-none");
        $("#password-right").addClass("d-none");
        $("#btn-right").addClass("d-none");

        $("#same-1").addClass("d-none");
        $("#same-2").addClass("d-none");

         document.getElementById("SignupUsername").required = false;
         document.getElementById("SignupEmail").required = false;
         document.getElementById("SignupPassword").required = false;
         document.getElementById("SigninEmail").required = true;
         document.getElementById("SigninPassword").required = true;

        $("#right").removeClass("backanimationfromright");
        $("#left").removeClass("backanimationfromleft");
        $("#right").addClass("animationfromright");
        $("#left").addClass("animationfromleft");
    }
    else {
        $("#right").removeClass("backanimationfrombottom");
        $("#left").removeClass("backanimationfromtop");
        $("#right").addClass("animationfrombottom");
        $("#left").addClass("animationfromtop");
    }

    setTimeout(function () {
        if (windowWidth <= 600) {
            $("#h2-left").addClass("d-none");
            $("#p-left").addClass("d-none");
            $("#btn-left").addClass("d-none");

            $("#h1-right").addClass("d-none");
            $("#user-right").addClass("d-none");
            $("#email-right").addClass("d-none");
            $("#password-right").addClass("d-none");
            $("#btn-right").addClass("d-none");

            $("#same-1").addClass("d-none");
            $("#same-2").addClass("d-none");
        }
        // The Code
        $("#h2-hidden-left").removeClass("d-none");
        $("#p-hidden-left").removeClass("d-none");
        $("#btn-hidden-left").removeClass("d-none");

        $("#h1-hidden-right").removeClass("d-none");
        $("#email-hidden-right").removeClass("d-none");
        $("#password-hidden-right").removeClass("d-none");
        $("#btn-hidden-right").removeClass("d-none");

        $("#same-1").removeClass("d-none");
        $("#same-2").removeClass("d-none");
        $("#anchor-tag").removeClass("d-none");
    }, 2000);
}


function rhstolhs() {
    if (windowWidth > 600) {
        $("#h2-hidden-left").addClass("d-none");
        $("#p-hidden-left").addClass("d-none");
        $("#btn-hidden-left").addClass("d-none");

        $("#h1-hidden-right").addClass("d-none");
        $("#email-hidden-right").addClass("d-none");
        $("#password-hidden-right").addClass("d-none");
        $("#btn-hidden-right").addClass("d-none");

        $("#same-1").addClass("d-none");
        $("#same-2").addClass("d-none");
        $("#anchor-tag").addClass("d-none");

        $("#right").removeClass("animationfromleft");
        $("#left").removeClass("animationfromright");

        $("#right").addClass("backanimationfromright");
        $("#left").addClass("backanimationfromleft");

        document.getElementById("SignupUsername").required = true;
        document.getElementById("SignupEmail").required = true;
        document.getElementById("SignupPassword").required = true;
        document.getElementById("SigninEmail").required = false;
        document.getElementById("SigninPassword").required = false;

    }
    else {
        $("#right").removeClass("animationfromtop");
        $("#left").removeClass("animationfrombottom");

        $("#right").addClass("backanimationfrombottom");
        $("#left").addClass("backanimationfromtop");
    }

    setTimeout(function () {
        if (windowWidth <= 600) {
            $("#h2-hidden-left").addClass("d-none");
            $("#p-hidden-left").addClass("d-none");
            $("#btn-hidden-left").addClass("d-none");

            $("#h1-hidden-right").addClass("d-none");
            $("#email-hidden-right").addClass("d-none");
            $("#password-hidden-right").addClass("d-none");
            $("#btn-hidden-right").addClass("d-none");

            $("#same-1").addClass("d-none");
            $("#same-2").addClass("d-none");
            $("#anchor-tag").addClass("d-none");
        }


        // The Code
        $("#h2-left").removeClass("d-none");
        $("#p-left").removeClass("d-none");
        $("#btn-left").removeClass("d-none");

        $("#h1-right").removeClass("d-none");
        $("#user-right").removeClass("d-none");
        $("#email-right").removeClass("d-none");
        $("#password-right").removeClass("d-none");
        $("#btn-right").removeClass("d-none");

        $("#same-1").removeClass("d-none");
        $("#same-2").removeClass("d-none");
    }, 2000);
}