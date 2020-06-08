## 商品相关的 api

### index

首页中用到的相关请求

#### goods/choices/

精选模块

```json
[
    {
        "image": String,
        "goods": [
            {
                "id": Number,
                "images": [
                    {
                        "image"
                    }
                ],
                "name": String,
                "short": String,
                "quantity": Number,
                "discount": Number,
                "price": Number,
            },
            {
                "id": Number,
                "image": String,
                "name": String,
                "short": String,
                "quantity": Number,
                "discount": Number,
                "price": Number,
            },
            {
                "id": Number,
                "image": String,
                "name": String,
                "short": String,
                "quantity": Number,
                "discount": Number,
                "price": Number,
            },
        ]
	},
]
```



#### slides/

轮播图

```json
[
    {
        "id": Number,
        "title": String,
        "image": String,
    }
]
```



slides/\<id:int\>/

某一轮播图活动对应的所有商品

```json
[
    {
        "id": Number,
        "image": String,
        "goods": [
            {
                "id": Number,
                "image": String,
                "name": String,
                "short": String,
                "quantity": Number,
                "discount": Number,
                "price": Number,
            }
        ]
    }
]
```



categories/

所有分类信息

```json
[
    {
        "id": Number,
        "name": String,
        "image": String
    }
]
```

