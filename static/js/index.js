$('.nav nav-sidebar').click(function ()  {

    if ($($(this))[0].href == String(window.location)) {

        $(this).addClass('active');
    }

});
