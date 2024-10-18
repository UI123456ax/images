document.addEventListener('DOMContentLoaded', function() {
    const imageElement = document.getElementById('randomImage');
    const imagePath = 'ACG-img/img/';
    
    // 获取图片列表
    fetch('ACG-img/image-list.json')
        .then(response => response.json())
        .then(imageList => {
            // 随机选择一张图片
            const randomImage = imageList[Math.floor(Math.random() * imageList.length)];
            // 设置图片源
            imageElement.src = imagePath + randomImage;
        })
        .catch(error => console.error('Error:', error));
});
