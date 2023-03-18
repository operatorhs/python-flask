$(function () {
    $('.active-btn').click(function (event) {
        event.preventDefault()
        var $this=$(this)
        var is_active = parseInt($this.attr('data-active'))
        var message = is_active ? '您确定要隐藏此帖子吗' : '您确定要显示此帖子吗'
        var post_id = $this.attr('data-post-id')
        var result = confirm(message)
        if (!result) {
            return
        }
        var data = {
            is_active: is_active ? 0 : 1
        }
        console.log(data)
        zlajax.post({
            url: '/cms/posts/active/' + post_id,
            data: data
        }).done(function () {
            window.location.reload()
        }).fail(function (error) {
            alert(error.message)
        })
    })
    $('.comments-btn').click(function(event) {
        var post_id = $(this).attr('data-post-id')
        window.location.href = '/cms/posts/comments/' + post_id
    })
})

