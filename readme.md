## Learning Resource
[學習面向對象的令狐衝](https://mp.weixin.qq.com/s?__biz=MzAxOTc0NzExNg==&mid=2665513353&idx=1&sn=a5dc69542fae6aabf0fef9b5f5881a9d&chksm=80d679cab7a1f0dc530bd1745c2c9552b739afc701ecb2f8e1eba8624d1fefc2c3cc64cd1d30&scene=21#wechat_redirect)

### Implemented API

[x] Init a employer

`employ_a = Employ(id=1, name='Ben')`

[x]Get employer type

`employ_a.get_type()`  
1. `sales`
2. `rd`
3. `pt`

[x] Get Payment method

`employ_a.payment_method()  => Payment_from_Post`

[x] Get receipt

`employ_a.receipt()` 

could return `Not sale type` if this employ is not a sale type
or `[{'20200309':34}, {'20200310':22}]`

[x] Get Payment schedule

`employ_a.payment_schedule()` => `bi-weekly`

[x] Get salary dispatch record

`employ_a.salary_dispatch_record()`

 could be... 

 `{'2020/05':15000}` for sales







