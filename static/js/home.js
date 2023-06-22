$('#exit_com').on('click', function () {
        $.ajax({
            url: '/exit_com',
            type: 'post',
            success: function (res) {
                console.log(res)
            }
        })
    })
