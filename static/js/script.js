window.onload = function () {
    var task;

    function change() {
        let form = $('.change').children()[0];
        form.innerHTML += '<input name="id" value="' + $(task).attr('id') + '"><input type="hidden" name="col" value="' + $(task).parent().parent().attr('id') + '">';
        form.submit();
    }

    function del() {
        let form = $('.del').children()[0];
        form.innerHTML += '<input name="id" value="' + $(task).attr('id') + '">';
        form.submit();
    }


    $('.task').on('mouseover', function () {
        $(this).css({'box-shadow': '5px 5px 28px -6px white'})
    })

    $('.task').on('mouseout', function () {
        $(this).css({'box-shadow': '5px 5px 10px -6px white'})
    })

    $(function () {
        var isDragging = false;
        $('.task')
            .mousedown(function () {
                isDragging = false;
            })
            .mousemove(function () {
                isDragging = true;
            })
            .mouseup(function () {
                isDragging = false;
                task = $(this);
                setTimeout(change, 500);
            });

        $('.content').sortable({
            connectWith: '.content'
        }).disableSelection();

    });

    $('.delete-button').on('click', function () {
        setTimeout(del, 500);
    })

    $('.add-task-button').on('click', function () {
        let form = $(this).parent();
        form.submit();
    })

}