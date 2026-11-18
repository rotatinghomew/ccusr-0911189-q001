# errata · 办事资讯版本与渠道回执台账

使用 Python 3.11 标准库，不需要联网、第三方包或数据库。输入示例使用本地合成记录。

```sh
python3 -m errata shift data/sample.json
python3 -m unittest discover -s tests -v
```

输出为 UTF-8 JSON。输入文件不可读、业务引用无效或记录不符合口径时退出码为 2，同时报告原因。

## 记录口径

`versions` 的 `errors` 是该版本携带的错误编号，`clears` 是该修订明确澄清的错误编号；接触仅由 `touches` 记录。同一居民可多次领取不同版本；`person=null` 是匿名，`copies` 只表示份数。`tick` 是来源台账统一后的顺序点，同一时间以记录顺序为准。
`contacts` 的行是当前渠道许可，不是到达凭证；`notices` 按 `key` 标识工单，只有 `delivered` 是成功。`policy` 提供本轮名额和错误严重等级。当前反馈单按版本汇总、列出失败工单和可拨渠道。
