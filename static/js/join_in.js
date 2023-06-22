$('#join').on('click', function () {
    $.ajax({
        url: '/join_in',
        type: 'post',
        data: {
            'cno': $('#Cno').val(),
            'cname': $('#Cname').val(),
        },
        dataType: "json",
        success: function (res) {
            console.log(res)
        }
    })
})