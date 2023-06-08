$('#btn-login').on('click', function () {
        $.ajax({
            url: '/log_in',
            type: 'post',
            data: { 'user': $('#user').val(), 'pwd': $('#pass').val() ,'status':$("input[name='status'][checked]").val()},
            dataType: "json",
            success: function (res) {
                console.log(res)
            }
        })
    })