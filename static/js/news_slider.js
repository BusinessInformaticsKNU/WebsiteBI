/**
 * Created by namik on 09.06.17.
 */
$(function () {
    var counter = 0;
    $hottest_news = $(".hotest-news");

    $(".arrow-left").bind("click", function () {
        changeHotNews("prev")
    });
    $(".arrow-right").bind("click", function () {
        changeHotNews("next")
    });

    function changeHotNews(whatToDo) {
        console.log("Hello");
        console.log("counter on the start " + counter);
        if (whatToDo == "next") {
            counter++;
        }
        else {
            counter--;
        }
        if (counter >= 3) {
            counter %= 3;
        }
        else if (counter < 0) {
            counter += 3;
        }
        console.log("counter on the finish " + counter);
        switch (counter) {
            case 0 :
                $hottest_news.attr({"src": "img/news/News_big_people.jpg", "class": "center-block hotest-news"});
                break;
            case 1:
                $hottest_news.attr({"src": "img/news/News_big_study.jpg", "class": "center-block hotest-news"});
                break;
            case 2:
                $hottest_news.attr({"src": "img/news/News_big_people.jpg", "class": "center-block hotest-news"});
                break;
        }
    }
});