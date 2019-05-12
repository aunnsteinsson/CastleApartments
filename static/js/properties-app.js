// Changes title to 'blah'
// $(document).ready(function() {
//     document.title = 'blah';
// });

// Creates the slider
$(document).ready(function () {
    $(".js-range-slider").ionRangeSlider({
        onChange: function (data) {
            // console.log(data.from); #TODO: TENGJA RETT
            // console.log(data.to);
            },
        type: "double",
        skin: "flat",
        min: 0,
        max: 1000,
    });
});
$(document).ready(function () {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/properties/search/?search-filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                var newHTML = resp.data.map(d => {
                    return `
                    <div class="col-md-3 well castles">
                        <a href="/properties/${d.id}">
                        <div class="card mb-4 box-shadow">
                            <img class="card-img-top"  alt="Thumbnail [100%x225]" src='${d.firstimage}'data-holder-rendered="true">
                            <div class="card-body">
                                <h1 class="card-text" id="castle-name"> ${d.name}</h1>
                                <p class="card-text"> ${d.info}</p>
                            </div>
                        </div>
                        </a>
                    </div>`
                });
                $('.castles').html(newHTML.join(''))
                $('#search-box').val('')
            },
            error: function (xhr, status, error) {
                //Todo: gæti þurft eitthvað annað error handling
                console.error(error);
            }
        })
    })

})