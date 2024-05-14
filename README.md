<h4>Description:</h4>
使用Django建置LINE機器人，可依據使用者欲搜尋的臺灣城市，從氣象局API撈出對應的天氣資訊，目前取得的天氣時間資料區間為當天的資料。
使用ngrok建立https伺服器。

`可搜尋的城市名單:`
`宜蘭縣,花蓮縣, 臺東縣, 澎湖縣, 金門縣, 連江縣, 臺北市, 新北市, 桃園市, 臺中市, 臺南市, 高雄市, 基隆市, 新竹縣, 新竹市, 苗栗縣, 彰化縣, 南投縣, 雲林縣, 嘉義縣, 嘉義市, 屏東縣`


<h4>Requirement:</h4>
<ol>
  <li>Django >= 5.0</li>
  <li>line-bot-sdk-python</li>
  <li>ngrok</li>
    因LINE Bot使用webhook url來做伺服器連結，必須是一個網站（不能是IP位置）和必須是https。而ngrok是一個代理伺服器，可以建立https伺服器
</ol>

<h4>機器人回覆:</h4>
![S__33816579](https://github.com/clingoram/mylinebot/assets/18278657/b6cfc302-6fac-46a6-925c-95fa8bc9c38f)
![crawler reply](https://github.com/clingoram/mylinebot/assets/18278657/460798fa-3c48-4561-a576-0d76afb0b695)
