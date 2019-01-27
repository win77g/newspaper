$(document).ready(function () {
 console.log("hi");
     // вывод в модальное окно wishlist продукта
     $(document).on('click', "#news_category",function (e){
         e.preventDefault();
         var data = {};
         var news_slug = $(this).data("slug");

         console.log(news_slug);

//         var url = form.attr("action");


        var csrf_token = $('#news_modal [name="csrfmiddlewaretoken"]').val();
         console.log(csrf_token);
         data["csrfmiddlewaretoken"] = csrf_token;

         data.slug = news_slug;
         console.log(data.slug);

         $.ajax({
            url: '/slug/',
            type: 'POST',
            data: data,
            cache: true,
            success: function(data){
                console.log(data);
//                showWishlist(data);
              $('.list_news_top ').html(data);
            }
        });
//         $('#wishlist').modal();
//     function showWishlist(data) {
//            $('#wishlist .modal-body').html(data);
//            $('#wishlist').modal(data);
//        }
     });



});

