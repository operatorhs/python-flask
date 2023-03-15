
$(function() {
    $('#captcha-btn').on('click', function(event) {
        event.preventDefault()
        var email = $('input[name="email"]').val()
        zlajax.get({
            url: '/user/mail/captcha?email=' + email
        }).done(function (result) {
            console.log('验证码发送成功', result)
        }).fail(function (error) {
            console.log('获取失败了', error, error.message)
        })
    })
})
