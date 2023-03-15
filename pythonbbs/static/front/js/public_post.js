$(function() {
    var E = window.wangEditor

    const editorConfig = { MENU_CONF: {} }
    editorConfig.MENU_CONF['uploadVideo'] = {
        server: '/upload/video',
        fieldName: 'file-video',
        timeout: 20 * 1000, // 5s
    }

    editorConfig.MENU_CONF['uploadImage'] = {
      server: '/upload/image',
      timeout: 5 * 1000, // 5s
      fieldName: 'file',
    }

    const editor = E.createEditor({
      selector: '#editor-text-area',
      html: '',
      config: editorConfig
    })

    const toolbar = E.createToolbar({
      editor,
      selector: '#editor-toolbar',
    })


    $('#submit-btn').click(function(event) {
        event.preventDefault()

        var title = $("input[name='title']").val()
        var board_id = $("select[name='board_id']").val()
        var content = editor.getHtml()

        console.log(editor,content )

        zlajax.post({
            url: '/post/public',
            data: {title, board_id, content}
        }).done(function () {
            setTimeout(function () {
                window.location = '/'
            }, 1000)
        }).fail(function(error) {
            alert(error.message)
        })
    })

})

