document.addEventListener("DOMContentLoaded", function() {
    const detailButtons = document.querySelectorAll('button');
    detailButtons.forEach(button => {
        button.addEventListener('click', () => {
            console.log('详情按钮被点击');
        });
    });
});
function toggleEvents(element) {
    // 找到点击的 h2 元素的下一个兄弟元素，即包含活动的 div
    var eventsDiv = element.nextElementSibling;
    // 切换显示状态
    if (eventsDiv.style.display === "none") {
        eventsDiv.style.display = "block";
    } else {
        eventsDiv.style.display = "none";
    }
}
