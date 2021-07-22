# 📝 2021/07/23


検索結果すら、自分のリテラシーが低いので細々とやってく


> ODataクエリによる検索(最新２０件取得)

```
GET　/text/all?$orderby=_created_at desc&$limit=20
```


半角スペースで死んでたので

`%20` でどうにか凌ぐ




```
url = 'https://versatileapi.herokuapp.com/api/text/all?$orderby=_created_at%20desc&$limit=20'
```
