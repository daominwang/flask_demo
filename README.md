请求方法 GET

请求参数

| 参数       | 说明                                            |
| ---------- | ----------------------------------------------- |
| team_name  | 球队名                                          |
| match_time | 比赛时间（为北京时间，格式如 2019-12-10 16:00） |


响应内容

| 参数 | 含义 |
| --- | --- |
| code | 状态码（200时返回的是data，内含球队数据；500时返回的是msg，描述系统异常的原因） |
| msg | 返回信息 |
| data | 返回数据 |

| 状态码值 | 状态码含义 |
| --- | --- |
| 200 | 成功 |
| 500 | 内部错误 | 
