$(function() {
  $('.fa-columns').click(function() {
    $('#main-navbar').hide();
  });
  $('.fa-arrows-alt').click(function() {
    $('.navbar').toggle();
  });

  var $slider_container = $('.slider-container'),
      $slider = $('.slider');

  $slider.slick({
    appendArrows: $slider_container,
    // FontAwesomeのクラスを追加
    prevArrow: '<div class="slider-arrow slider-prev fa fa-angle-left"></div>',
    nextArrow: '<div class="slider-arrow slider-next fa fa-angle-right"></div>',
  });

  $('form').submit(function() {

    var url = 'https://slack.com/api/chat.postMessage',
        data = {
            token: 'xoxp-414368684705-414209150944-440338646112-8455f7bb849561f979ea400c136d4cdb',
            channel: '#23_shinjuku_manage',
            username: 'ぱいちんユーザからの問い合わせ',
            text: 'ぱいちんユーザから問い合わせがありました' + '\n'
              + '==============================================' + '\n'
              + '件名: ' + $('#contact-title').val() + '\n'
              + '連絡先: ' + $('#contact-mail').val() + '\n'
              + '内容: ' + $('#contact-body').val() + '\n'
              + '=============================================='
        };

    $.ajax({
        type: 'GET',
        url: url,
        data: data,
        });
    alert('お問い合わせありがとうございます。3日経っても返答がない場合は、お手数ですがもう一度お問い合わせください。');
  });
});
