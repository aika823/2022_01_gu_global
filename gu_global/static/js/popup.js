$(function() {
  // window.open('popup.html', 'windowPop', 'width=400, height=600, left=100, top=200, resizable = yes')

  // 쿠키 가져오기
  var getCookie = function(cname) {
      var name = cname + "=";
      var ca = document.cookie.split(';');
      for (var i = 0; i < ca.length; i++) {
          var c = ca[i];
          while (c.charAt(0) == ' ') c = c.substring(1);
          if (c.indexOf(name) != -1) return c.substring(name.length, c.length);
      }
      return "";
  }

  // 24시간 기준 쿠키 설정하기  
  var setCookie = function(cname, cvalue, exdays) {
      var todayDate = new Date();
      todayDate.setTime(todayDate.getTime() + (exdays * 24 * 60 * 60 * 1000));
      var expires = "expires=" + todayDate.toUTCString(); // UTC기준의 시간에 exdays인자로 받은 값에 의해서 cookie가 설정 됩니다.
      document.cookie = cname + "=" + cvalue + "; " + expires;
  }

  var couponClose = function() {
      if ($("input[name='chkbox']").is(":checked") == true) {
          setCookie("close", "Y", 1); //기간( ex. 1은 하루, 7은 일주일)
      }
      var box_length = $('.layerBox').length;
      console.log(box_length);

      if(box_length != 0) {
        $('.layerBox').last().detach()
      }
      $(this).parent('.layerBox').hide();
      // $(".pop").hide();
  }

  function count() {
      $('.number').each(function() {
          $(this)
              .prop('Counter', 0)
              .animate({
                  Counter: $(this).text(),
              }, {
                  duration: 4000,
                  easing: 'linear',
                  step: function(now) {
                      $(this).text(Math.ceil(now));
                  },
              });
      });
  }

  $(document).ready(function() {
      var cookiedata = document.cookie;
      if (cookiedata.indexOf("close=Y") < 0) {
          $(".pop").show();
      } else {
          $(".pop").hide();
      }
      $(".btnClose").click(function() {
          couponClose();
      });
  });

  var count_num = 0;

  var $wrap = $('.text-wrap');
  var $page = $('.page-start');
  var $window = $(window);
  var pageOffsetTop = $page.offset().top;
  var pageOffsetCount = $('.page-count').offset().top;

  $window.resize(function() {
      pageOffsetTop = $page.offset().top;
      pageOffsetCount = $('.page-count').offset().top;
  });

  $window.on('scroll', function() {
      var scrolled = $window.scrollTop() >= pageOffsetTop;
      $wrap.toggleClass('down', scrolled);

      var scrolled = $window.scrollTop() >= pageOffsetCount;
      if (scrolled) {
          if (count_num == 0) {
              count();
          }
          count_num = count_num + 1;
      }

  });


});