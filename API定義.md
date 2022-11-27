# API定義
## get
```
/get/user(使わないかも)
{
    user_id: ユーザーのID (str)
    name: ユーザーの名前 (str)
}

/get/allcal/{id}
{
    {
        cal_id: id(str) カレンダーのID
        date: 日付(datetime)
        text: 内容(str)
        url: 画像URL(str)
    },
    {
        ...
    }
} 
/get/{id}
{
    cal_id: id(str) カレンダーのID
    date: 日付(datetime)
    text: 内容(str)
    url: 画像URL(str)
}
```
## post
```
/post/user

requestbody
{
    userid: str
    username: str
}

responce
{
    userid: str
    username: str
}

/post/newplan

requestbody
{
    cal_id: str
    date: datetime
    text: str
    url: str
}

responce
{
    user_id = ユーザーのid(str),
    cal_id = UUID(str),
    date = datetime,
    text = 結果：str,
    url = 画像url:str,
}
```

## update
```
/calender/update/{id}
{
    'message':'sucess'
}
```

## update
```
/calender/delete/{id}
{
    'message':'sucess'
}
```