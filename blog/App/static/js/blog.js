function getMoreInfo(p) {
    console.log("加载更多");
    $.ajax({
        type: 'GET',
        url: '/blog?page=' + p,
        dataType: 'json',
        jsonp: 'callback',
        async: true,
        success: function (res) {
            console.log(res);
        },
    })
}
