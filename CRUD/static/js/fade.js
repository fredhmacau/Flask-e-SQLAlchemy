var meta_cloak = $.meta('metro4:cloak').attr("content");
var meta_cloak_duration = $.meta('metro4:cloak_duration').attr("content");
if (window.METRO_CLOAK_REMOVE === undefined) {
    window.METRO_CLOAK_REMOVE = meta_cloak !== undefined ? (""+meta_cloak).toLowerCase() : "fade";
}
if (window.METRO_CLOAK_DURATION === undefined) {
    window.METRO_CLOAK_DURATION = meta_cloak_duration !== undefined ? parseInt(meta_cloak_duration) : 300;
}

if (window.METRO_CLOAK_REMOVE !== "fade") {
    $(".m4-cloak").removeClass("m4-cloak");
    $(window).fire("metro-initiated");
} else {
    $(".m4-cloak").animate({
        draw: {
            opacity: 1
        },
        dur: 300,
        onDone: function(){
            $(".m4-cloak").removeClass("m4-cloak");
            $(window).fire("metro-initiated");
        }
    });
}
