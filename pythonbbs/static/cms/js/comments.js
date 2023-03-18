$(function () {
    $('.active-btn').click(function (event) {
        event.preventDefault()
        var $this=$(this)
        var is_active = parseInt($this.attr('data-active'))
        var message = is_active ? '您确定要隐藏此评论吗' : '您确定要显示此评论吗'
        var comment_id = $this.attr('data-comment-id')
        var result = confirm(message)
        if (!result) {
            return
        }
        var data = {
            is_active: is_active ? 0 : 1
        }
        console.log(data)
        zlajax.post({
            url: '/cms/posts/comment/active/' + comment_id,
            data: data
        }).done(function () {
            window.location.reload()
        }).fail(function (error) {
            alert(error.message)
        })
    })
})

