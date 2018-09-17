<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js"></script>
<script src="https://raw.githubusercontent.com/tobia/Pause/master/jquery.pause.js"></script>
<script>
$(function(){
    var setElm = $('.loopSlider'),
    slideSpeed = 2000;

    setElm.each(function(){
        var self = $(this),
        selfWidth = self.innerWidth(),
        findUl = self.find('ul'),
        findLi = findUl.find('li'),
        listWidth = findLi.outerWidth(),
        listCount = findLi.length,
        loopWidth = listWidth * listCount;

        findUl.wrapAll('<div class="loopSliderWrap" />');
        var selfWrap = self.find('.loopSliderWrap');

        if(loopWidth > selfWidth){
            findUl.css({width:loopWidth}).clone().appendTo(selfWrap);

            selfWrap.css({width:loopWidth*2});

            function loopMove(){
                selfWrap.animate({left:'-' + (loopWidth) + 'px'},slideSpeed*listCount,'linear',function(){
                    selfWrap.css({left:'0'});
                    loopMove();
                });
            };
            loopMove();

            setElm.hover(function() {
                selfWrap.pause();
            }, function() {
                selfWrap.resume();
            });
        }
    });
});
</script>
