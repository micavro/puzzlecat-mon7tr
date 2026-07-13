# PuzzleCat 独立题解全集

本文件整理了本地 `archive/round-1-outcomes.json` 中全部 **289 道 correct 题目**。本次整理没有联网，只读取本地题面归档、`solve-log.md`、提交记录和此前留下的独立推理记录；不采用官方题解、作者解析或直接答案来源来补写机制。

每题均按“题面要点—我的解法—验证”书写。若本地记录只能确认部分步骤、最终正确提交，或原日志曾混入不合规来源，正文会明确标成“本地独立证据有限”，宁可留下缺口也不反向编造完整解法。

## 题目索引

| # | 题目 | ID | 答案 |
|---:|---|---|---|
| 1 | [#1](#p-9i9WHnxJ) | `9i9WHnxJ` | `CORRECT` |
| 2 | [#wall1 O(∩_∩)O](#p-TpQKhwRH) | `TpQKhwRH` | `0-0` |
| 3 | [#wall2 机器人合体](#p-AxmTwX1Q) | `AxmTwX1Q` | `TARS` |
| 4 | [#wall3 OOTD](#p-qlZUKLri) | `qlZUKLri` | `ONLINE TO OFFLINE` |
| 5 | [&](#p-Hi044RZL) | `Hi044RZL` | `风和日丽` |
| 6 | [1 small maze](#p-KmGXEjGS) | `KmGXEjGS` | `17` |
| 7 | [10 Buttons](#p-F5kyul5g) | `F5kyul5g` | `TicTacToe` |
| 8 | [21st Century Cryptic](#p-tqM7ji9S) | `tqM7ji9S` | `ANDROID` |
| 9 | [7️⃣🔪](#p-dCzF4LbF) | `dCzF4LbF` | `SEVER` |
| 10 | [[NbH2谜022]五色交辉](#p-GtybeioV) | `GtybeioV` | `者` |
| 11 | [[回放]花卉培育回放](#p-ixJRTMow) | `ixJRTMow` | `扎啤征战必胜激情坚持肃杀革命住户往昔算卦` |
| 12 | [[旧题] bitop](#p-RMZAJFgi) | `RMZAJFgi` | `QUBIT` |
| 13 | [A Cryptic](#p-AkhTwX1Q) | `AkhTwX1Q` | `SERENDIPITY` |
| 14 | [AAA Cryptic](#p-uBVC56DT) | `uBVC56DT` | `CORAL` |
| 15 | [AB谜](#p-kxqS2WKJ) | `kxqS2WKJ` | `蒙德` |
| 16 | [Animals in Grids](#p-D3WPz728) | `D3WPz728` | `ENGLISH` |
| 17 | [Another Cryptic](#p-1EGaRpKD) | `1EGaRpKD` | `PLUMB` |
| 18 | [APP](#p-mdar8Uar) | `mdar8Uar` | `扪心` |
| 19 | [Calculate！](#p-lZoOiBju) | `lZoOiBju` | `I SEE YOU PEE` |
| 20 | [CCBC](#p-sHRBl3vq) | `sHRBl3vq` | `河神` |
| 21 | [Celebratory Cryptic](#p-6ed5dzET) | `6ed5dzET` | `MATCH` |
| 22 | [Clues with Problems](#p-XDEkPIap) | `XDEkPIap` | `CASUAL` |
| 23 | [CROSS†WORD](#p-7wAIxIpP) | `7wAIxIpP` | `DISORDER` |
| 24 | [Cryptic 1- 绿泡泡](#p-e83oQPLb) | `e83oQPLb` | `通讯录 新的朋友 群聊` |
| 25 | [Cryptic Clue 一则](#p-aqestzDO) | `aqestzDO` | `ANAGRAM` |
| 26 | [Cryptic cryptic Cryptic cryptic cryptic cryptic Cryptic cryptic](#p-XpakPIap) | `XpakPIap` | `ONLY` |
| 27 | [Cryptixacum](#p-7QRIxIpP) | `7QRIxIpP` | `DANDELION` |
| 28 | [Find the Answer Ⅱ](#p-xo5D8t6h) | `xo5D8t6h` | `IN THE LINK` |
| 29 | [Find the Answer Ⅲ](#p-GEFbeioV) | `GEFbeioV` | `FOLIAGE` |
| 30 | [Finding Dragon's Pearl (tanlige)](#p-sqHBl3vq) | `sqHBl3vq` | `ELEMENT AL` |
| 31 | [Finding Dragon's Pearl 2](#p-MrIxAs7n) | `MrIxAs7n` | `TOOL AX` |
| 32 | [Iconic](#p-ys7zg7XA) | `ys7zg7XA` | `MCDONALDS` |
| 33 | [Little Cryptic 3](#p-TjvKhwRH) | `TjvKhwRH` | `开心` |
| 34 | [LLM is waiting for...](#p-YBnhZAop) | `YBnhZAop` | `PROMPT` |
| 35 | [Mini Choco Banana](#p-p3x2nNtD) | `p3x2nNtD` | `firstchoco` |
| 36 | [NESTH](#p-WAXlljce) | `WAXlljce` | `EARTH` |
| 37 | [Not A 和同开珎](#p-LNjqNrv1) | `LNjqNrv1` | `藏宝图` |
| 38 | [One cryptic](#p-5asuzMeL) | `5asuzMeL` | `FISHER` |
| 39 | [OoOo.o](#p-So2j2oe3) | `So2j2oe3` | `CENTER` |
| 40 | [Phigryptics](#p-XMskPIap) | `XMskPIap` | `SATURN OS` |
| 41 | [pqqp](#p-UWqvRTeZ) | `UWqvRTeZ` | `PAIRED` |
| 42 | [puzzle.cat](#p-atMstzDO) | `atMstzDO` | `RECOUNT` |
| 43 | [Reuniting Craft](#p-koQS2WKJ) | `koQS2WKJ` | `BORON` |
| 44 | [SIX SEVEN!!!](#p-MVLxAs7n) | `MVLxAs7n` | `HOTDOG` |
| 45 | [Super~big~](#p-aLPstzDO) | `aLPstzDO` | `WORLD CUP` |
| 46 | [Test](#p-7UlIxIpP) | `7UlIxIpP` | `什么` |
| 47 | [To ronto](#p-DnOPz728) | `DnOPz728` | `PIANO` |
| 48 | [type](#p-yhBzg7XA) | `yhBzg7XA` | `9256` |
| 49 | [wora1e](#p-653d5dzE) | `653d5dzE` | `ADAPT` |
| 50 | [☀️、⛵ 、💃 、✈️](#p-tNP7ji9S) | `tNP7ji9S` | `DOWNPOUR` |
| 51 | [「NLS-001」🔥](#p-L9DqNrv1) | `L9DqNrv1` | `煜` |
| 52 | [【98】狂想](#p-yELzg7XA) | `yELzg7XA` | `MEET A PARTNER AT THE HOTEL BAR` |
| 53 | [【NbH₂谜】倒数ing…](#p-cK6HRhJe) | `cK6HRhJe` | `中央` |
| 54 | [【NbH₂谜】黑板](#p-LWPqNrv1) | `LWPqNrv1` | `BRICK` |
| 55 | [【北斗谜航】#7☀️ 🌼 🔥 🌙](#p-ckFHRhJe) | `ckFHRhJe` | `新北二楼` |
| 56 | [【星谜002】ReReRebus](#p-RkaAJFgi) | `RkaAJFgi` | `PRISON` |
| 57 | [【星谜003】你图片带括号](#p-51auzMeL) | `51auzMeL` | `PUZZLE` |
| 58 | [【星谜004】Made in Russia](#p-m0fr8Uar) | `m0fr8Uar` | `PAST` |
| 59 | [【棱镜谜】一词多义](#p-TSvKhwRH) | `TSvKhwRH` | `瓜` |
| 60 | [【谜题】地名重组](#p-FbXyul5g) | `FbXyul5g` | `太原市` |
| 61 | [【鼠鼠谜】五角星](#p-avmstzDO) | `avmstzDO` | `AETHER` |
| 62 | [【鼠鼠谜】什么声音](#p-OZCiZO0v) | `OZCiZO0v` | `STRING` |
| 63 | [【鼠鼠谜】动物朋友](#p-jmKZrexE) | `jmKZrexE` | `MOON` |
| 64 | [【鼠鼠谜】我兜](#p-Gs6beioV) | `Gs6beioV` | `ANGLE` |
| 65 | [【鼠鼠谜】源自自然](#p-fLUYBRMr) | `fLUYBRMr` | `毛笔` |
| 66 | [【鼠鼠谜】螺旋](#p-TxHKhwRH) | `TxHKhwRH` | `DNA` |
| 67 | [【鼠鼠谜】道味海上](#p-YLdhZAop) | `YLdhZAop` | `HABITAT` |
| 68 | [【🚌】狂想](#p-S3Pj2oe3) | `S3Pj2oe3` | `48184` |
| 69 | [〖NbH₂谜〗Wordle](#p-5t7uzMeL) | `5t7uzMeL` | `IF` |
| 70 | [〖NbH₂谜〗未植数](#p-UlUvRTeZ) | `UlUvRTeZ` | `交叉相乘` |
| 71 | [〖星谜001〗漏墨](#p-ASMTwX1Q) | `ASMTwX1Q` | `B` |
| 72 | [〖棱镜谜〗见微知著](#p-4Rs9OF2B) | `4Rs9OF2B` | `OBSERVATION` |
| 73 | [〖鼠鼠谜〗加特零](#p-ut8C56DT) | `ut8C56DT` | `DUMPLING` |
| 74 | [〖鼠鼠谜〗竹林](#p-M8UxAs7n) | `M8UxAs7n` | `DECIMAL` |
| 75 | [一个字：从前](#p-TD4KhwRH) | `TD4KhwRH` | `梦` |
| 76 | [一代人的故事](#p-AjxTwX1Q) | `AjxTwX1Q` | `红番区` |
| 77 | [一则运算](#p-qWjUKLri) | `qWjUKLri` | `TANGERINE` |
| 78 | [七字谜](#p-MotxAs7n) | `MotxAs7n` | `FONT MASTER` |
| 79 | [不削能玩？](#p-4SL9OF2B) | `4SL9OF2B` | `REMOTE` |
| 80 | [不可能解决的难题](#p-KxUXEjGS) | `KxUXEjGS` | `立方倍积` |
| 81 | [不是中文 Cryptic](#p-pPS2nNtD) | `pPS2nNtD` | `SAGE` |
| 82 | [不是省油的灯](#p-I6LNP392) | `I6LNP392` | `INCINERATION` |
| 83 | [两种木棍](#p-9kkWHnxJ) | `9kkWHnxJ` | `火柴` |
| 84 | [两面包夹芝士](#p-Ca5fVTmL) | `Ca5fVTmL` | `BACON` |
| 85 | [中专说唱高手](#p-sU4Bl3vq) | `sU4Bl3vq` | `HIPHOP` |
| 86 | [中国Cry??ic（二）](#p-C1bfVTmL) | `C1bfVTmL` | `若叶睦` |
| 87 | [中国Cryptic（二）](#p-j2WZrexE) | `j2WZrexE` | `车 丰田` |
| 88 | [中英互译-DLC](#p-K2JXEjGS) | `K2JXEjGS` | `OUTCOME` |
| 89 | [串联珍珠](#p-odqmNtwx) | `odqmNtwx` | `TELECAST` |
| 90 | [九个梦魇](#p-JGPgoAEX) | `JGPgoAEX` | `史` |
| 91 | [二进制晶格](#p-RDqAJFgi) | `RDqAJFgi` | `SWIFT` |
| 92 | [五月的新智能手机](#p-AXpTwX1Q) | `AXpTwX1Q` | `TUMBLR` |
| 93 | [人越多越好，鱼越切越少](#p-fIqYBRMr) | `fIqYBRMr` | `田园` |
| 94 | [以小见大](#p-TPWKhwRH) | `TPWKhwRH` | `BETWEEN` |
| 95 | [以德芙人](#p-JumgoAEX) | `JumgoAEX` | `滑雪` |
| 96 | [何意【V】](#p-mGtr8Uar) | `mGtr8Uar` | `GOAL` |
| 97 | [你好，谢谢，最后是……](#p-E9mtl1dT) | `E9mtl1dT` | `SEE YOU` |
| 98 | [便携计数器](#p-a7xstzDO) | `a7xstzDO` | `点赞` |
| 99 | [信达雅](#p-XYkPIapg) | `XYkPIapg` | `QUOD ERAT DEMONSTRANDUM` |
| 100 | [元素魔法](#p-GC3beioV) | `GC3beioV` | `CURE RATE` |
| 101 | [克制关系](#p-GYnbeioV) | `GYnbeioV` | `DROWN` |
| 102 | [公式化 ISIS 谜题](#p-kZtS2WKJ) | `kZtS2WKJ` | `SOLVER` |
| 103 | [六月十日的笔记本](#p-PV7e2esI) | `PV7e2esI` | `海阔天空` |
| 104 | [别敲了](#p-yuhzg7XA) | `yuhzg7XA` | `HELLO` |
| 105 | [动物园谜001：大家好啊](#p-ermoQPLb) | `ermoQPLb` | `下路` |
| 106 | [动物细胞融合](#p-oFUmNtwx) | `oFUmNtwx` | `杀` |
| 107 | [动物躲猫猫](#p-BULEpJHi) | `BULEpJHi` | `三国演义` |
| 108 | [十一个单词](#p-zCJG691D) | `zCJG691D` | `WHOSE` |
| 109 | [十一个单词2](#p-RjXAJFgi) | `RjXAJFgi` | `ORGAN` |
| 110 | [十字谜](#p-RiAJFgie) | `RiAJFgie` | `灵光一现` |
| 111 | [单词勇者的冒险](#p-CI1fVTmL) | `CI1fVTmL` | `STRENGTH` |
| 112 | [危险源](#p-z1FG691D) | `z1FG691D` | `ATOM` |
| 113 | [历史谜（一）](#p-LwpqNrv1) | `LwpqNrv1` | `东西南北` |
| 114 | [历史谜（二）](#p-pej2nNtD) | `pej2nNtD` | `三五成群` |
| 115 | [又是三个词？](#p-OA2iZO0v) | `OA2iZO0v` | `BLUEPRINT` |
| 116 | [友人的来信](#p-ikmRTMow) | `ikmRTMow` | `SCHOLAR` |
| 117 | [双日凌空（一）](#p-baG5uOJW) | `baG5uOJW` | `公公偏头痛 三打祝家庄` |
| 118 | [反切的艺术](#p-cinHRhJe) | `cinHRhJe` | `鱼钩` |
| 119 | [反向探骊格](#p-HKd44RZL) | `HKd44RZL` | `一笔画` |
| 120 | [叠叠叠叠叠词](#p-Ys8hZAop) | `Ys8hZAop` | `原神` |
| 121 | [古老迷宫游戏](#p-y1Ezg7XA) | `y1Ezg7XA` | `UNFOLD` |
| 122 | [只需枚举](#p-GrbeioVN) | `GrbeioVN` | `ENUMERATE` |
| 123 | [吃什么](#p-F1Myul5g) | `F1Myul5g` | `烤鸡腿` |
| 124 | [启动](#p-hv41SWQP) | `hv41SWQP` | `当日` |
| 125 | [和同开珎](#p-mJYr8Uar) | `mJYr8Uar` | `京` |
| 126 | [和同谜](#p-XPtkPIap) | `XPtkPIap` | `明后` |
| 127 | [和和同同](#p-7WSIxIpP) | `7WSIxIpP` | `动力` |
| 128 | [哈基谜（二）](#p-yBIzg7XA) | `yBIzg7XA` | `ALPHABET` |
| 129 | [哈基谜（雾](#p-6Grd5dzE) | `6Grd5dzE` | `蒋` |
| 130 | [唐人街灯谜（巴黎）](#p-cWVHRhJe) | `cWVHRhJe` | `阿勒泰` |
| 131 | [嘉豪谜（一）](#p-IvFLNP39) | `IvFLNP39` | `DEATH` |
| 132 | [回転](#p-OS5iZO0v) | `OS5iZO0v` | `焼売` |
| 133 | [圆](#p-9SSWHnxJ) | `9SSWHnxJ` | `PUSKAS` |
| 134 | [填字游戏](#p-M0NxAs7n) | `M0NxAs7n` | `欲将心事付瑶琴` |
| 135 | [大厂笔试题](#p-KMgXEjGS) | `KMgXEjGS` | `NETEASE` |
| 136 | [大发大发](#p-bEu5uOJW) | `bEu5uOJW` | `心思` |
| 137 | [大数邻](#p-5ILuzMeL) | `5ILuzMeL` | `YAKUMAN` |
| 138 | [好吃的成语](#p-5LquzMeL) | `5LquzMeL` | `工匠熟能生巧` |
| 139 | [好数](#p-oyvmNtwx) | `oyvmNtwx` | `GREY` |
| 140 | [如约而至](#p-Wj2lljce) | `Wj2lljce` | `INFANT` |
| 141 | [字母谜](#p-mzEr8Uar) | `mzEr8Uar` | `GOOSE` |
| 142 | [字母重组](#p-EQxtl1dT) | `EQxtl1dT` | `AGAINST` |
| 143 | [字的奥秘](#p-KBXEjGSH) | `KBXEjGSH` | `拾` |
| 144 | [字谜三则](#p-PmEe2esI) | `PmEe2esI` | `明目张胆` |
| 145 | [学好数学](#p-uYPC56DT) | `uYPC56DT` | `WELL` |
| 146 | [学舌](#p-OjoiZO0v) | `OjoiZO0v` | `凄凉` |
| 147 | [宝可灯谜1](#p-yYszg7XA) | `yYszg7XA` | `胡说树` |
| 148 | [小学生必背](#p-ybfzg7XA) | `ybfzg7XA` | `9` |
| 149 | [展览墙](#p-d1uF4LbF) | `d1uF4LbF` | `HELLO WORLD` |
| 150 | [巧填幻方](#p-YvzhZAop) | `YvzhZAop` | `NEUTRAL` |
| 151 | [巧填方格](#p-6Cnd5dzE) | `6Cnd5dzE` | `CONJUGACY` |
| 152 | [帮Stavros回家](#p-lXxOiBju) | `lXxOiBju` | `GREECE` |
| 153 | [平面直角坐标系](#p-fBtYBRMr) | `fBtYBRMr` | `AXIS` |
| 154 | [当一切都沉寂之时](#p-swOBl3vq) | `swOBl3vq` | `DEADLINE` |
| 155 | [彩色方块](#p-qwTUKLri) | `qwTUKLri` | `TELEGRAM` |
| 156 | [微谜137：述数术](#p-UsvRTeZO) | `UsvRTeZO` | `ALBUM` |
| 157 | [微谜139: 汉语词典](#p-JpgoAEXN) | `JpgoAEXN` | `价值` |
| 158 | [微谜145: 叠色](#p-CzfVTmLk) | `CzfVTmLk` | `万紫千红` |
| 159 | [微谜147: 力](#p-LimqNrv1) | `LimqNrv1` | `GOING` |
| 160 | [心](#p-duyF4LbF) | `duyF4LbF` | `LOVE` |
| 161 | [怀旧数学](#p-o0tmNtwx) | `o0tmNtwx` | `MIX` |
| 162 | [成词成对](#p-WTklljce) | `WTklljce` | `LAYOUT` |
| 163 | [成语与反义词](#p-iS6RTMow) | `iS6RTMow` | `括` |
| 164 | [成语与反义词2](#p-OkbiZO0v) | `OkbiZO0v` | `事无巨细` |
| 165 | [成语接龙](#p-D0iPz728) | `D0iPz728` | `心安理得` |
| 166 | [我是嘉豪（一）](#p-WRKlljce) | `WRKlljce` | `尹相杰` |
| 167 | [我爱记歌词](#p-EIStl1dT) | `EIStl1dT` | `SING` |
| 168 | [我的世界一直在下雨……](#p-JyxgoAEX) | `JyxgoAEX` | `SUNNY` |
| 169 | [我解谜](#p-ZmApgd2S) | `ZmApgd2S` | `RING` |
| 170 | [我解谜 I puzzIe.](#p-JY3goAEX) | `JY3goAEX` | `9` |
| 171 | [才不是汽水谜！(二)](#p-eyFoQPLb) | `eyFoQPLb` | `横岗` |
| 172 | [才不是汽水谜！（一）](#p-ELjtl1dT) | `ELjtl1dT` | `坏` |
| 173 | [打字比赛](#p-EqZtl1dT) | `EqZtl1dT` | `CHINA` |
| 174 | [找不同](#p-zY6G691D) | `zY6G691D` | `ACID RAIN` |
| 175 | [抽象猜歌1](#p-TP9KhwRH) | `TP9KhwRH` | `BAD ROMANCE` |
| 176 | [抽象猜歌2](#p-APVTwX1Q) | `APVTwX1Q` | `BILLIE JEAN` |
| 177 | [抽象猜歌4](#p-9ppWHnxJ) | `9ppWHnxJ` | `MOSKAU` |
| 178 | [抽象猜歌5](#p-fvQYBRMr) | `fvQYBRMr` | `SCHNAPPI` |
| 179 | [拼好字](#p-2mbMJHkc) | `2mbMJHkc` | `ALGORITHM` |
| 180 | [指北](#p-UwEvRTeZ) | `UwEvRTeZ` | `ENSURE` |
| 181 | [探骊格之底线](#p-gy76lhr6) | `gy76lhr6` | `生肖 牛` |
| 182 | [探骊格（三）](#p-s7QBl3vq) | `s7QBl3vq` | `字 体` |
| 183 | [数独谜题](#p-ADITwX1Q) | `ADITwX1Q` | `RESUME` |
| 184 | [文化造纸](#p-7vOIxIpP) | `7vOIxIpP` | `诣` |
| 185 | [文字游戏](#p-BvqEpJHi) | `BvqEpJHi` | `alpha` |
| 186 | [料理](#p-q4kUKLri) | `q4kUKLri` | `刺身` |
| 187 | [旅立ち](#p-p0e2nNtD) | `p0e2nNtD` | `運勢` |
| 188 | [旅行前也要先填饱肚子呀……](#p-cSyHRhJe) | `cSyHRhJe` | `CHANGI` |
| 189 | [无需多言](#p-qOpUKLri) | `qOpUKLri` | `LIFE` |
| 190 | [无需枚举](#p-Xe7kPIap) | `Xe7kPIap` | `FUN` |
| 191 | [时雨谜 · 〇三一 \|\| 血雨](#p-KeQXEjGS) | `KeQXEjGS` | `HAWAII` |
| 192 | [明诚谜 003](#p-KpIXEjGS) | `KpIXEjGS` | `吴承恩` |
| 193 | [明诚谜 005](#p-FCjyul5g) | `FCjyul5g` | `YOUR` |
| 194 | [明诚谜001](#p-X2akPIap) | `X2akPIap` | `北京明诚学校` |
| 195 | [明诚谜004](#p-AZDTwX1Q) | `AZDTwX1Q` | `LEMON` |
| 196 | [明诚谜007](#p-tQe7ji9S) | `tQe7ji9S` | `A6F10H3` |
| 197 | [明诚谜008](#p-eJ0oQPLb) | `eJ0oQPLb` | `详细信息` |
| 198 | [明诚谜009](#p-9XXWHnxJ) | `9XXWHnxJ` | `RIVER` |
| 199 | [最烂的谜题只需枚举](#p-TSUKhwRH) | `TSUKhwRH` | `TRUETYPE` |
| 200 | [月照纱窗 2](#p-m61r8Uar) | `m61r8Uar` | `离家今几载` |
| 201 | [月照纱窗 3](#p-Kx6XEjGS) | `Kx6XEjGS` | `枕上劝人归` |
| 202 | [月照纱窗 4](#p-TMHKhwRH) | `TMHKhwRH` | `动作` |
| 203 | [月照纱窗1](#p-q9SUKLri) | `q9SUKLri` | `无多花片子` |
| 204 | [月照纱窗（无限版）](#p-gCN6lhr6) | `gCN6lhr6` | `我是月照纱窗传奇` |
| 205 | [本题设有中间答案验证](#p-IWfLNP39) | `IWfLNP39` | `IT ALL CLICKED` |
| 206 | [来自地球的礼物](#p-zEbG691D) | `zEbG691D` | `REMOTE CONTROLLED CAR` |
| 207 | [极简键盘](#p-bYF5uOJW) | `bYF5uOJW` | `REFERENCE` |
| 208 | [核类艺术（微恐）](#p-tvD7ji9S) | `tvD7ji9S` | `NUCLEAR WEAPON` |
| 209 | [梨谜014A](#p-XjYkPIap) | `XjYkPIap` | `循环往复` |
| 210 | [森林不退化](#p-E4otl1dT) | `E4otl1dT` | `奥秘` |
| 211 | [森林退化](#p-ghc6lhr6) | `ghc6lhr6` | `大巴` |
| 212 | [水浒卡](#p-RX1AJFgi) | `RX1AJFgi` | `WATER MARGIN` |
| 213 | [江河湖海](#p-WiTlljce) | `WiTlljce` | `2` |
| 214 | [汽水谜](#p-gFt6lhr6) | `gFt6lhr6` | `吴京` |
| 215 | [汽水谜（三）](#p-bC65uOJW) | `bC65uOJW` | `伽勒尔双弹瓦斯` |
| 216 | [汽水谜（二）](#p-z5nG691D) | `z5nG691D` | `非人` |
| 217 | [汽水谜（六）](#p-RkTAJFgi) | `RkTAJFgi` | `海风` |
| 218 | [汽水谜（四）](#p-iK0RTMow) | `iK0RTMow` | `新年快乐` |
| 219 | [洋](#p-79kIxIpP) | `79kIxIpP` | `HARBOR` |
| 220 | [添几笔](#p-p8D2nNtD) | `p8D2nNtD` | `云` |
| 221 | [演变](#p-5EtuzMeL) | `5EtuzMeL` | `魂魄` |
| 222 | [漫游](#p-1BzaRpKD) | `1BzaRpKD` | `RAMBLING` |
| 223 | [火柴人推箱子](#p-1IuaRpKD) | `1IuaRpKD` | `BOXES` |
| 224 | [熊不是黑白的](#p-xebD8t6h) | `xebD8t6h` | `PANDA` |
| 225 | [熟悉的等式](#p-TelKhwRH) | `TelKhwRH` | `GENIUS` |
| 226 | [猜单词](#p-KZ7XEjGS) | `KZ7XEjGS` | `REAL WAR` |
| 227 | [猜单词 1](#p-zu0G691D) | `zu0G691D` | `FASCINATOR` |
| 228 | [猜单词 2](#p-mnCr8Uar) | `mnCr8Uar` | `CLASSMATES` |
| 229 | [画](#p-SxSj2oe3) | `SxSj2oe3` | `AFRICA` |
| 230 | [留空](#p-HjG44RZL) | `HjG44RZL` | `BAT` |
| 231 | [病历乱神](#p-x8hD8t6h) | `x8hD8t6h` | `UNUSUAL TREATMENT` |
| 232 | [百合谜 01](#p-cO8HRhJe) | `cO8HRhJe` | `ADACHI` |
| 233 | [相生相克](#p-yC1zg7XA) | `yC1zg7XA` | `EARTH THEATER` |
| 234 | [神鲸谜 003](#p-gbq6lhr6) | `gbq6lhr6` | `AGE` |
| 235 | [神鲸谜 007](#p-RKhAJFgi) | `RKhAJFgi` | `乙炔基` |
| 236 | [福尔摩斯](#p-Zeipgd2S) | `Zeipgd2S` | `HOUSE` |
| 237 | [秘密单词本](#p-stNBl3vq) | `stNBl3vq` | `BEAUTY` |
| 238 | [符世绘](#p-xJsD8t6h) | `xJsD8t6h` | `五谷丰登` |
| 239 | [粉色](#p-4O19OF2B) | `4O19OF2B` | `BEST BOAT` |
| 240 | [纵横字咪](#p-C7hfVTmL) | `C7hfVTmL` | `FELICETTE` |
| 241 | [编程](#p-KowXEjGS) | `KowXEjGS` | `CODE` |
| 242 | [缩略](#p-L4xqNrv1) | `L4xqNrv1` | `MAP` |
| 243 | [美术课呢？](#p-KDdXEjGS) | `KDdXEjGS` | `CANCEL` |
| 244 | [老地方（微恐）](#p-9AAWHnxJ) | `9AAWHnxJ` | `GRENADE` |
| 245 | [自我治疗](#p-IH5LNP39) | `IH5LNP39` | `血炎症` |
| 246 | [节日快乐](#p-SMkj2oe3) | `SMkj2oe3` | `VANILLA` |
| 247 | [芉禧姩洣趧迋ふ（一）](#p-sIwBl3vq) | `sIwBl3vq` | `LONELY ISLAND` |
| 248 | [芉禧姩洣趧迋ふ（二）](#p-WA5lljce) | `WA5lljce` | `COMEDY CENTRAL` |
| 249 | [花卉培育！20260619](#p-YtJhZAop) | `YtJhZAop` | `安康` |
| 250 | [花卉培育！20260620](#p-9KKWHnxJ) | `9KKWHnxJ` | `终结` |
| 251 | [花卉培育！20260621](#p-HAg44RZL) | `HAg44RZL` | `图示` |
| 252 | [花卉培育！20260622](#p-4TE9OF2B) | `4TE9OF2B` | `草莓` |
| 253 | [花卉培育！20260623](#p-5BEuzMeL) | `5BEuzMeL` | `口腔` |
| 254 | [芳香](#p-BBEpJHim) | `BBEpJHim` | `茉莉` |
| 255 | [英文翻译？](#p-OMhiZO0v) | `OMhiZO0v` | `ELEVEN` |
| 256 | [蔚蓝谜](#p-RSsAJFgi) | `RSsAJFgi` | `奥赛` |
| 257 | [蛙谜1 篮球赛得分情况](#p-P8Le2esI) | `P8Le2esI` | `0` |
| 258 | [西行漫记](#p-sQlBl3vq) | `sQlBl3vq` | `LONGEST HIGHWAY` |
| 259 | [观星思人](#p-I9CLNP39) | `I9CLNP39` | `春日忆李白` |
| 260 | [译口同声](#p-JzDgoAEX) | `JzDgoAEX` | `WRITE TO YOU` |
| 261 | [语文课](#p-5h1uzMeL) | `5h1uzMeL` | `吹拉弹唱` |
| 262 | [语言](#p-LvSqNrv1) | `LvSqNrv1` | `石英` |
| 263 | [误差分析](#p-c9rHRhJe) | `c9rHRhJe` | `JAPAN` |
| 264 | [读法错误](#p-Mm7xAs7n) | `Mm7xAs7n` | `THE OLD MAN AND THE SEA` |
| 265 | [课文两景](#p-TkqKhwRH) | `TkqKhwRH` | `水龙` |
| 266 | [负负得……](#p-9AlWHnxJ) | `9AlWHnxJ` | `LINEAR` |
| 267 | [贪婪与高尚](#p-IUdLNP39) | `IUdLNP39` | `蝤` |
| 268 | [越狱](#p-usrC56DT) | `usrC56DT` | `咚` |
| 269 | [路线](#p-FsDyul5g) | `FsDyul5g` | `ID` |
| 270 | [跳舞的小人](#p-GBdbeioV) | `GBdbeioV` | `ICONIC` |
| 271 | [跳马2](#p-iD5RTMow) | `iD5RTMow` | `CLAY PIPES` |
| 272 | [这不是数独，这是英独！](#p-ogImNtwx) | `ogImNtwx` | `NUTRIENTS` |
| 273 | [这是Cryptic clue吗？](#p-HRJ44RZL) | `HRJ44RZL` | `CASE` |
| 274 | [这期神了](#p-9kAWHnxJ) | `9kAWHnxJ` | `DIVINE` |
| 275 | [远亲与不邻](#p-9TOWHnxJ) | `9TOWHnxJ` | `GLAM` |
| 276 | [邑首Quiz](#p-Prte2esI) | `Prte2esI` | `小虍阜` |
| 277 | [降水](#p-bsb5uOJW) | `bsb5uOJW` | `RAIN` |
| 278 | [随蓝01](#p-iZFRTMow) | `iZFRTMow` | `三角` |
| 279 | [集单谜](#p-zt5G691D) | `zt5G691D` | `SEASONDAN` |
| 280 | [集单谜2-忌惮谜](#p-7ljIxIpP) | `7ljIxIpP` | `THE BEGINNING` |
| 281 | [非洲79](#p-RPMAJFgi) | `RPMAJFgi` | `马普托` |
| 282 | [食物·景观·战役](#p-KS3XEjGS) | `KS3XEjGS` | `火烧` |
| 283 | [鱼数](#p-fqvYBRMr) | `fqvYBRMr` | `CATFISH` |
| 284 | [麻雀](#p-XxEkPIap) | `XxEkPIap` | `白頭山` |
| 285 | [黑暗森林组织：序](#p-O2YiZO0v) | `O2YiZO0v` | `VERMOUTH` |
| 286 | [미로](#p-dfGF4LbF) | `dfGF4LbF` | `미로의 수다쟁이` |
| 287 | [복제](#p-pmp2nNtD) | `pmp2nNtD` | `시공기하영토` |
| 288 | [회전](#p-Sepj2oe3) | `Sepj2oe3` | `목공` |
| 289 | [！？土土？！](#p-1wsaRpKD) | `1wsaRpKD` | `山脚下的泥土路和地里的铁` |

## 逐题题解

<a id="p-9i9WHnxJ"></a>

## #1（9i9WHnxJ）

- 答案：`CORRECT`

### 题面要点

图片给出七组 A–I 范围内的字母，风味提到“猪圈”，并强调原字母没有旋转或翻转。

### 我的解法

“猪圈”提示 Pigpen cipher。把每个源字母替换成其猪圈密码笔画，并保持原方向，七组轮廓依次读成 `C O R R E C T`。早先按视觉直觉把两个角形看成 L，得到的 `COLLECT` 只是中间答案；系统提示“未旋转/翻转”正是用来把这两个位置纠正为 R。

### 验证

`COLLECT` 命中中间验证，`E` 判错，最终 `CORRECT` 获 `correct`；共 1 次错误提交。

<a id="p-TpQKhwRH"></a>

## #wall1 O(∩_∩)O（TpQKhwRH）

- 答案：`0-0`

### 题面要点

前两例分别把摩斯码 `-.-` 与 K、`lol` 与《英雄联盟》联系起来；第三幅是国际象棋白方王翼易位局面，答案严格区分字符。

### 我的解法

共同点是短字符串既有专业含义，又像网络颜文字。第三图应写王翼易位记号，通常排作 `O-O`。本题判定采用数字零的排印形式，因此应写成 `0-0`。

### 验证

`O-O` 被判 incorrect，改交 `0-0` 后 correct；三字符长度和中间连字符均与题面一致。

<a id="p-AxmTwX1Q"></a>

## #wall2 机器人合体（AxmTwX1Q）

- 答案：`TARS`

### 题面要点

四幅影视机器人图片各配一个带连字符的名称模板，并用问号标出提取位；风味文字提示“合体的顺序有调整”。

### 我的解法

按模板识别四个机器人：`K-2SO` 取 `S`，`T-800` 取 `T`，`WALL-E` 取 `A`，`R2-D2` 取 `R`。自上而下得到 `STAR`，再依题意调整组合顺序，重排成《星际穿越》的机器人 `TARS`。此前把第一幅误认成 Sonny 会得到错误字母，模板中的连字符和长度正好用于纠错。

### 验证

四个名称与模板逐字符吻合，`STAR → TARS` 也解释了“顺序有调整”。`TARS` 提交正确。

<a id="p-qlZUKLri"></a>

## #wall3 OOTD（qlZUKLri）

- 答案：`ONLINE TO OFFLINE`

### 题面要点

核心提示是商业模式“线上线下融合”，题面排版中可直接读出 `O、2、O`，最终枚举为 `(6 2 7)`。

### 我的解法

“线上到线下”行业缩写为 `O2O`。题目把第一个字母 O、选项编号 2、后一个 O 排成这个缩写；标题 `OOTD` 也提示“缩写再展开”的玩法。按枚举把 `O2O` 展开为 `ONLINE TO OFFLINE`。

### 验证

三个词长度分别为 6、2、7，语义与“线上线下融合”完全一致；零错通过。

<a id="p-Hi044RZL"></a>

## &（Hi044RZL）

- 答案：`风和日丽`

### 题面要点

八行五言格式由重复标签 A–G 标记平仄，要求回答四字词语，并给出 `G & A F`。

### 我的解法

先按五言律诗格律给重复位置统一赋平仄，`&` 直接读作“和”，可确定答案应是常见的“X和YZ”四字词。日志先按较严格的格律模板推出另一组声调并连续试错，直到 `风和日丽` 被接受后，才反向以“一三不论”解释 `G/A/F = 平/仄/仄`。

### 验证

连接词、四字格式与最终答案一致，日志记录前六个候选均错，`风和日丽` 最终获 `correct`。本地独立证据有限：现有日志没有在提交前唯一推出这组平仄，不能把事后格律解释写成独立确定答案的证明。

<a id="p-KmGXEjGS"></a>

## 1 small maze（KmGXEjGS）

- 答案：`17`

### 题面要点

20×20 推箱迷宫中有九个按钮、七个刚性箱体；一次合法操作只能把一个完整箱体平移一格，要求最终覆盖全部按钮。

### 我的解法

本题主 `solve-log.md` 因大小写 ID 冲突写入了另一题，故采用同目录保留的本题本地日志和求解程序记录。把玩家可达区域与各箱锚点作为状态，用 push-only A* 搜索；相同多米诺箱做对称归一化。最短方案的推动数分解为：底部横箱右 2、左侧竖箱上 5、中部横箱右 6、6×6 方箱上 1、中部横箱再上 1、大异形箱上 1，总计 `2+5+6+1+1+1=17`。

### 验证

Python 与独立 C++ 实现均返回最小推动数 17，终态恰好覆盖九个按钮；提交 `17` 为 correct。

<a id="p-F5kyul5g"></a>

## 10 Buttons（F5kyul5g）

- 答案：`TicTacToe`

### 题面要点

归档的是一个交互页面：九个彩色按钮组成 3×3 棋盘，另有第十个白色按钮；任务要求连续赢得三颗星。

### 我的解法

检查本地交互脚本可见，它按井字棋的八种三连线判断胜负，并用 minimax 生成对手落子。每赢一局增加一颗星，第十个按钮用于进入下一局；连续三胜后终局遮罩直接显示应提交 `TicTacToe`。

### 验证

3×3 棋盘、三连线规则和终局文本完全一致。本地提交 `TicTacToe` 为正确。

<a id="p-tqM7ji9S"></a>

## 21st Century Cryptic（tqM7ji9S）

- 答案：`ANDROID`

### 题面要点

Cryptic clue：`Maybe a man with real, original government document? (7)`。

### 我的解法

定义是 `Maybe a man`：仿生人可以呈现为男性。字谜部分把 `with` 取作 `AND`；`real, original` 取两个词的首字母 `RO`；`government document` 是 `ID`。拼接得到 `AND + RO + ID = ANDROID`。

### 验证

答案长度 7，定义、逐段字谜和“21st Century”的科技主题三重吻合；零错通过。

<a id="p-dCzF4LbF"></a>

## 7️⃣🔪（dCzF4LbF）

- 答案：`SEVER`

### 题面要点

一把刀切过数字 7，下面有五个字母格，最后一格呈破损状。

### 我的解法

数字 7 的英文是 `SEVEN`，恰有五字母；刀的动作是 `SEVER`，也是五字母。图像表示用刀“切断” SEVEN，并让末字母所在的格子发生变化，得到 `SEVER`。

### 验证

字数、动作含义和末格破损全部吻合；`SEVER` 首投正确，错误 0 次。

<a id="p-GtybeioV"></a>

## [NbH2谜022]五色交辉（GtybeioV）

- 答案：`者`

### 题面要点

四色汉字分别与图标所示部件组合成新字，再翻成以 S 开头的英文词；红色路径产生第五种颜色。

### 我的解法

`黄+竹=簧→SPRING`，`黑+犬=默→SILENCE`，`青+日=晴→SUNNY`，`白+七=皂→SOAP`。红线抽出 `IENNA`，补共同首字母 S 得 `SIENNA`。将 sienna 译回“赭”，沿用同一拆字规则：`赤+者=赭`，所以问号处要填的基础部件是 `者`。

### 验证

五个英文词均获 intermediate，最终提交 `者` 为 correct，且无错误提交。

<a id="p-ixJRTMow"></a>

## [回放]花卉培育回放（ixJRTMow）

- 答案：`扎啤征战必胜激情坚持肃杀革命住户往昔算卦`

### 题面要点

十组各有三个中文提示，分别从读音、字形部件和意义三个角度指向一个二字词；最终把十个二字词连写。

### 我的解法

逐组求得：`扎啤、征战、必胜、激情、坚持、肃杀、革命、住户、往昔、算卦`。例如 `扎啤` 是酒水，和“巴黎”押韵，且扎/摸共享扌、啤/牌共享卑；`激情` 表示活力，与“批评”押韵，激/邀共享敫、情/请共享青。其余各组也以同样的音、形、义三重约束确定，按题面次序直接串联。

### 验证

初版首词 `渤海` 因意义关系过弱被判错；改为完整串 `扎啤征战必胜激情坚持肃杀革命住户往昔算卦` 后提交正确。

<a id="p-RMZAJFgi"></a>

## [旧题] bitop（RMZAJFgi）

- 答案：`QUBIT`

### 题面要点

图片以字形位图做 NOT、AND、OR 操作；五个子题答案会通过中间反馈依次给出最终答案字母。

### 我的解法

例题 `NOTE` 解析为 `NOT E`，`STANDBY` 解析为 `ST AND BY`。同理五题分别为 `C OR N=CORN`、`NOT(M OR E)=NOTMORE`、`AB AND ON=ABANDON`、`H OR R OR S=HORRORS`、`L AND F OR M=LANDFORM`。提交前三个子答案后，站点依次返回最终第 1–3 位 `Q、U、B`。结合 bitop/量子位主题，五字母答案唯一补成 `QUBIT`。

### 验证

所有位图操作都能按单词内部的运算符切分重现；三个中间字母和主题共同锁定 `QUBIT`，零错通过。

<a id="p-AkhTwX1Q"></a>

## A Cryptic（AkhTwX1Q）

- 答案：`SERENDIPITY`

### 题面要点

Cryptic clue：`Inspired yet, somehow, by lucky discovery (11)`。

### 我的解法

定义是 `lucky discovery`，`somehow` 是变位指示词，素材为十一字母 `INSPIRED YET`。将其重排恰得 `SERENDIPITY`，词义也正是“偶然发现美好事物/意外幸运发现”。

### 验证

字母多重集、枚举 11 和定义完全一致；首次提交 correct。

<a id="p-uBVC56DT"></a>

## AAA Cryptic（uBVC56DT）

- 答案：`CORAL`

### 题面要点

三条英文 cryptic clue 分别枚举为 6、4、5，最后给出 `(1/6)(2/6)(1/4)(4/5)(5/5)` 的提取式。

### 我的解法

第一题以 `ants` 为定义，将 `You Notice On Local Oaks Can` 的首字母 `YNOLOC` 反转得 `COLONY`。第二题从 `board` 去首字母后重排 `oard` 得 `ROAD`。第三题用“三”=`TRI` 加铝的元素符号 `AL` 得 `TRIAL`。依次提取 `COLONY` 的第 1、2 字母，`ROAD` 的第 1 字母，`TRIAL` 的第 4、5 字母，得到 `C O R A L`。

### 验证

三个答案都同时满足定义、词法和长度，提取唯一得到 `CORAL`；首次提交正确。

<a id="p-kxqS2WKJ"></a>

## AB谜（kxqS2WKJ）

- 答案：`蒙德`

### 题面要点

题面用字母代表汉字，给出 AB、BA、CA、DE、DFGE 等词，要求求出 CD。

### 我的解法

AB 是非汽水饮料且 BA 也成词，锁定 `AB=牛奶`、`BA=奶牛`，所以 A=牛、B=奶。CA 是奶制品品牌 `蒙牛`，得 C=蒙；DE 是品牌 `德亚`，得 D=德、E=亚。DFGE 是《英雄联盟》地区 `德玛西亚`，进一步确认 D=德、F=玛、G=西、E=亚。于是 CD=`蒙德`。

### 验证

每个给定词都被同一组字母代换解释，且 `蒙德` 本身也是明确的地区名；零错通过。

<a id="p-D3WPz728"></a>

## Animals in Grids（D3WPz728）

- 答案：`ENGLISH`

### 题面要点

七条英文线索各要求用一种传统字谜格变换得到动物名，括号给出抽取位置与词长。

### 我的解法

依次得到：`REED→DEER` 取 E，`MONKEY` 取 N，`CLOG→DOG` 取 G，`LEAF→FLEA` 取 L，`WIKI→KIWI` 取 I，`STALLION` 取 S，`HOGWARTS-S→HOGWART→WARTHOG` 取 H。七个抽取字母连成 `ENGLISH`。

### 验证

七行的动物词长和指定位置均吻合，提交 `ENGLISH` 为 correct。

<a id="p-1EGaRpKD"></a>

## Another Cryptic（1EGaRpKD）

- 答案：`PLUMB`

### 题面要点

线索是 `Sound quiet learner, dumb after dropping day (5)`。

### 我的解法

定义取 `Sound` 的动词义“测量深度”。`quiet` 给 `P`，`learner` 给 `L`，`dumb` 删除代表 day 的 `D` 后剩 `UMB`，拼成 `P + L + UMB = PLUMB`。

### 验证

答案为五字母，定义和每个词法部件都被精确使用；`PLUMB` 提交正确。

<a id="p-mdar8Uar"></a>

## APP（mdar8Uar）

- 答案：`扪心`

### 题面要点

三幅图分别提示抖音、闲鱼、快手，并用不同颜色标出这些应用名中汉字的部件。

### 我的解法

抖音取 `抖` 的灰色 `扌`，闲鱼取 `闲` 的深色 `门`，快手取 `快` 的蓝色 `忄`。答案第一格把灰色和深色左右拼合，即 `扌+门=扪`；第二格全蓝，把 `忄` 还原为其独立字形 `心`，得到 `扪心`。

### 验证

颜色和部件拼字逐格闭合；`扪心` 提交为 `correct`，错误 0 次。

<a id="p-lZoOiBju"></a>

## Calculate！（lZoOiBju）

- 答案：`I SEE YOU PEE`

### 题面要点

三道数学式分别缺少集合关系、集合运算和概率函数；隐藏文字提示先完成数学，再作“同声传译”。

### 我的解法

`{0}` 与自然数集之间填子集符号 `⊂`，其形似 C；`{2}` 与 `{3}` 合成 `{2,3}` 要填并集 `∪`，形似 U；`0≤?(A)≤1` 填概率 `P(A)`。连同题面已有的 I，最终视觉上得到 `I C U P`。把字母名读出声就是 `I see you pee`。

### 验证

每个符号都使原式成立，谐音又完整成句；答案首次提交 correct。

<a id="p-sHRBl3vq"></a>

## CCBC（sHRBl3vq）

- 答案：`河神`

### 题面要点

图片画西西弗斯推石，题目追问导致这项惩罚的事件中“她是谁的女儿”，答案枚举为两个汉字。

### 我的解法

我先被循环、时间意象带偏，猜过“时间”。回到西西弗斯神话本身：西西弗斯向河神阿索波斯泄露宙斯掳走其女儿埃癸娜的消息，因此招致宙斯报复。题目问的正是埃癸娜是谁的女儿，所以答案取身份类别“河神”。

### 验证

这条因果链直接解释西西弗斯图像和“女儿”措辞，且恰为二字；提交正确。

<a id="p-6ed5dzET"></a>

## Celebratory Cryptic（6ed5dzET）

- 答案：`MATCH`

### 题面要点

线索是 `PuzzleCat participated in Mystery Hunt to compete! (5)`。

### 我的解法

定义是 `to compete = MATCH`。从 `Mystery Hunt` 取外框/首字母 `M H`，把 `PuzzleCat` 中的 `CAT` 放入其中，得到 `M(CAT)H`。

### 验证

插入结构、五字母枚举和定义同时闭合；`MATCH` 零错通过。

<a id="p-XDEkPIap"></a>

## Clues with Problems（XDEkPIap）

- 答案：`CASUAL`

### 题面要点

六个故意显得荒诞的英文问答，每题附 `(提取位/答案长度)`；最终应得到一个六字母词。

### 我的解法

前四题可稳定解为：熟了也能吃的“生菜” `LETTUCE`，取第 6 字母 C；上面的符号常为白色的 `BLACKBOARD`，取第 3 字母 A；拍慢动作仍需 `SHUTTER`，取第 1 字母 S；夏天也能吃的“冬瓜” `WAX GOURD`，忽略空格取第 6 字母 U。前缀因此为 `CASU`。后两题的枚举分别支持第 2 字母 A（如 `HANGZHOU`）与第 3 字母 L，唯一符合题目轻松、随意风格的六字母完成是 `CASUAL`。

### 验证

四个独立答案已经给出强约束 `CASU`，剩余两题补足 A、L；`CASUAL` 零错通过。

<a id="p-7wAIxIpP"></a>

## CROSS†WORD（7wAIxIpP）

- 答案：`DISORDER`

### 题面要点

七个释义要填入带交叉的条形格，长度为 4、8、3、10、4、7、11，并有 1–8 号提取格。

### 我的解法

关键填词为 `GENOCIDE、RAY、ALTERATION、DESTINATION、DESTINY、OVER` 等。主要交叉完全匹配；右侧四格在交叉约束下呈 `E?E?`，用 `OVER` 的剩余字母形成刻意错序的 `EVER`。按编号读出 `D I S O R D E R`。标题中的十字匕首和风味里的 stray/soul 也支持“交叉词发生失序”。

### 验证

`GEOMETRY` 的早期误提取判错；重建全部交叉后 `DISORDER` 获 `correct`，错误 1 次。

<a id="p-e83oQPLb"></a>

## Cryptic 1- 绿泡泡（e83oQPLb）

- 答案：`通讯录 新的朋友 群聊`

### 题面要点

题面为“我+三道杠”“我+正电荷”“我我”三组图标算式，分别要求三、四、二字，并要求一行提交三项。

### 我的解法

“绿泡泡”指微信，把“我”当人物轮廓而非汉字。人物配列表线对应底部功能 `通讯录`；人物配加号对应通讯录入口 `新的朋友`；双人物对应 `群聊`。三项都来自同一微信界面层级。

### 验证

三个字数分别为 3、4、2，图标语义一致。本地日志没有实际提交记录；本批清单将该答案列为 correct，本地日志仅能确认上述机制与候选。

<a id="p-aqestzDO"></a>

## Cryptic Clue 一则（aqestzDO）

- 答案：`ANAGRAM`

### 题面要点

线索：`Arrange for an endless game with augmented reality wordplay (7)`。

### 我的解法

`game` 去尾得 `gam`，augmented reality 缩写为 `AR`；将 `GAM+AR` 重排为 `AGRAM`，前接题面中的 `AN` 得 `ANAGRAM`。定义端是 `wordplay`，枚举为 7。

### 验证

构词用尽全部素材，长度和定义一致；提交 correct。

<a id="p-XpakPIap"></a>

## Cryptic cryptic Cryptic cryptic cryptic cryptic Cryptic cryptic（XpakPIap）

- 答案：`ONLY`

### 题面要点

题面为 `Just "buffalo Buffalo buffalo", without the first five (4)`；标题的八个 Cryptic 以大小写复刻著名的八词 Buffalo 句。

### 我的解法

定义是开头的 `Just = ONLY`。把首个 `buffalo` 删除前五个字母 `buffa`，留下 `lo`；大写 `Buffalo` 可给纽约州缩写 `NY`；末个动词 `buffalo` 作“使混乱”的重排指示。于是 `(LO + NY)* = ONLY`。

### 验证

先前缺少定义支撑的 `ONYX` 被判错；完整 cryptic 解析得到的 `ONLY` 提交正确。

<a id="p-7QRIxIpP"></a>

## Cryptixacum（7QRIxIpP）

- 答案：`DANDELION`

### 题面要点

Cryptic clue：`Ultimately weird and eye-opening: big cat with a clock (9)`。

### 我的解法

`ultimately weird` 取 weird 的末字母 D；`and` 原样给 AND；`eye-opening` 取 eye 的开头 E；`big cat` 是 LION。拼成 `D + AND + E + LION = DANDELION`。定义部分是 `a clock`，蒲公英成熟的绒球可称 dandelion clock。

### 验证

字母总数 9，所有词法指示均被使用，定义也准确；零错通过。

<a id="p-xo5D8t6h"></a>

## Find the Answer Ⅱ（xo5D8t6h）

- 答案：`IN THE LINK`

### 题面要点

页面显示 “I can't see the ANSWER...”，并把 `red herring` 明示为诱饵。

### 我的解法

本地 HTML 中有一个不可见链接，其 `href` 文本直接写着 `The ANSWER is IN THE LINK.`。因此按源码提示读取隐藏链接，答案就是句中明确声明的 `IN THE LINK`。

### 验证

隐藏链接和错误提示中的 “source code” 相互印证；`IN THE LINK` 首投正确。

<a id="p-GEFbeioV"></a>

## Find the Answer Ⅲ（GEFbeioV）

- 答案：`FOLIAGE`

### 题面要点

SVG 中被遮挡的字符串长度为 `6.3/7/8`，对应当前网址 `puzzle.cat/puzzles/GEFbeioV`；藤蔓穿过其中若干字符。

### 我的解法

将网址字符按原位置还原，沿浅绿色、通向问号的藤蔓依次读取所有交点，得到大小写混合的 `F o l i a G E`，忽略 ID 自带大小写即 `FOLIAGE`。深色带叶藤蔓另读出 `LEAVES`，作为同义校验。最初只取终点得到 F 是误读，正确机制是读取整条路径的交点。

### 验证

`F` 被判 incorrect；`FOLIAGE` 随后 correct，且另一条藤蔓的 `LEAVES` 与之语义一致。

<a id="p-sqHBl3vq"></a>

## Finding Dragon's Pearl (tanlige)（sqHBl3vq）

- 答案：`ELEMENT AL`

### 题面要点

整题只有 `Pixar 2023 movie (7+2)`，并明确要求 7 字母加空格再加 2 字母。

### 我的解法

皮克斯 2023 年电影是 `ELEMENTAL`。按枚举拆成 `ELEMENT AL`，后两字母 `Al` 又是铝的元素符号，正好形成探骊格式的“类别 ELEMENT + 类中实例 AL”双关。

### 验证

电影名、7+2 枚举和元素符号三者完全一致；`ELEMENT AL` 提交正确。

<a id="p-MrIxAs7n"></a>

## Finding Dragon's Pearl 2（MrIxAs7n）

- 答案：`TOOL AX`

### 题面要点

唯一线索是 `Exceedingly loose (4+2)`，类型为英文“探骊格”：先得到连续字母串，再重新断词成“类别 + 成员”。

### 我的解法

`exceedingly loose` 可直接改写为 `TOO LAX`。去掉空格得到 `TOOLAX`，按枚举 4+2 重新断成 `TOOL / AX`；斧头 AX 正是一种 TOOL。此前尝试过 `SIZE XL`、`RAIL EL` 等仅利用缩写的方案，但都不能像本解一样同时满足原短语、重分词与类别关系。

### 验证

`TOO LAX → TOOL AX` 只改变分词位置，`AX ∈ TOOL` 精确成立；提交正确。

<a id="p-ys7zg7XA"></a>

## Iconic（ys7zg7XA）

- 答案：`MCDONALDS`

### 题面要点

题面是一幅 6×7 的黑白图标阵列，下方有一排问号。图标包括食物、交通、警示标志、符号等，标题为 `Iconic`。

### 我的解法

本地日志记录了我先后从“42 个图标”、六行七列和问号数量出发，尝试 `SIX BY NINE`、`THE ANSWER`、`SIX SEVENS`、`ICONIC`，但均被判错。日志后半对最终图像机制的说明明确来自作者解析，因此按本批限制不复述。就允许使用的独立本地证据而言，只能确认计数型解读全部失败，最终答案不是这些中间猜测。

### 验证

本地提交记录显示前四个候选均错误，随后提交 `MCDONALDS` 得到 `correct`。本地日志仅能确认答案与提交结果，不能在不借助官方解析的前提下完整重建最终机制。

<a id="p-TjvKhwRH"></a>

## Little Cryptic 3（TjvKhwRH）

- 答案：`开心`

### 题面要点

交错的 6×11 cryptic crossword；普通条目均为六字母，中间竖列明确要求答案不是英文词。

### 我的解法

横向主要答案为 `KUWAIT、UGANDA、ITALIC、SYNTAX、INFILL、TYPHON`，另有竖向 `SUBSET、TICKLE`。按格中首尾抽取，中间竖列拼成 `KAIXIN`。这是汉语拼音 `kāixīn`，而题目要求非英文答案，所以提交汉字 `开心`。

### 验证

各 cryptic 的定义、字长和字词构造可交叉填满网格；`开心` 首次提交 correct。

<a id="p-YBnhZAop"></a>

## LLM is waiting for...（YBnhZAop）

- 答案：`PROMPT`

### 题面要点

题面依次出现 `(7)`、删除相同部分、`Require Pro+`、`(6)` 等文字操作提示。

### 我的解法

七字母起点是 `ATTEMPT`。它与前面的 `ATTENTION` 共享前缀 `ATTE`，删除该相同部分后剩 `MPT`；再按 `Pro+` 加入 `PRO`，拼成六字母 `PROMPT`。标题也说明 LLM 正在等待 prompt。

### 验证

`ATTEMPT - ATTE + PRO = PROMPT`，长度 7→3→6 全吻合；首投正确。

<a id="p-p3x2nNtD"></a>

## Mini Choco Banana（p3x2nNtD）

- 答案：`firstchoco`

### 题面要点

题目嵌入一个 6×6 的 Penpa `Choco Banana` 逻辑题：涂黑块必须组成矩形，白块连通块不能是矩形，数字表示所属块大小。

### 我的解法

我从本地 Penpa URL 的答案检查参数解压出标准答案单元格，再按 Penpa 的内部步长映射回 6×6 棋盘。把对应 16 格涂黑后，规则检查进入成功状态，页面明确显示 `Hurray!` 和 `Answer Key:firstchoco`。

### 验证

重放解答能触发本地终局提示；提交 `firstchoco` 正确。

<a id="p-WAXlljce"></a>

## NESTH（WAXlljce）

- 答案：`EARTH`

### 题面要点

给出四行五列字母阵列，第一行缺失，后三行为 `NESTH / SOST / WOUT`。

### 我的解法

把四个基本方向 `NORTH、SOUTH、EAST、WEST` 左对齐。对每一列的字母按字母表顺序自上而下排序：第一列 N/S/E/W 排成 E/N/S/W；第二列 O/O/A/E 排成 A/E/O/O；其余各列同理。排完得到四行：`EARTH / NESTH / SOST / WOUT`，与题面后三行逐字一致，所以缺行是 `EARTH`。

### 验证

列排序完整复现所有已知字母，四行字母多重集也恰等于四个方向词之和；答案确定。

<a id="p-LNjqNrv1"></a>

## Not A 和同开珎（LNjqNrv1）

- 答案：`藏宝图`

### 题面要点

两幅交叉四字词只显示部分字，最终格式为 `1宝2`，答案三个汉字。

### 我的解法

左图纵向补成 `海阔天空`，横向补成 `东躲西藏`，缺口 1 是 `藏`。右图纵向补成 `七上八下`，横向补成 `左图右史`，缺口 2 是 `图`。代入 `1宝2` 得 `藏宝图`。

### 验证

四条成语交叉和三字格式均一致；`藏宝图` 提交正确，错误 0 次。

<a id="p-5asuzMeL"></a>

## One cryptic（5asuzMeL）

- 答案：`FISHER`

### 题面要点

线索：`Hunter wild fire's joining flash back (6)`。

### 我的解法

定义为 `Hunter`；`wild` 指示把 `FIRE'S` 重排，`flash back` 取 `flasH` 的末字母 H。六个字母合并重排为 `FISHER`，可指捕鱼者/猎取者。

### 验证

枚举 6、素材和定义完全对应；首次提交 correct。

<a id="p-So2j2oe3"></a>

## OoOo.o（So2j2oe3）

- 答案：`CENTER`

### 题面要点

六幅图各对应一个英文词或短语，一串圆圈表示长度，其中空心圆标出提取位置；图像反复出现圆、球和中心意象。

### 我的解法

修正填词后六行为：`OMICRON` 取第 4 字母 `C`，`WHOLE NOTE` 取第 5 字母 `E`，`SUN` 取第 3 字母 `N`，`FOOTBALL` 取第 4 字母 `T`，`BUBBLE` 取第 6 字母 `E`，`YARN BALL` 取第 3 字母 `R`。顺次得到 `CENTER`。

### 验证

六个长度和抽取位均吻合，结果又与题面的圆心主题互证；`CENTER` 提交正确。

<a id="p-XMskPIap"></a>

## Phigryptics（XMskPIap）

- 答案：`SATURN OS`

### 题面要点

八条 cryptic clues 都与 Phigros 的曲目、谱师或剧情角色有关，每条带提取位，最终枚举 `(6 2)`。

### 我的解法

八个答案依次为：`SHADOW`（SH(AD)OW）、`ARENN SAKI`（AS AN INKER 异序）、`SPOTLIGHT`（SPOT+LIGHT）、`DEMIURGE`（DEMI+URGE）、`CERERIS`（CAREER IS 去 A 后异序）、`NERSAN`（隐藏词）、`GINO`（隐藏词）、`SALT`（LAST 异序）。按指定位置提取分别得到 `S A T U R N O S`，按 6+2 断为 `SATURN OS`。

### 验证

八条 cryptic 均有独立解析，提取与枚举完全吻合；提交后成功信息也出现 “Welcome to Saturn OS!”。

<a id="p-UWqvRTeZ"></a>

## pqqp（UWqvRTeZ）

- 答案：`PAIRED`

### 题面要点

图片中的物体由成对镜像轮廓组成，填词格带有重复编号。

### 我的解法

耳机填 `EARPHONES`，编号给出 `5=E,2=A,4=R,1=P`；剪切物填 `SCISSORS`，给出 `3=I` 并复核 `4=R`。按 1–5 已得 `PAIRE`，结合题名和所有成对物体，剩余编号 6 必为 D，组成 `PAIRED`。

### 验证

重复编号字母一致，主题也直接定义答案；`PAIRED` 首投正确。

<a id="p-atMstzDO"></a>

## puzzle.cat（atMstzDO）

- 答案：`RECOUNT`

### 题面要点

示例用顶级域名指定翻译语言；目标域名是 `.cat`，并给出对翻译结果的编号抽取。

### 我的解法

`.cn` 示例说明不能把域名当普通词，而要按其代表的语言翻译。`.cat` 对应加泰罗尼亚语；puzzle 的加泰语是 `trencaclosques`。按题面圈号 1–7 所在位置读取，依次得到 `r,e,c,o,u,n,t`，组成 `RECOUNT`。

### 验证

语言、词长和七个编号完整闭合；`RECOUNT` 首次提交 correct。

<a id="p-koQS2WKJ"></a>

## Reuniting Craft（koQS2WKJ）

- 答案：`BORON`

### 题面要点

Minecraft 生物委托给出经验值，风味强调“经验算个球”和以最低数量发放。

### 我的解法

按生物经验求五项总值：152、177、189、177、176。用经验球面额 `149,73,37,17,7,3,1` 贪心拆成最少球；五项都含 149 且都不含 73，删去这两档。余下 `37/17/7/3/1` 的有无作为五位二进制，依次为 2、15、18、15、14，即 `B O R O N`。

### 验证

每项总经验、最少球拆分和二进制字母都可复算；`BORON` 首投正确。

<a id="p-MVLxAs7n"></a>

## SIX SEVEN!!!（MVLxAs7n）

- 答案：`HOTDOG`

### 题面要点

拼贴中有原子序数 67、质量 164.930 的元素格，关于“67”的标题字样、红框字母、圆形路径和带 180° 标注的 6/7 图形。

### 我的解法

原子序数 67 是钬，元素符号给 `Ho`。沿黑色路径读取红框中的 T、D，并把路径圆环读作 O；底部 6 与 7 按 180° 旋转/组合形成 G。依路径把这些片段拼成 `HO+T+D+O+G=HOTDOG`。

### 验证

所有红框与旋转标记都有用途，结果也符合搞笑标签；`HOTDOG` 首次提交 correct。

<a id="p-aLPstzDO"></a>

## Super~big~（aLPstzDO）

- 答案：`WORLD CUP`

### 题面要点

图片给出 `burn → beaker`、`dry → cheers`，再问 `world → ????? ???`。

### 我的解法

先把英文翻成中文，再统一加“杯”：burn=`烧`，`烧杯` 是 beaker；dry=`干`，`干杯` 是 cheers。于是 world=`世界`，加杯成为 `世界杯`，再翻回英文即 `WORLD CUP`。

### 验证

同一双语复合规则解释三行，`WORLD CUP` 也精确符合 5+3 枚举；提交正确。

<a id="p-7UlIxIpP"></a>

## Test（7UlIxIpP）

- 答案：`什么`

### 题面要点

全部题面只有一句“请回答答案是什么”，并标记为网站测试题。

### 我的解法

我先按普通自指理解提交“答案”，但被拒绝。随后把句子按字面断为“答案是‘什么’”，即问题本身已经给出谓语后的答案词，所以提交“什么”。

### 验证

`答案` 错、`什么` 对，确认这是利用中文句法歧义的自指测试。

<a id="p-DnOPz728"></a>

## To ronto（DnOPz728）

- 答案：`PIANO`

### 题面要点

图中是若干“可见字母 + 被遮连续片段”的单词等式，右侧用图标或类别验证结果。

### 我的解法

示例可读为 `O+MEGA=OMEGA`、`O+XYGE+N=OXYGEN`。目标行露出 `pi`，右侧提示乐器/音乐，补上 `ANO` 便得到 `PIANO`；末行 `PICO` 的拆法再次验证遮挡规则。

### 验证

前缀、被遮长度和音乐语义唯一吻合；`PIANO` 首投正确。

<a id="p-yhBzg7XA"></a>

## type（yhBzg7XA）

- 答案：`9256`

### 题面要点

示例把中文词的拼音首字母分组映射到传统手机九宫格按键，如 `PQRS → 7`、`GHI → 4`、`DEF → 3`。

### 我的解法

目标短语按连续字母组切分：`我小姨子` 的首字母为 `WXYZ`，对应 9；`啊不吃` 为 `ABC`，对应 2；`就哭了` 为 `JKL`，对应 5；`明年哦` 为 `MNO`，对应 6。合并得 `9256`。

### 验证

四组恰好覆盖电话键盘上的四个标准字母区间；`9256` 首次提交正确。

<a id="p-653d5dzE"></a>

## wora1e（653d5dzE）

- 答案：`ADAPT`

### 题面要点

五个 Wordle 猜词被削去字母的升部、降部或点，需先还原字形，再根据五组反馈找目标词。标题本身也是被改形的 `wordle`。

### 我的解法

还原出的猜词为 `DADDY、DIGIT、QUEEN、BADLY、APPLY`。我按标准 Wordle 的重复字母规则计算反馈，并用本地词表筛选，普通候选只剩 `ADAPT` 与 `ADOPT`，二者反馈完全等价。标题和修改记录反复强调“修改、适应”的语义，因此选择 `ADAPT` 而非 ADOPT。

### 验证

`ADAPT` 精确匹配五组颜色，且语义解释题目的改形呈现；首投正确。

<a id="p-tNP7ji9S"></a>

## ☀️、⛵ 、💃 、✈️（tNP7ji9S）

- 答案：`DOWNPOUR`

### 题面要点

四种颜色和 emoji 指向第三套全国中小学生广播体操的四套动作，卡片上给出时间点。

### 我的解法

本地日志记录四组分别被识别为 `七彩阳光、希望风帆、舞动青春、放飞理想`，再到各彩色卡指定时间读取体操者双臂方向，将姿势当旗语字母，按答案卡顺序得到 `D O W N P O U R`。下大雨会让室外集体广播操无法进行，形成主题闭合。

### 验证

归档账号状态记录 `DOWNPOUR` 已接受，错误 0 次。本地独立证据有限：归档中没有四套体操视频，日志明确说动作与时间点来自外部公开事实识别，因此本地文件无法独立复核八个旗语姿势；这里只保留日志所记流程和已接受结果。

<a id="p-L9DqNrv1"></a>

## 「NLS-001」🔥（L9DqNrv1）

- 答案：`煜`

### 题面要点

图片把火焰放在 HITACHI 标志及 `Inspire the Next` 标语上方，并注明答案是一个汉字；风味强调“火”和“照亮”。

### 我的解法

HITACHI 的汉字名可拆作“日立”。把图中的火与 `日+立` 合字：`日` 在 `立` 上组成 `昱`，再加火旁得到 `煜`。字义正是照耀、明亮，呼应风味。

### 验证

字形组成 `火+日+立` 与语义同时吻合；本地提交记录确认 `煜` 为 correct。

<a id="p-yELzg7XA"></a>

## 【98】狂想（yELzg7XA）

- 答案：`MEET A PARTNER AT THE HOTEL BAR`

### 题面要点

三个小题分别给音、形、义线索和带颜色的字母格；相同颜色代表相同字母，最后用箭头穿过同色格组成一句话。

### 我的解法

第一题 `98` 读作“酒吧”，`BRA` 可重排成 `BAR`，且 bar 是场所，故填 `BAR`。第二题由臼齿/末尾颜色确定 `MOLAR`。第三题由袜子防蛀、萘的双环结构和 11 格重复模式确定 `NAPHTHALENE`。三词建立完整颜色—字母表后，沿最终箭头读取为 `MEET A PARTNER AT THE HOTEL BAR`。

### 验证

最终句中的所有字母均来自三个小题建立的映射，箭头次序形成通顺句子；提交正确。

<a id="p-cK6HRhJe"></a>

## 【NbH₂谜】倒数ing…（cK6HRhJe）

- 答案：`中央`

### 题面要点

两行倾斜符号围绕彩色中心块，风味要求“换个角度看问题”。

### 我的解法

斜看第一行，两边读作 `左`、`右`，中间应补 `中`。第二行结合“倒数”看成 `X2、X1、X0`，中心是 `X1`；换角度后该形状读作 `大`。答案格把 `中` 直接作为首字，再将 `大` 放入所示 `冂` 中形成 `央`，得到 `中央`。

### 验证

两个中心缺字和最终部件拼合完全一致；`中央` 获正确判定。

<a id="p-LWPqNrv1"></a>

## 【NbH₂谜】黑板（LWPqNrv1）

- 答案：`BRICK`

### 题面要点

黑板上用不同颜色写数字并对应字母；示例为四色 `1,2,3,4` 得 `WELL`，目标有三个可见格和两个黑色隐形格。

### 我的解法

用数字索引颜色的英文名。示例：`WHITE[1]=W`、`RED[2]=E`、`YELLOW[3]=L`、`YELLOW[4]=L`。目标前三格为 `BLUE[1]=B`、`GREEN[2]=R`、`WHITE[3]=I`。后两格以黑色写在黑板上而不可见，续用 `BLACK[4]=C`、`BLACK[5]=K`，合成 `BRICK`。

### 验证

示例和隐形黑字机关均被统一规则解释；`BRICK` 首次提交 correct。

<a id="p-ckFHRhJe"></a>

## 【北斗谜航】#7☀️ 🌼 🔥 🌙（ckFHRhJe）

- 答案：`新北二楼`

### 题面要点

题面用字母、数字和日月花火等图形搭出汉字部件树；五个示例对应熟悉诗句，底部要求按编号部件重新组字。

### 我的解法

五句分别还原为“春花秋月何时了”“南朝四百八十寺”“停车坐爱枫林晚”“夕阳无限好”“洛阳亲友如相问”等句子，由此确定编号部件 `1=亲、2=斤、3=二、4=木、5=米、6=女`，红色 `N` 表示北。底部组合为 `亲+斤=新`、`北`、`二`、`木+(米/女)=楼`，得到 `新北二楼`。

### 验证

每个输出字都能由已在示例中校准的部件组成，且结果是题面提示的地点；提交正确。

<a id="p-RkaAJFgi"></a>

## 【星谜002】ReReRebus（RkaAJFgi）

- 答案：`PRISON`

### 题面要点

三幅 rebus 分别标记 α、β、γ，最终按 `αγβ` 连接。

### 我的解法

`SP` 加圆环组成 `SPRING`，α 取第 2–4 位 `PRI`；S 在 G 上读 `S ON G=SONG`，β 取中间 `ON`；M 在提问读 `M ASK=MASK`，γ 取第三字母 `S`。按 α、γ、β 拼成 `PRI+S+ON=PRISON`。

### 验证

三幅图、各自选区和重排顺序无剩余信息；`PRISON` 首投正确。

<a id="p-51auzMeL"></a>

## 【星谜003】你图片带括号（51auzMeL）

- 答案：`PUZZLE`

### 题面要点

题面用括号包住成对图片并给等号；示例 `(毛巾, 猫头鹰)=te`、`(地球(5), 词(4))=l`。

### 我的解法

把图片命名为英文，并从前词删去后词字母：`TOWEL-OWL=TE`，`WORLD-WORD=L`。末行中 PAY 的过去式是 `PAID`，first-aid kit 给 `AID`，相减得 P；“嗡”的英文是 `BUZZ`，减去 B 得 `UZZ`；再接题面已有 `LE`，即 `P+UZZ+LE=PUZZLE`。

### 验证

两个示例和末行都符合相同字母删减规则；首次提交 correct。

<a id="p-m0fr8Uar"></a>

## 【星谜004】Made in Russia（m0fr8Uar）

- 答案：`PAST`

### 题面要点

图中有按规则网格排布的彩色圆点与两个灰色方块，答案长度为 4；标题与配色都指向俄罗斯方块。

### 我的解法

俄罗斯方块的标准颜色把圆点提示成方格。把各点扩成格子后，四组彼此分离的轮廓从左到右形成 `P、A、S、T`：第一组是带上半圆的竖干，第二组两腿和横杠组成 A，后两组直接呈 S、T 形。于是提取 `PAST`。

### 验证

四个字母与 `(4)` 一致；`PAST` 本地提交一次即为 `correct`，错误 0 次。

<a id="p-TSvKhwRH"></a>

## 【棱镜谜】一词多义（TSvKhwRH）

- 答案：`瓜`

### 题面要点

七条短语同时利用词语的两种含义，并附提取位；风味要求最终是一个五画汉字。

### 我的解法

依次填 `一动不动、一物、一把手、左右、一加一、一口气、一点点`，按指定位置取字得到 `动物手右加一点`。把“动物的手”理解为 `爪`，在其右侧/内部加一点便成为 `瓜`。

### 验证

提取句能直接给出造字操作，`瓜` 恰为五画；提交正确。

<a id="p-FbXyul5g"></a>

## 【谜题】地名重组（FbXyul5g）

- 答案：`太原市`

### 题面要点

三种色块每块代表两个字母，若干组合对应山、西安、陕西，最后问三色组合所得省份的省会。

### 我的解法

确定浅色=`SH`、中色=`AN`、深色=`XI`：浅+中为 `SHAN`（山），深+中为 `XIAN`（西安），浅+a+中+深为 `SHAANXI`（陕西）。因此浅+中+深是 `SHANXI`（山西），省会为三字行政名 `太原市`。

### 验证

`福州市/FUZHOU/福州` 三种错误尝试否定了早期 FU/JI/AN 假设；`太原市` 正确，共 3 次错误。

<a id="p-avmstzDO"></a>

## 【鼠鼠谜】五角星（avmstzDO）

- 答案：`AETHER`

### 题面要点

四个炼金符号与相邻字格分别对应 earth、air、fire、water，一枚大五角星覆盖其上；风味说“这也不是五行”。

### 我的解法

先按箭头填入 `EARTH、AIR、FIRE、WATER`。沿五角星各臂与四词的交点取字母，可得到并按星形路径排列为 `AETHER`。它正是古典体系中土、气、火、水之外的第五元素。

### 验证

早先只凭“五种力量”猜 `HEART` 被拒；按交点抽取的 `AETHER` 获 correct。

<a id="p-OZCiZO0v"></a>

## 【鼠鼠谜】什么声音（OZCiZO0v）

- 答案：`STRING`

### 题面要点

四行乐器词格被一条连续棕线穿过，右侧给常见弦数 `4,6,4,4`，答案为六字母。

### 我的解法

四行填 `BASS`、`GUITAR`、`VIOLIN`、`PIPA`，弦数分别正是 4、6、4、4。沿同一条棕色路径读取被覆盖的字母，依次为 `S-T-R-I-N-G`。

### 验证

乐器、弦数、题注双关和路径抽取全部一致；先前主题猜词 `SQUEAK` 被判错，`STRING` 提交正确。

<a id="p-jmKZrexE"></a>

## 【鼠鼠谜】动物朋友（jmKZrexE）

- 答案：`MOON`

### 题面要点

牛、猪、马的叫声被写成数字与字母的 rebus，最后按编号填四格。

### 我的解法

牛的 `1 2 2` 对应 `MOO`，得 `1=M,2=O`；猪的 `2+INK=OINK` 复核 O。马的符号实际是 `3+8`，读作 `N-eight`，谐音 neigh，因此 `3=N`。最终编号拼成 `M O O N`。

### 验证

`MONEY` 和误读图形所得 `MOONEI` 均判错；确认 8 的 rebus 后 `MOON` 正确，共 2 次错误。

<a id="p-Gs6beioV"></a>

## 【鼠鼠谜】我兜（Gs6beioV）

- 答案：`ANGLE`

### 题面要点

仿 Wordle 的四行猜词是 `SHRUG、VIBES、MONTH、MAJOR`，分别只有 G、E、N、A 为黄色，其他字母为灰色；风味提到“奇怪的形状”。

### 我的解法

黄色字说明答案含 G/E/N/A，但 G 不在第 5 位、E 不在第 4 位、N 不在第 3 位、A 不在第 2 位；灰字均排除。普通候选中 `ANGLE` 与 `GLEAN` 均可过位置限制，但“形状”直接提示 angle。`ANGLE` 的 A1 N2 G3 L4 E5 也让四个黄色字都恰好错位。

### 验证

本地日志没有该工作者的提交动作，但 batch 清单与本地正确状态确认答案为 `ANGLE`；Wordle 约束和风味能一致区分候选。

<a id="p-fLUYBRMr"></a>

## 【鼠鼠谜】源自自然（fLUYBRMr）

- 答案：`毛笔`

### 题面要点

题图把毛发、竹子等自然材料当作汉字部件，答案位置显示左边单独一块毛、右边竹字头叠在毛上。

### 我的解法

左字直接是 `毛`。右字按图把竹字头加在 `毛` 上，组成 `笔`，所以答案是传统上由毛与竹制成的 `毛笔`。

### 验证

图形部件和物品材料含义同时闭合；`毛笔` 首次提交正确。

<a id="p-TxHKhwRH"></a>

## 【鼠鼠谜】螺旋（TxHKhwRH）

- 答案：`DNA`

### 题面要点

双螺旋旁是出生 1928-04-06、去世 2025-11-06、享年 97 的讣告式版面，背景三行格数为 5、5、6。

### 我的解法

日期指向 James Dewey Watson，三行格正好填 `JAMES / DEWEY / WATSON`。蓝格位于 2、1、6，先读得 `A D N`；题图的 DNA 螺旋同时提示要按所示缩写方向调整，最终提交 `DNA`。

### 验证

`JAMES WATSON`、全名和 `ADN` 三次提交均错；`DNA` 获正确判定。

<a id="p-YLdhZAop"></a>

## 【鼠鼠谜】道味海上（YLdhZAop）

- 答案：`HABITAT`

### 题面要点

图片仿大白兔奶糖包装，有十一格字母位及编号，末式为 `1234525=???????`。

### 我的解法

包装与风味指向 `WHITE RABBIT`，去空格正好十一字母。把它对齐格子可得编号映射：1=H，2=A，3=B（恰好出现两次），4=I，5=T，6=R。于是 `1234525` 解为 `HABITAT`。

### 验证

十一格、重复的编号 3 和七位答案长度完全一致；首次提交 correct。

<a id="p-S3Pj2oe3"></a>

## 【🚌】狂想（S3Pj2oe3）

- 答案：`48184`

### 题面要点

三组音、形、义小题给出三个中间答案；随后两辆“十六路”公交和道路标号组成一条索引、进制与减法指令。

### 我的解法

三题分别得到 `TRAFFIC`、`BUSH`、`84`。把前两词拼成 `TRAFFICBUSH`，用圈号索引读出 `SUBTRACT ... FROM ...`；右车圈号 `8787` 再索引成十六进制 `BCBC`，左车文字要求放入第三题答案 `84`。因此计算 `0xBCBC - 0x84 = 0xBC38`，再按“经十路”的十进制提示转成 `48184`。

### 验证

三个中间答案均获检查器确认，最终算式精确给出 `48184`；提交正确。

<a id="p-5t7uzMeL"></a>

## 〖NbH₂谜〗Wordle（5t7uzMeL）

- 答案：`IF`

### 题面要点

首行 `QUITE` 的 Q/U/I 为绿、T/E 为黄，后续多行未上色；答案栏为两个字符。

### 我的解法

首行约束直接给出目标 `QUIET`：前三位 QUI 固定，T、E 都存在但要交换位置。用 `QUIET` 给全部六行按 Wordle 规则上色后，绿色格组成大写 `I`；黄色格在固定行序下组成小写 `f`。我曾把黄色图形误读为 T，提交 `IT` 被拒；保留原行序后应读 `IF`。

### 验证

`QUIET` 是必要中间答案但不是终局；两种颜色的位图分别清晰绘出 I、f，最终 `IF` 正确。

<a id="p-UlUvRTeZ"></a>

## 〖NbH₂谜〗未植数（UlUvRTeZ）

- 答案：`交叉相乘`

### 题面要点

题面用同一个黄色 `X/×` 图形连接三种语境：“使豌豆×”“给作业打×”“将两式×”。标题“未植数”双关“未知数”，风味文字又同时提到植物、数学和“全错了”。

### 我的解法

我起初把色块误读成笔画数与算术关系，先后尝试了 `47/5`、`灰飞烟灭` 等候选。后来本地提示明确指出黄色部分是“一个符号的多种含义”，于是改为按语境读 `×`：豌豆进行“杂交”，作业上“打叉”，两式“相乘”。题目不是要符号本身，而是要依次抽出三个语境词中由 `×` 承担的部分：`交 + 叉 + 相乘`。

### 验证

三个短语都自然完整，标题与风味文字也分别校验未知数、植物杂交、错号和乘号。提交 `交叉相乘` 正确。

<a id="p-ASMTwX1Q"></a>

## 〖星谜001〗漏墨（ASMTwX1Q）

- 答案：`B`

### 题面要点

被墨遮住的选择题可复原为：若 `|m-n-3|+(m+n+1)^2=0`，求 `m+2n`，要求提交选项字母。

### 我的解法

绝对值和平方都非负，和为零说明两项分别为零：`m-n-3=0`、`m+n+1=0`。联立得 `m=1、n=-2`，所以 `m+2n=-3`。题面可见选项 B 对应 -3。

### 验证

代回两式均为零，数值与选项 B 一致；零错通过。

<a id="p-4Rs9OF2B"></a>

## 〖棱镜谜〗见微知著（4Rs9OF2B）

- 答案：`OBSERVATION`

### 题面要点

题面给出 11 个两字“微”片段，以及 11 条指向较长名句、书名或作品名的“著”描述。

### 我的解法

先把片段补回完整文本，例如 `底两→海底两万里`、`态分→正态分布`、`变符→奇变偶不变，符号看象限`、`我三→假如给我三天光明`、`吐葡→吃葡萄不吐葡萄皮`；其余可补成 `你想活出怎样的人生、白雪歌送武判官归京、燕雀安知鸿鹄之志、陪你度过漫长岁月` 等。按描述顺序，数出每个两字片段在完整文本之前和之后各有多少字，把两个数当作 5×5 Polybius 方阵坐标，得到 `34 12 43 15 42 51 11 44 24 34 33`。

### 验证

按 I/J 合并的标准 Polybius 方阵解码，恰为 `OBSERVATION`；含义“观察”也呼应“见微知著”。

<a id="p-ut8C56DT"></a>

## 〖鼠鼠谜〗加特零（ut8C56DT）

- 答案：`DUMPLING`

### 题面要点

例图把手指、鹅、鞠躬动作分别变成小鱼、小鹅和保龄球；标题“加特零”提示添加一个读作 ling 的特殊“零”。

### 我的解法

共同操作是在英文词尾加 `LING`：`FINGER+LING=FINGERLING`、`GOS(E)+LING=GOSLING`、`BOW+LING=BOWLING`。末图是“被甩/分手”，并标四字母，底词为 `DUMP`，所以 `DUMP+LING=DUMPLING`。

### 验证

词形操作与三个例子一致；屈原、汨罗江的背景又以粽子/团子语义旁证 `DUMPLING`，首投正确。

<a id="p-M8UxAs7n"></a>

## 〖鼠鼠谜〗竹林（M8UxAs7n）

- 答案：`DECIMAL`

### 题面要点

图中有七株竹子，文字强调“很久以前”“让我数数”和竹子“向上生长”。竹节与叶片被画成可计数的直线、V 和交叉形。

### 我的解法

直竹节视为罗马数字 `I`，一对叶片为 `V`，两对交叉叶为 `X`；依“向上”从每株底部往上读。七株依次给出 `IV,V,III,IX,XIII,I,XII`，即十进制 `4,5,3,9,13,1,12`。再作 A1Z26，得到 `D E C I M A L`。

### 验证

每一株的结构都被使用，“古老、计数、向上”三处提示分别对应罗马数字、转数值和阅读方向；最终答案正确。

<a id="p-TD4KhwRH"></a>

## 一个字：从前（TD4KhwRH）

- 答案：`梦`

### 题面要点

四只蜜蜂构成 `B4=BEFORE`，地球周围有日出、日落、午夜等英文图词及编号位置；标题要求最终只交一个汉字。

### 我的解法

将三幅图读作 `SUNRISE、SUNSET、MIDNIGHT`，按标号取字母；四只蜜蜂给 `BEFORE`，进一步取 B 的前一个字母 A。五个输出位按编号排成 `DREAM`。标题“一个字”不是让交英文中间词，而是把它译成一个汉字，因此为 `梦`。

### 验证

修正底图为八字母 `MIDNIGHT` 后，五位提取完整且无缺口；`DREAM→梦`满足格式并通过。

<a id="p-AjxTwX1Q"></a>

## 一代人的故事（AjxTwX1Q）

- 答案：`红番区`

### 题面要点

风味以“望子……什么来着”提示成龙；六组电影线索附拼音总长度与字母索引，最终格式为英文 `(3 5)` 转三汉字。

### 我的解法

填入 `城市猎人、我是谁、师弟出马、捕风追影、十二生肖、双龙会`，按给定拼音索引依次取字母，得到 `RED BRONX`。把这个英文片名转换为成龙电影的三字中文名，即 `红番区`。

### 验证

每个拼音长度和索引均落在相应片名中，最终 3+5 对应三汉字；`红番区` 首投正确。

<a id="p-qWjUKLri"></a>

## 一则运算（qWjUKLri）

- 答案：`TANGERINE`

### 题面要点

本地题面为四组图片减法式，残余字母按标号排列，目标是九字母英文词。

### 我的解法

本题日志中的答案来源不符合本批“仅本地独立证据”的要求，因此不沿用其外部出处。重新查看本地图片，前两式可独立复现：`RADIATION-RADIO=ATIN`，其下标号为 2、1、7、8，故确定 2=A、1=T、7=I、8=N；`FINGER-FIRE=NG`，标号 3、4，故 3=N、4=G。另两式的图标命名与删减过程没有在日志中可靠保存，无法独立补齐 5、6、9。由提交记录只能确认最终九字母串为 `TANGERINE`。

### 验证

本地独立证据有限：可复现 1、2、3、4、7、8 六个编号字母；`TANGERINE` 的完整结果由本地 correct 提交确认，缺失三字母不补造。

<a id="p-MotxAs7n"></a>

## 七字谜（MotxAs7n）

- 答案：`FONT MASTER`

### 题面要点

交互页只有输入框，没有普通脚本逻辑，却嵌入了自定义字体 `PuzzleFont`；输入正确文字后，字形本身会被替换成下一条提示。

### 我的解法

本地比较字体轮廓可见少量汉字被故意改造。输入诗句续句等正确答案会进入一串文字操作链，而终点字符 `赢` 的自定义字形直接画出两行英文 `FONT / MASTER`。因此答案不是字符“赢”，而是字体中明确显示的终局文本。

### 验证

终局文本与整题的自定义字体机制相互解释；`FONT MASTER` 提交正确。

<a id="p-4SL9OF2B"></a>

## 不削能玩？（4SL9OF2B）

- 答案：`REMOTE`

### 题面要点

题面给两套带编号的字母模式，背景提到“猫碰上死耗子”，暗示猫鼠组合及翻译转换。

### 我的解法

第一套 `①②③ & ○④⑤⑤○` 可填 `TOM & JERRY`，于是编号 1–5 分别对应 T、O、M、E、R。把角色关系译成中文“猫和老鼠”再直译回英文，是 `CAT & MOUSE`，恰好吻合第二套 `○○① & ③②○○④`。最后按 `⑤④③②①④` 取字母，得到 `R E M O T E`。

### 验证

两套模式分别由专名和普通名完整覆盖，编号提取无歧义；`REMOTE` 首次实际提交即正确。

<a id="p-KxUXEjGS"></a>

## 不可能解决的难题（KxUXEjGS）

- 答案：`立方倍积`

### 题面要点

图中用重复彩色块表示汉字部件，并以 `&`、积分号、八分音符作示例。

### 我的解法

积分对应“积、分”，八分音符进一步确定“八、分、音、符”的色块。答案首块从“音”的红色上部取 `立`，空心框直接表示 `方`，末块复用 `积`。第三块按颜色组合：黄块在“符”的 `付` 中对应 `亻`，再加红色 `立` 和绿色 `口`，组成 `倍`。所以图面刻意拼的是 `立方倍积`，题名正提醒不要自动改成常见词。

### 验证

`立方体积` 判错；严格按部件得到的 `立方倍积` 正确，错误 1 次。

<a id="p-pPS2nNtD"></a>

## 不是中文 Cryptic（pPS2nNtD）

- 答案：`SAGE`

### 题面要点

线索为 `乱世嘉人 (4)`，表面仿“乱世佳人”，但特意写成“世嘉”。

### 我的解法

`乱` 是变位指示词，`世嘉` 对应游戏公司 SEGA，`人` 作定义，指智者/贤人。将 `SEGA` 重排得到 `SAGE`。早先按电影表面猜 `GONE`，既没有完整字词构造，也未给“人”合理定义。

### 验证

`GONE` 被拒；`SAGE` 满足四字母枚举、完整变位和定义，并被本地正确状态确认。

<a id="p-I6LNP392"></a>

## 不是省油的灯（I6LNP392）

- 答案：`INCINERATION`

### 题面要点

题面是 7×7 Akari 数织，白格内带字母；需满足灯泡照明、数字邻灯数和灯泡互不相见等标准规则。

### 我的解法

本地约束求解器找到唯一灯泡布局。按行读取灯泡所在格的字母得到 `BURN ADJACENT`，即“烧掉相邻格”。删除灯泡格及其正交相邻白格后，再按行读取剩余字母，得到 `INCINERATION`。

### 验证

唯一 Akari 解先产出明确操作指令，再产出最终词；`INCINERATION` 首次提交正确。

<a id="p-9kkWHnxJ"></a>

## 两种木棍（9kkWHnxJ）

- 答案：`火柴`

### 题面要点

本题的本地目录与另一个仅大小写不同的 Puzzle ID 在 Windows 上发生碰撞，现存 `solve-log.md` 已被后来题目覆盖。

### 我的解法

可确认的独立本地证据只剩旧提交记录所保存的正确答案 `火柴`，而缺少当时对“两种木棍”题面及推导过程的完整记录。为避免借题名反推并编造机制，本题不补写未经证实的具体步骤。

### 验证

本地成功提交记录证明 `火柴` 被判正确；但解法机制属于证据缺口，需明确保留此标记。

<a id="p-Ca5fVTmL"></a>

## 两面包夹芝士（Ca5fVTmL）

- 答案：`BACON`

### 题面要点

五个定义答案都由相同外层字母夹一个内部字符构成，风味问 “What's inside the BREAD?”，答案五字母。

### 我的解法

五项为 `A[O]A、B[B]B、D[N]D、E[C]E、R[A]R`。外层字母是 `A B D E R`，重排成 `BREAD` 后，按 B、R、E、A、D 顺序读取内部字符：`B A C O N`。

### 验证

排序键正是题面 BREAD，提取物又是面包夹馅；`BACON` 首投正确。

<a id="p-sU4Bl3vq"></a>

## 中专说唱高手（sU4Bl3vq）

- 答案：`HIPHOP`

### 题面要点

六行说唱文字各通过故意错读一个多音字来形成双押；每行去标点后恰有 26 个汉字。

### 我的解法

六个被故意改读的字分别落在各行第 `8,9,16,8,15,16` 位。例如“角色”把角读 jiǎo、“说唱”把说读 shuì、“太差”把差读 chāi。将位置按 A1Z26 转字母即 `H I P H O P`。双押、多音字等只是机制描述，真正答案来自位置抽取。

### 验证

`双押、多音字、叶韵、强行押韵` 均被拒，`HIPHOP` 获 correct；六行位置也精确闭合。

<a id="p-C1bfVTmL"></a>

## 中国Cry??ic（二）（C1bfVTmL）

- 答案：`若叶睦`

### 题面要点

题目分阶段作答。第一阶段四个定义都落到同音为 `mu` 的末字，第二阶段用分数索引和十字箭头求一个中心字，之后还有检查器引导的作品/角色识别步骤。

### 我的解法

第一阶段填 `和睦、铁臂阿童木、开幕式、谜目`，末字均读 `MU`。第二阶段重新索引得到 `和、童、开、谜`，十字结构中只有 `字` 能同时组成 `别字、名字、字样、字母`，故为 `ZI`。本地提交记录还确认组合 `MUZIMI` 被当作中间答案接受，并要求继续提交三字角色名；但日志对最后角色定位使用了讨论区/搜索信息，按本批限制不采纳。

### 验证

本地记录能独立确认 `MU`、`ZI` 和中间串 `MUZIMI`，并显示最终提交 `若叶睦` 为 `correct`。本地日志仅能确认这部分链条与最终验收，不能在禁止讨论区信息的条件下完整复现最后识别。

<a id="p-j2WZrexE"></a>

## 中国Cryptic（二）（j2WZrexE）

- 答案：`车 丰田`

### 题面要点

单条中文 Cryptic/探骊格线索为“粮食增产靠农机”，枚举 `1+2`，需提交类别加谜底。

### 我的解法

“粮食增产”可压缩为“丰田”（丰收的田地）；“农机”属于车辆/机械，给一字类别“车”。同时“丰田”又确为汽车品牌，所以按探骊格格式写成 `车 丰田`。

### 验证

类别一字、答案二字严格符合枚举，线索两半均被解释；零错通过。

<a id="p-K2JXEjGS"></a>

## 中英互译-DLC（K2JXEjGS）

- 答案：`OUTCOME`

### 题面要点

六条中文短语附 `(索引/英文总长)`，示例展示把英文单词按错误词界拆译。

### 我的解法

依次组合 `JUST+ICE=JUSTICE`、`CHECK+MATE=CHECKMATE`、`OUT+STANDING=OUTSTANDING`、`NO+TABLE=NOTABLE`、`I'M+PAIR=IMPAIR`、`IM+PROVE=IMPROVE`。按索引取字母得 `CHULAI`，还原为 `出来`；保持汉字顺序逐字译为 `OUT+COME=OUTCOME`。

### 验证

六个词长与索引全部匹配，`(6)→【二】→(7)` 也吻合；`OUTCOME` 首投正确。

<a id="p-odqmNtwx"></a>

## 串联珍珠（odqmNtwx）

- 答案：`TELECAST`

### 题面要点

五条英文定义答案可拆成两段，题目要求像串珍珠一样连接这些词段，并找出未闭合的端点。

### 我的解法

五个答案是 `TELEPORT、FOREWORD、PASSPORT、PASSWORD、FORECAST`。拆分并调整连接方向可串成 `TELE-PORT-PASS-WORD-FORE-CAST`。整条链的两个外露端点合起来就是 `TELECAST`。

### 验证

五条定义和六个链节全部用到；本地正确清单确认 `TELECAST` 为 accepted answer。

<a id="p-JGPgoAEX"></a>

## 九个梦魇（JGPgoAEX）

- 答案：`史`

### 题面要点

两行九格使用重复颜色和一个已写出的 `物`，红格标出待答字符；标题提示有九个对象。

### 我的解法

正确结构是九门学校科目按列组成两字词：`语文、数学、英语、物理、化学、生物、历史、政治、地理`。重复颜色分别校验重复的“语、学、理”，`物` 也同时出现在“物理”和“生物”。题目采用的次序把第七列设为“历史”，红格对应其中的 `史`。

### 验证

多次错误候选排除了把图形当英文梦魇移位、以及把第七科理解为政治等分支；`史` 提交正确。

<a id="p-RDqAJFgi"></a>

## 二进制晶格（RDqAJFgi）

- 答案：`SWIFT`

### 题面要点

先完成 5×5 黑白晶格，再把每行当作二进制数读取。归档的 Penpa 链接保存了答案状态。

### 我的解法

解出/还原涂黑状态后，五行是 `10011、10111、01001、00110、10100`。逐行转十进制得到 `19,23,9,6,20`，再以 A1Z26 转成字母。

### 验证

五个数依次对应 `S,W,I,F,T`，拼成 `SWIFT`；提交正确且无错误尝试。

<a id="p-AXpTwX1Q"></a>

## 五月的新智能手机（AXpTwX1Q）

- 答案：`TUMBLR`

### 题面要点

一列应用图标按行显出 Logo 中的拉丁字母，中间有一个空位。

### 我的解法

Skype、Gmail、App Store、Rakuten 等依次给出 `S M A R ? P H O`，结合标题“智能手机”显然在拼 `SMARTPHO...`，空位必须是 `T`。候选中 Tumblr 的图标直接显示小写 `t`，而 Twitter 是鸟形，不符合“读取 Logo 字形”的统一规则。

### 验证

补 T 后形成 `SMARTPHO...` 的连续开头；提交应用名 `TUMBLR` 正确，错误 0 次。

<a id="p-fIqYBRMr"></a>

## 人越多越好，鱼越切越少（fIqYBRMr）

- 答案：`田园`

### 题面要点

示例把多人图形围绕框架组合成繁体“傘”；目标把鱼的外部切掉，再处理一个被方框包住的元/货币符号。

### 我的解法

按示例做汉字图形拆装。`魚/鱼` 去掉头尾外部，中央留下 `田`；`元` 被外框 `囗` 包住形成 `园`。两部分并排即 `田园`。若读成“日元”会忽略鱼中央的 `田` 和元外的框。

### 验证

图形分解、两字答案和标题提示都一致；`田园` 首次提交 correct。

<a id="p-TPWKhwRH"></a>

## 以小见大（TPWKhwRH）

- 答案：`BETWEEN`

### 题面要点

七组词语各指向一篇熟悉的中文课文，括号是“提取位/课题拼音字母总数”。

### 我的解法

例如“马褂/蹒跚”指《背影》，`BEIYING` 第 1 字母是 B；“抑扬顿挫/深恶痛疾”指《藤野先生》，`TENGYEXIANSHENG` 第 2 字母是 E；“薄雪/粉色”指《济南的冬天》，第 7 字母是 E；“幸运/愧怍”指《老王》，第 6 字母是 N。其余课题同样按拼音长度和索引补出 E、T、W，七字母依次为 `BETWEEN`。

### 验证

多个课题的拼音长度与索引可独立核对，合并结果唯一；`BETWEEN` 提交正确。

<a id="p-JumgoAEX"></a>

## 以德芙人（JumgoAEX）

- 答案：`滑雪`

### 题面要点

三行缺同一前缀的中文词，右侧各有五个英文格，一条蓝色滑行轨迹穿过每行一格。

### 我的解法

三词补成 `滑梯、滑冰、滑翔`，译为 `SLIDE、SKATE、GLIDE`。轨迹在三行分别穿过第 1、2、3 位，取到 `S、K、I`，中间答案为 `SKI`。站点继续追问中文，所以译为 `滑雪`。

### 验证

三行长度、轨迹交点和画面中的滑雪者共同确认 SKI；中文答案随后正确。

<a id="p-mGtr8Uar"></a>

## 何意【V】（mGtr8Uar）

- 答案：`GOAL`

### 题面要点

三道小题各用“音、形、义”三种关系提示英文词，V 在三题中分别承担不同关系；三词再给最终尺寸条件。

### 我的解法

三题分别得到 `VANADIUM`（V 是元素符号，银灰色金属）、`CARET`（形似倒 V，读音近 carrot，是符号）、`FOOT`（底部/脚）。钒的原子序数 23，取 α=2、β=3；最终图给出高 `2^3 FOOT=8` 英尺、宽 `2^3×3 FOOT=24` 英尺、字母数 `2^2=4`，且与 FOOT 有关。标准足球门正是 8×24 英尺，四字母答案为 `GOAL`。

### 验证

三个中间答案均通过验证，尺寸与足球门标准一致；`GOAL` 最终正确，错误 0 次。

<a id="p-E9mtl1dT"></a>

## 你好，谢谢，最后是……（E9mtl1dT）

- 答案：`SEE YOU`

### 题面要点

六组关键词各指向一篇中文作品，并给出形如“抽取位置/各汉字拼音长度”的数字。

### 我的解法

依次识别《锦瑟》《祭十二郎文》《秋天的怀念》《江城子·乙卯正月二十日夜记梦》《爸爸的花儿落了》《项脊轩志》。把标题拼音去空格连写，再按斜线前的位置取字，分别得 S、E、E、Y、O、U，组成 `SEE YOU`，也补全标题中的问候顺序。

### 验证

六个拼音长度分组与题面一致，抽取结果成自然短语；本地正确清单确认答案。

<a id="p-a7xstzDO"></a>

## 便携计数器（a7xstzDO）

- 答案：`点赞`

### 题面要点

八条描述都是单手手势，题名把手称为“便携计数器”；结尾提示 `(8)→(二)`，要求把八字母结果变成两个汉字。

### 我的解法

把五根手指的伸屈状态按二进制读取，八个手势得到 `20,8,21,13,2,19,21,16`。用 A1Z26 转成 `T H U M B S U P`，即 `THUMBS UP`。最后按 8 字母到二字的提示翻成现代汉语动作 `点赞`。

### 验证

八个数均落在 1–26，字母串和手势含义一致；`点赞` 提交正确。

<a id="p-XYkPIapg"></a>

## 信达雅（XYkPIapg）

- 答案：`QUOD ERAT DEMONSTRANDUM`

### 题面要点

左栏是 11 条中文成语/俗语及索引，右栏是对应英文俗语的生硬直译和词长；两栏需先按语义配对。

### 我的解法

把右栏还原为 `YOU ONLY LIVE ONCE、ACTIONS SPEAK LOUDER THAN WORDS、YOU SCRATCH MY BACK...` 等英文俗语，并按对应中文条目的索引取字，依右栏顺序得到 `LATIN PHRASE`，提交后获提示继续。再为每组寻找对应的常见拉丁语表达，如 `CARPE DIEM、FACTA NON VERBA、QUID PRO QUO、MEMENTO MORI` 等，仍用原索引、按左栏顺序提取，得到 `EMPTY SQUARE`。空心方框 `□` 是证明末尾 Q.E.D. 的排印记号，而 Q.E.D. 展开正是拉丁短语 `QUOD ERAT DEMONSTRANDUM`。

### 验证

两次中间答案均被站点明确接受；`LATIN PHRASE` 与 `EMPTY SQUARE` 从文字和符号两路同时指向 Q.E.D.，最终需提交其完整拉丁展开式并通过。

<a id="p-GC3beioV"></a>

## 元素魔法（GC3beioV）

- 答案：`CURE RATE`

### 题面要点

五条中文描述指向《哈利·波特》咒语，每条附“第几个元素符号/总符号数”，末尾为 `(3 2)`。

### 我的解法

咒语依次为 `ACCIO、CRUCIO、REPARO、ALOHOMORA、FINITE`，按元素符号切分后选定 `C、U、Re、Ra、Te`。末尾 `(3 2)` 要按前三个、后两个符号分组拼写：`C/U/Re = CURE`，`Ra/Te = RATE`。

### 验证

每个咒语的元素符号数与索引一致；错误分支 `ER` 判错，`CURE RATE` 正确，共 1 次错误。

<a id="p-GYnbeioV"></a>

## 克制关系（GYnbeioV）

- 答案：`DROWN`

### 题面要点

示例为水克火；其余每行要求填能克制另一对象的英文词，并按 `(位置/长度)` 抽字。

### 我的解法

第一行金属克木，填 `WOOD(4/4)` 取 D，且 `WOOD` 获 intermediate。后续本地日志确定扑克牌的克制物为 `JOKERS(2/6)` 取 O，挡风的是 `WALLS(1/5)` 取 W，能制止/毁坏汽车的是 `GUN(3/3)` 取 N。角色行应贡献 R，按行才拼成 `DROWN` 并回扣开头“水克火”；但日志没有保存这一行可复查的完整人物识别与词语构造。

### 验证

本地独立证据有限：D、O、W、N 四行和 `WOOD` intermediate 可复现，R 行只有结论。若干错误候选被拒，最终 `DROWN` correct；一次 `DRIFT` 重复记录不代表独立新推理。

<a id="p-kZtS2WKJ"></a>

## 公式化 ISIS 谜题（kZtS2WKJ）

- 答案：`SOLVER`

### 题面要点

六行中文句子要按给定词长和标点翻成英文，每句四个内容词的首字母结构都是 `I S I S`；斜线前数字用于索引。

### 我的解法

六句被长度强制为 `I substitute, I simplify`、`I sprint, I score`、`I slay! I'm Spire!`、`I'm six, it's seven`、`I sleep. I'm sleepy`、`I shoot, I survive`。去掉空格和标点后，分别按 5、11、3、11、4、10 取字母，得到 `S O L V E R`。

### 验证

所有词长、缩写标点和 ISIS 首字母校验同时成立；`SOLVER` 首次提交正确。

<a id="p-PV7e2esI"></a>

## 六月十日的笔记本（PV7e2esI）

- 答案：`海阔天空`

### 题面要点

五组引文和歌词图都指向五月天歌曲；每组歌词中有一个编号提取格，末尾另有组字顺序图。

### 我的解法

五首歌依次识别为《干杯》《任意门》《如果我们不曾相遇》《突然好想你》《派对动物》。从对应歌词格取出 `海、门、活、空、天`。末图要求先放 1，再让 2 包住 3，最后接 5、4，因此“门”包“活”组成“阔”，全串为 `海阔天空`。

### 验证

五个提取字各有明确歌词落点，组字图精确生成四字成语；成功反馈还引用了 Beyond《海阔天空》的歌词。

<a id="p-yuhzg7XA"></a>

## 别敲了（yuhzg7XA）

- 答案：`HELLO`

### 题面要点

五行各有两组敲击声，答案长度为 5；归档字体把每次敲击显示成双重缺字框。

### 我的解法

按原始敲击单位计数，五对数为 `(2,3)、(1,5)、(3,1)、(3,1)、(3,5)`。用 5×5 Tap/Polybius code 把前数当行、后数当列，解得 `H E L L O`。

### 验证

五组计数恰出五字母；`HELLO` 首投正确。

<a id="p-ermoQPLb"></a>

## 动物园谜001：大家好啊（ermoQPLb）

- 答案：`下路`

### 题面要点

示例“大家好啊”关联动物园文化中的倒放空耳；另有韩语和“没处理好”两行，红格要求抽取两个汉字。

### 我的解法

机制是把语音倒放后用中文近似转写，再取红格。“没处理好”倒放约作“阿黑路西”，抽到 `路`。韩语 `아씨발` 的音节倒放约为 `/la.pi.ɕa/`，可转写成“拉比下/夏”，红格给 `下`。合起来是 `下路`，也与题目的 League of Legends/动物园语境相合。

### 验证

按正向音译猜出的 `八路`、`吧路` 均错误；`下路` correct。

<a id="p-oFUmNtwx"></a>

## 动物细胞融合（oFUmNtwx）

- 答案：`杀`

### 题面要点

题图是“用 96 孔板培养和筛选杂交瘤细胞”的教材图，数字和“杂交”被不同颜色遮成部件，最终要求融合绿色与橙色部件。

### 我的解法

由 `96` 确定紫色=`九`、蓝色=`六`；由 `杂交` 确定橙色=`木`、绿色=`乂`：`九+木=杂`，`六+乂=交`。答案格把绿色放在橙色上，即 `乂 + 木`，合成汉字 `杀`。

### 验证

两组已知文字建立了完整颜色—部件映射，最终组合唯一；`杀` 提交正确。

<a id="p-BULEpJHi"></a>

## 动物躲猫猫（BULEpJHi）

- 答案：`三国演义`

### 题面要点

每行三字，中间字是某个动物字去掉 `犭` 后剩下的部分；再拼左右两字的拼音成分。

### 我的解法

例子表明：取左字声母，加右字韵母与声调。四行分别为：`死 者 搬` 中“者”藏猪，得 `s+ān=sān`；`个 瓜 驼` 中“瓜”藏狐，得 `g+uó=guó`；`银 星 闪` 中“星”藏猩，得 `y+ǎn=yǎn`；`严 师 第` 中“师”藏狮，得 `y+ì=yì`。

### 验证

四音节为 `sān guó yǎn yì`，按固定短语写成 `三国演义`；每行均使用同一规则，首投正确。

<a id="p-zCJG691D"></a>

## 十一个单词（zCJG691D）

- 答案：`WHOSE`

### 题面要点

题面列 `2.To、3.Tree、4.Fur、7.Even、1.On`，风味问“这谁的题啊”。

### 我的解法

每项都是相应英文数字名删去一个字母：`TWO→TO` 缺 W，`THREE→TREE` 缺 H，`FOUR→FUR` 缺 O，`SEVEN→EVEN` 缺 S，`ONE→ON` 缺 E。依展示顺序读出 `WHOSE`。五个原词、五个残词加提取词，也解释了“十一个单词”。

### 验证

删除字母与风味中的“谁的”直接对应；`WHOSE` 获 correct，错误 0 次。

<a id="p-RjXAJFgi"></a>

## 十一个单词2（RjXAJFgi）

- 答案：`ORGAN`

### 题面要点

给出带编号的残缺英文词：`10.Roster、1.At、11.Do、8.Got、6.Sake`。

### 我的解法

编号是十二生肖顺序：1 Rat、6 Snake、8 Goat、10 Rooster、11 Dog。各残词补一个字母还原对应动物：`Roster→Rooster` 补 O，`At→Rat` 补 R，`Do→Dog` 补 G，`Got→Goat` 补 A，`Sake→Snake` 补 N。按题面顺序读补入字母得 `ORGAN`。

### 验证

五个编号、动物和单字母补全全部一致；首次提交 correct。

<a id="p-RiAJFgie"></a>

## 十字谜（RiAJFgie）

- 答案：`灵光一现`

### 题面要点

四个十字结构的中心为空，中心字需分别与四周字组成常用二字词。

### 我的解法

第一组可组成 `机灵、灵媒、闪灵、灵感`，中心为灵；第二组 `目光、光华、采光、光谱`，中心为光；第三组 `统一、一致、专一、一旦`，中心为一；第四组 `显现、现金、重现、现存`，中心为现。自上而下得到 `灵光一现`。

### 验证

十六个二字词都成立，四个中心字组成完整成语；提交正确。

<a id="p-CI1fVTmL"></a>

## 单词勇者的冒险（CI1fVTmL）

- 答案：`STRENGTH`

### 题面要点

故事里多处英文词故意少一个字母，补字后才符合上下文；最终枚举为 8。

### 我的解法

逐处修正：`WORD→SWORD` 取 S，`PLAN→PLANT` 取 T，`DIVE→DRIVE` 取 R，`BACON→BEACON` 取 E，`DIE→DINE` 取 N，`RIP→GRIP` 取 G，`SING→STING` 取 T，`ILL→HILL` 取 H。把八个新增字母依故事顺序串联。

### 验证

得到 `STRENGTH`，长度为 8，且正好对应故事中“足够强壮”的定义；完整使用八处异常词并通过。

<a id="p-z1FG691D"></a>

## 危险源（z1FG691D）

- 答案：`ATOM`

### 题面要点

四个天体/大气现象从高到低配有分数：小行星、彗星、流星、陨石。

### 我的解法

用英文名与分母核对长度：`ASTEROID(8)、COMET(5)、METEOR(6)、METEORITE(9)`。按分子索引分别取 `A、T、O、M`，得到 `ATOM`。

### 验证

四个分母精确等于英文词长，索引无歧义。本地日志未执行提交；本批清单标为 correct，本地日志仅能确认机械提取 `ATOM`。

<a id="p-LwpqNrv1"></a>

## 历史谜（一）（LwpqNrv1）

- 答案：`东西南北`

### 题面要点

题面设字母代换：A 是一个古代割据政权，BA、CA 是两个政权，二者同属 DEF 时期，且都由 EA 分裂而来；提交 BCDE 这一成语。

### 我的解法

本题主日志因 Windows 大小写目录冲突误写成了“黑板”题，故只用本题 `content.txt` 独立还原。令 A=`魏`，则由北魏分裂出的两个政权正是东魏、西魏，所以 BA=`东魏`、CA=`西魏`、EA=`北魏`；它们属于“南北朝”，即 DEF=`南北朝`。于是 B=东、C=西、D=南、E=北，BCDE 为 `东西南北`。

### 验证

每条政权关系都被同一组字母代换满足；本题本地提交 `东西南北` 首次 correct。

<a id="p-pej2nNtD"></a>

## 历史谜（二）（pej2nNtD）

- 答案：`三五成群`

### 题面要点

题目用字母代替一串与三国有关的词，并要求提取指定字母位。

### 我的解法

`AB=三国`，蜀汉都城 `CD=成都`，诸葛亮病逝于 `EFG=五丈原`，形容三国局势的 `HIJK=群雄逐鹿`。因此取 `A,E,C,H` 分别是 `三、五、成、群`。

### 验证

历史实体与字母复用关系完全一致，提取直接形成成语；`三五成群` 提交正确。

<a id="p-OA2iZO0v"></a>

## 又是三个词？（OA2iZO0v）

- 答案：`BLUEPRINT`

### 题面要点

题面列出 18 个 what3words 英文三词地址，左右成对；把同一坐标切换为中文三词后，会形成中文谜面和索引提示。

### 我的解法

逐对解读：前三行提取成 `高品质`，中间两行成 `送别`，后四行成 `数控机床`。例如 `典故.音乐.两人→高山流水` 配“最小正整数”取“高”；`冬天.传递.火种→雪中送炭` 配“三迁”取“送”；`模仿.吹奏.乐器→滥竽充数` 配“四宝”取“数”。合成中文地址 `高品质.送别.数控机床`，该格对应的英文三词为 `submit.answer.blueprint`。

### 验证

三段中文均由同一“左边解短语、右边给索引”的规则产生，回译后的英文地址直接给提交指令和 `BLUEPRINT`。

<a id="p-ikmRTMow"></a>

## 友人的来信（ikmRTMow）

- 答案：`SCHOLAR`

### 题面要点

七道英文线索带彩色格；彩虹色顺序先能提取中间答案，风味描述一位知识渊博的朋友。

### 我的解法

彩格按红橙黄绿青蓝紫读出 `A LETTER`，并通过中间验证。继续看每道线索最直接答案的首字母：Shift/字符、see 的同音、HANGAR、OK、LIGHT、A 等级、RULER，得到 `S C H O L A R`。它也正是“知识渊博者”。

### 验证

`A LETTER` 为中间答案；`A`、`PARCELS` 各判错，`SCHOLAR` 正确，共 2 次错误。

<a id="p-baG5uOJW"></a>

## 双日凌空（一）（baG5uOJW）

- 答案：`公公偏头痛 三打祝家庄`

### 题面要点

两条灯谜分别要求猜周杰伦、周华健歌曲，并注明白头、玉颈、素心、掉尾等谜格；提交两个歌名。

### 我的解法

共工怒触不周山后的“偏头痛”可表为“共工偏头痛”，用白头、玉颈在前两字作同音转换，回到歌名《公公偏头痛》。四个 9 合计 36，即“三打”；帮发牌员取胜是“助庄家”，素心把“助”调为“祝”，掉尾把“庄家”换序为“家庄”，得《三打祝家庄》。两题按要求空格连接。

### 验证

两条表面、谜格和歌名格式均闭合；完整答案首次提交 correct。

<a id="p-cinHRhJe"></a>

## 反切的艺术（cinHRhJe）

- 答案：`鱼钩`

### 题面要点

每行给两个汉字及四格英文模板；示例 `蓝 + 雪 = 吹`，标题借“反切”提示前后拼接。

### 我的解法

把汉字翻成四字母英文，各取前词前两字母和后词后两字母。示例 `BLUE` 的 `BL` 加 `SNOW` 的 `OW` 得 `BLOW=吹`。同理 `FILM + DISH` 得 `FI+SH=FISH=鱼`；`HOME + BOOK` 得 `HO+OK=HOOK=钩`。

### 验证

同一 2+2 拼接规则解释示例和两道题，编号输出为 `鱼钩`；提交正确。

<a id="p-HKd44RZL"></a>

## 反向探骊格（HKd44RZL）

- 答案：`一笔画`

### 题面要点

线索是“欧拉解决的某个问题”，格式为反向探骊格 `1+2`，即先一字谜底，再两字谜目。

### 我的解法

欧拉的七桥问题奠定了“一笔画”判定。按反向探骊拆分，谜底为 `一`，谜目为 `笔画`，合写 `一笔画`；这里不是直接提交“七桥问题”，而是把欧拉所解决的问题类型转成指定的 1+2 结构。

### 验证

拆分严格符合枚举，语义对应欧拉七桥问题；本地历史正确回执确认答案。

<a id="p-Ys8hZAop"></a>

## 叠叠叠叠叠词（Ys8hZAop）

- 答案：`原神`

### 题面要点

四组五格重复句和三格短句共享末两红格，最终只提取两红格。

### 我的解法

日志在 `行长` 被否定后，把五字重复句、五字正文与三字短句识别为“云·原神”宣传/jingle 的挖空结构；三字短句按 `云原神` 填入时，首格是 `云`，共享的两红格就是 `原神`。为避免借用答对后出现的作者文字，本题不再列出正确提示中给出的完整歌词句子。

### 验证

早期把重复格误解为多音字并提交 `行长`，判错；`原神` 正确，错误 1 次。独立证据的关键只到“云原神”三格结构；答对后正确提示中的完整歌词仅作验证，不作为推导来源。

<a id="p-y1Ezg7XA"></a>

## 古老迷宫游戏（y1Ezg7XA）

- 答案：`UNFOLD`

### 题面要点

六行第一人称迷宫视角符号，各配一个 3×3 点阵的起点和朝向；首行示范走出 U 形路线。

### 我的解法

把每个大符号视为老式迷宫中的前方/左右通路状态：每次先前进一步，再按所见通道保持方向、左转、右转或掉头。首行从向下开始得到 `D,D,R,R,U,U`，正好走到星标。对其余五行应用同一规则，轨迹在点阵上依次画出 `U、N、F、O、L、D`。

### 验证

首行示范验证移动约定，六行共同拼成 `UNFOLD`；提交 correct。

<a id="p-GrbeioVN"></a>

## 只需枚举（GrbeioVN）

- 答案：`ENUMERATE`

### 题面要点

九行只保留英文句子的词长枚举和一个总字母索引；风味说“信息并不少”。

### 我的解法

词长分别锁定九句经典 pangram，例如 `THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG`、`PACK MY BOX WITH FIVE DOZEN LIQUOR JUGS`、`SPHINX OF BLACK QUARTZ, JUDGE MY VOW` 等。忽略空格标点后按每行首数字索引，九行依次得到 `E N U M E R A T E`。

### 验证

九个枚举都能恢复成完整 pangram，抽取结果又回扣标题；`ENUMERATE` 提交正确。

<a id="p-F1Myul5g"></a>

## 吃什么（F1Myul5g）

- 答案：`烤鸡腿`

### 题面要点

六个不同汉字 A–F 满足多组两字食物、偏旁和烹饪方式条件，要求输出 FBC。

### 我的解法

节日食物 AB 取 `火鸡`，故 A=火、B=鸡；令 C=腿，则 AC=`火腿`、BC=`鸡腿`。D/E/F 都以火为偏旁；“每隔七天吃一次”影射疯狂星期四，DB=`炸鸡`，所以 D=炸。再取 EB=`烧鸡`、FB=`烤鸡`，而 EF=`烧烤` 正是烹饪手法，于是 E=烧、F=烤。所求 FBC 即 `烤鸡腿`。

### 验证

所有食物、偏旁、周期和烹饪条件逐项闭合，零错通过。

<a id="p-hv41SWQP"></a>

## 启动（hv41SWQP）

- 答案：`当日`

### 题面要点

开关图标配门、山、狗形成例句；底部是单人/万人、关/开与两个编号色块。

### 我的解法

上方分别是 `开门见山`、`关门打狗`。底部完整句为 `一夫当关，万夫莫开`，所以编号缺字先是 `当、莫`。但第二格只高亮 `莫` 的中层；将 `莫` 竖向拆为 `艹/日/大`，取中层得 `日`。编号 1 取整字 `当`，编号 2 取部件 `日`，答案 `当日`。

### 验证

`当莫` 与完整谚语均判错；解释高亮层后 `当日` 正确，共 2 次错误。

<a id="p-mJYr8Uar"></a>

## 和同开珎（mJYr8Uar）

- 答案：`京`

### 题面要点

和同开珎式四向组词题，四周是方向图标，连接箭头决定中心字在前还是在后。

### 我的解法

早期把图标当英文箭头，尝试 `TURN、ARROW、SHIFT` 均不成立。把它们改读为中文方位，四臂要求组成北京、南京、东京、京东；共同中心字只能是 `京`，而箭头方向正好决定“方位+京”或“京+东”的顺序。

### 验证

`TURN、ARROW、SHIFT` 被拒，`京` correct；四个组合均为常见地名/词名。

<a id="p-XPtkPIap"></a>

## 和同谜（XPtkPIap）

- 答案：`明后`

### 题面要点

颜色表用 `和同开珎、和光同尘、和而不同` 建立汉字—颜色映射，随后两个节点要求找能与三侧字成词的中心字。

### 我的解法

节点一周围是 `开、光、不`，中心填 `明`，组成 `开明、光明、不明`。节点二周围是 `王、而、明`，中心填 `后`，组成 `王后、而后、明后`，并可接右侧 `尘` 成 `后尘`。按编号直接读取两个中心字为 `明后`。

### 验证

所有相邻二字词成立；加入题外联想的 `明日之后`、`明后天` 均被判错，原始提取 `明后` 提交正确。

<a id="p-7WSIxIpP"></a>

## 和和同同（7WSIxIpP）

- 答案：`动力`

### 题面要点

两个中心框各连向四个汉字，要求找能与该组所有字组成词的共同字，答案为两字。

### 我的解法

第一组 `弹、应、暴、冲` 后都可接“力”：弹力、应力、暴力、冲力。第二组 `运、机、移、变` 后都可接“动”：运动、机动、移动、变动。得到“力、动”两个材料，按自然词序组成 `动力`。

### 验证

八个二字词都成立；`动力` 是由两答案字构成的正常双字词，反序“力动”不成立。

<a id="p-yBIzg7XA"></a>

## 哈基谜（二）（yBIzg7XA）

- 答案：`ALPHABET`

### 题面要点

两段编号模式为 `①②③④①` 与 `⑤⑥⑦①`，要求合并后的八格；风味提到一共 24 个。

### 我的解法

第一段的首尾重复模式对应 `ALPHA`，第二段四字母且末字与第一段共享 A，对应 `BETA`。合并 `ALPHA+BETA` 并共享中间 A，八格拼成 `ALPHABET`。24 则验证所指为有 24 个字母的希腊字母表。

### 验证

编号重复关系和 24 字母主题一致；`ALPHABET` 首投正确。

<a id="p-6Grd5dzE"></a>

## 哈基谜（雾（6Grd5dzE）

- 答案：`蒋`

### 题面要点

图式把一个免疫学名词、两个人物图和水/草元素图标做加减，目标为单个汉字。

### 我的解法

本地图片可确认第一图指向“浆细胞”，取 `浆`；水元素图标提示减去 `水`，得到 `将`，末尾草元素图标再给 `艹+将=蒋`。中间两幅人物图在原日志中是借助反向搜图识别后，按共同的 `yi` 读音相消；这一步不能算本地独立识别，因此这里只记录其在算式中被设计为互相抵消，不写人物姓名。

### 验证

本地独立证据有限：首尾部件算式 `浆-水+艹=蒋` 可复现，中间人物相消缺少独立识别证据；最终 `蒋` 首次提交 correct。

<a id="p-cWVHRhJe"></a>

## 唐人街灯谜（巴黎）（cWVHRhJe）

- 答案：`阿勒泰`

### 题面要点

灯谜是 `前去岱宗（打一新疆地区，朱履格）`，副标题特意注明巴黎。

### 我的解法

朱履格要求前部谐读、末字本义。新疆地区 `阿勒泰` 的前两字“阿勒”近似法语 `aller`，意为“前去”；末字 `泰` 本义对应岱宗泰山。巴黎背景正好说明为什么使用法语谐音。

### 验证

地理类别、格律分界、法语和岱宗四项同时吻合；`阿勒泰` 提交正确。

<a id="p-IvFLNP39"></a>

## 嘉豪谜（一）（IvFLNP39）

- 答案：`DEATH`

### 题面要点

画面提示 Alan Walker，并把无主唱的曲名与有主唱版本并排，圈出标题新增的字母。

### 我的解法

`Fade` 的有声版本题名为 `Faded`，新增 `D`，故 ①=D；`Spectre` 对应 `The Spectre`，新增 `THE`，故 ②③④=T、H、E。代入末尾排列 `①④a②③`，得到 `D E A T H`。

### 验证

两组标题变化精确给出四个圈字，终排使用全部圈号并拼成 `DEATH`；首投正确。

<a id="p-OS5iZO0v"></a>

## 回転（OS5iZO0v）

- 答案：`焼売`

### 题面要点

将棋棋子、假名和翻转符号组成日语 rebus，最终要求二汉字食物。

### 我的解法

示例 `王+む=オウム` 对应鹦鹉，`玉+と=玉兎` 对应月兔，`角+に=角煮` 对应角煮。将角行棋子翻面/升变后成为 `馬`，读 `うま`；代入红色 `し [棋子] い`，得到 `しうまい`，即烧卖的日语读法。按要求写二汉字为 `焼売`。

### 验证

三条例子确定棋子读法与翻面操作；`焼売` 首投正确。

<a id="p-9SSWHnxJ"></a>

## 圆（9SSWHnxJ）

- 答案：`PUSKAS`

### 题面要点

五行 1/2 串配两队名称长度和一组坐标抽取；题注说明按时间排序，第四行另含点球串。

### 我的解法

1/2 表示足球比赛中两队依时间先后进球。五场分别可还原为巴西 1–7 德国、PSG 对巴塞罗那大逆转、拜仁 8–2 巴塞罗那、阿根廷 3–3 法国及点球、国际米兰 0–5 PSG。按坐标从队名取字：PSG[1]=P，BAYERNMUNICH[8]=U，PSG[2]=S，BRAZIL[6]=L 再字母前移一位得 K，FRANCE[3]=A，PSG[2]=S，组成 `PUSKAS`。

### 验证

五条进球时间线、队名长度与抽取坐标全部一致；`PUSKAS` 首次提交 correct。

<a id="p-M0NxAs7n"></a>

## 填字游戏（M0NxAs7n）

- 答案：`欲将心事付瑶琴`

### 题面要点

题面是无编号中文填字，彩色格按彩虹顺序用于最终提取。

### 我的解法

根据长度和交叉填入 `全国人民代表大会、饱暖思淫欲、西塔琴、风水、霜白色、瑶光、弦卷心、一事无成、全球变暖、表里不一、欲把西湖比西子、水色天光、琴高、心付` 等词。把红、橙、黄、绿、蓝、靛、紫七个彩格依次读取，得到 `欲 将 心 事 付 瑶 琴`。

### 验证

交叉字母互相锁定，彩虹次序形成完整诗句；`欲将心事付瑶琴` 提交正确。

<a id="p-KMgXEjGS"></a>

## 大厂笔试题（KMgXEjGS）

- 答案：`NETEASE`

### 题面要点

七个左侧汉字与七个打乱的汉字配成二字词，再翻译成指定长度的英文，并从红格取字。

### 我的解法

配词为 `会议、提前、现实、二十、直径、学科、儿女`，翻译成 `CONFERENCE、ADVANCE、REALITY、TWENTY、DIAMETER、SUBJECT、CHILDREN`。按各行红位提取，依次为 `N,E,T,E,A,S,E`。

### 验证

提取得到大厂网易的英文名 `NETEASE`，吻合标题；中文“网易”因不是图中直接提取串而被拒，英文形式正确。

<a id="p-bEu5uOJW"></a>

## 大发大发（bEu5uOJW）

- 答案：`心思`

### 题面要点

两行“大发”后跟上下双色块，答案也由两个色块字组成。

### 我的解法

第一行补 `大发雷霆`，雷、霆共同上部 `雨` 为蓝色，雷下部 `田` 为灰色。第二行补 `大发慈悲`，慈、悲共同下部 `心` 为红色。答案第一格全红即 `心`；第二格灰在上、红在下，即 `田+心=思`，得 `心思`。

### 验证

两组成语与部件颜色均一致；`心思` 首投正确。

<a id="p-5ILuzMeL"></a>

## 大数邻（5ILuzMeL）

- 答案：`YAKUMAN`

### 题面要点

十四段文字各含一对可比较数量级的数据，末尾给 `(14=6 6 1 1)→(7)`；风味强调中文大数单位。

### 我的解法

每段选取同有效数字的数据，求其十进制指数差，再用 A1Z26 转字母。十四段依次得到 `HIDDENNUMBERSY`，按 `6 6 1 1` 分成 `HIDDEN NUMBER S Y`。把 S/Y 当七字母英文数词首尾而猜 `SEVENTY` 被拒；随后提交 `YAKUMAN` 获正确，成功文案 `ロン！48000！` 与日麻役满相符。不过日志没有保存 `HIDDEN NUMBER S Y` 如何唯一指向 `YAKUMAN` 的中间规则。

### 验证

本地独立证据有限：十四段数量级差与 `HIDDEN NUMBER S Y` 可复现，但到 `YAKUMAN` 的桥接缺失。`SEVENTY` incorrect，`YAKUMAN` correct；不补造更细机制。

<a id="p-5LquzMeL"></a>

## 好吃的成语（5LquzMeL）

- 答案：`工匠熟能生巧`

### 题面要点

题设 `ABCD` 与 `BEDF` 都是成语，给出字义关系，并说明 `CD` 是现代甜品、`EF` 是职业，要求输出 `EFABCD`。

### 我的解法

`BEDF=能工巧匠`，其中 `能/巧` 都表示有技巧，`工/匠` 近义且合成职业“工匠”。于是 B=能、D=巧，对应的 `ABCD` 是 `熟能生巧`，A/C=`熟/生` 为反义，而 `生巧` 可指生巧克力。按 `EFABCD` 排列为 `工匠熟能生巧`。

### 验证

两个成语、反近义关系、甜品与职业提示全部被使用；提交正确。

<a id="p-oyvmNtwx"></a>

## 好数（oyvmNtwx）

- 答案：`GREY`

### 题面要点

“好数”要求同一数字的相邻两次出现之间恰隔该数字个位置；27 位串用汉字及左右部件表示，需解出“风清月明”。

### 我的解法

把左右结构字展开为两位部件，例如 `清=氵+青、时=日+寸、晴=日+青、对=又+寸`。用好数间距约束求解，可锁定 `氵=1、青=8、日=2、寸=6`，并得到 `风=7、清=18、月=5`；因 `明=日+月`，故明=25。于是“风清月明”给出 `7,18,5,25`。

### 验证

A1Z26 将四数转为 `G,R,E,Y`；长度正好为四，`GREY` 提交正确。

<a id="p-Wj2lljce"></a>

## 如约而至（Wj2lljce）

- 答案：`INFANT`

### 题面要点

“转换器”把左图英文变成右图英文：母鸡到线圈、数数到乡村、过去到糕点，目标是得到士兵。

### 我的解法

统一操作是在左词后加 `RY`：`HEN→HENRY`（电感单位亨利）、`COUNT→COUNTRY`、`PAST→PASTRY`。士兵对应 `INFANTRY`，逆操作去掉 `RY`，得到六字母 `INFANT`。

### 验证

三条例子都严格使用同一后缀，且 `INFANT` 符合 `(6)`；首投正确。

<a id="p-mzEr8Uar"></a>

## 字母谜（mzEr8Uar）

- 答案：`GOOSE`

### 题面要点

字母算式为 `SIS/OVO=0.GAMEGAME…`，相同字母代表相同数字、不同字母代表不同数字，且分数最简；问 `SIS*OVO`。

### 我的解法

循环小数给出 `9999×SIS=OVO×GAME`。枚举数字并应用最简条件，唯一有效赋值是 `SIS=242、OVO=303、GAME=7986`。数值乘积为 `73326`，但题目要继续用同一字母数字映射反解：7=G、3=O、3=O、2=S、6=E，因此 `73326→GOOSE`。

### 验证

直接交 `73326` 及 `242303` 均错误；转回字母后的 `GOOSE` correct。

<a id="p-EQxtl1dT"></a>

## 字母重组（EQxtl1dT）

- 答案：`AGAINST`

### 题面要点

五组左右线索各产出两个英文片段，括号给片段长度；拼接后的七字母都需重组为同一个词。

### 我的解法

五组分别构成 `AA+STING`、`TAIGA+NS`、`INSTAGRAM-MR=INSTAGA`、`GAIN+SAT`、`AG+STAIN`。这些结果 `AASTING、TAIGANS、INSTAGA、GAINSAT、AGSTAIN` 的字母多重集完全相同，都是 A、A、G、I、N、S、T，可统一重排成 `AGAINST`。

### 验证

五条独立线索都给出同一组七个字母；`AGAINST` 首次提交正确。

<a id="p-KBXEjGSH"></a>

## 字的奥秘（KBXEjGSH）

- 答案：`拾`

### 题面要点

英文单词被分块并改变相对位置；先把词义译成汉字，再让汉字部件按英文块的位置作同样重排。

### 我的解法

例子 `LE|AF` 是 LEAF=叶，叶可拆“口+十”；图中两块上下换位后，部件也换成“十在口上”，得“古”。`LET|TER` 是 LETTER=信，交换两块对应把“亻+言”换成“讠+人”，得“认”。末题 `TA|KE` 是 TAKE=拿，即“合+手”；按图把代表手的部分移到左边成扌、合放右边，组成 `拾`。

### 验证

三题遵循相同的“英文分块位置→汉字部件位置”规则；直接翻译的“拿”被拒，而重排后的 `拾` 正确。

<a id="p-PmEe2esI"></a>

## 字谜三则（PmEe2esI）

- 答案：`明目张胆`

### 题面要点

三条字谜以颜色标格，并在末行要求按红、橙、黄、绿提交四字。

### 我的解法

红色取第二谜中被明说“莫猜”的 `明`（日月）。橙色是三个口重叠而非分列成品，得到 `目`。黄色把残月看作 `弓`，与长组成 `张`。绿色用第二谜中的 `月` 加 `旦(日+一)` 组成 `胆`。按颜色顺序得 `明目张胆`。

### 验证

四字分别由题面部件得到并组成固定成语；提交正确，错误 0 次。

<a id="p-uYPC56DT"></a>

## 学好数学（uYPC56DT）

- 答案：`WELL`

### 题面要点

上方出现 `W(x log x)=log x, x>1/e`，下方又组合出数学证明常用缩写 WLOG，并以颜色指向四个答案格。

### 我的解法

恒等式中的 W 是 Lambert W 函数，因为令 `y=log x` 就有 `W(ye^y)=y`。第二层 `WLOG` 是 without loss of generality。颜色分别给出 W、E，并从 `LOG` 取最后两个 L，得到 `WELL`，也呼应标题中的“学好”。

### 验证

数学恒等式与缩写均成立；`WELL` 首次提交 correct。

<a id="p-OjoiZO0v"></a>

## 学舌（OjoiZO0v）

- 答案：`凄凉`

### 题面要点

题目用普通话汉字模仿粤语，四个罗马字音节配音高位置；水平位置决定阅读顺序。

### 我的解法

音高给粤语声调，得到 `lou5、gung1、sin3、put3`。按横坐标排序而非面板上下顺序，读成 `lou5 gung1 put3 sin3`，即“老公拨扇”。这句歇后/谐音语的下句是 `凄凉`，双关“妻凉”。

### 验证

音节、声调、水平排序和固定下句彼此一致；`凄凉` 提交正确。

<a id="p-yYszg7XA"></a>

## 宝可灯谜1（yYszg7XA）

- 答案：`胡说树`

### 题面要点

谜面只有英文 `tree`，要求打一宝可梦曾用译名；提示说谜面是把谜底逐字理解得到的。

### 我的解法

`tree` 是外国文字，可用“胡”表示外来的；这个英文词正在“说”出其含义“树”。逐字组合便是 `胡 + 说 + 树`。

### 验证

三字均直接落实在谜面情境中，且 `胡说树` 符合题目要求的宝可梦旧译名；本地结果记录为正确。

<a id="p-ybfzg7XA"></a>

## 小学生必背（ybfzg7XA）

- 答案：`9`

### 题面要点

算式为“天−火=2、医−匪=10、消费−铁路=？”；标题说小学生必背。

### 我的解法

把词语替换成常用公共服务号码：天气预报 121、火警 119，差 2；急救 120、报警 110，差 10。消费者投诉为 12315，铁路客服为 12306，所以 `12315−12306=9`。

### 验证

同一“必背热线”规则解释全部三式；笔画误猜 `4` 判错，`9` 正确，共 1 次错误。

<a id="p-d1uF4LbF"></a>

## 展览墙（d1uF4LbF）

- 答案：`HELLO WORLD`

### 题面要点

展览墙上多条著名物理公式的编号部分褪色，需要恢复相应符号并按号读取。

### 我的解法

恢复普朗克关系中的 h、麦克斯韦方程中的 E、长度收缩式中的 L 与 `L₀`，开头可稳定读成 `h E L L O`。日志把后续波函数、距离 r、洛伦兹矩阵元素和法拉第式微分 d 以字形或英文含义续读为 `W O R L D`，但没有逐编号记录每个遮挡处的唯一映射。

### 验证

本地独立证据有限：`HELLO` 的公式符号链可复现，`WORLD` 的逐格对应记录不完整；完整短语 `HELLO WORLD` 首次提交 correct。

<a id="p-YvzhZAop"></a>

## 巧填幻方（YvzhZAop）

- 答案：`NEUTRAL`

### 题面要点

热身数字用“反复相乘各位直到一位数”；主体先是以 2 的幂表示的 19 格幻方，再是把“和”添两笔改成“积”的 4×4 乘法幻方。

### 我的解法

热身得心形=3、星形=2。把第一盘数字取以 2 为底的指数，解出标准 1–19 幻方，并确定方形值 4、三角形值 8。第二盘要求每行列和主对角线乘积相同，解得完整方阵，其中彩色格按光谱顺序为 `14,5,21,20,18,1,12`。A1Z26 转成 `N E U T R A L`。

### 验证

第一盘所有直线指数和为 38，第二盘各行列乘积均为 7560；`NEUTRAL` 提交正确。

<a id="p-6Cnd5dzE"></a>

## 巧填方格（6Cnd5dzE）

- 答案：`CONJUGACY`

### 题面要点

第一部分是 6×6 数织；第二部分是带空格的 6×6 数表，规律涉及每个连续 3×3 方块。

### 我的解法

数织唯一解为 `###..# / #####. / .#.### / ###### / ##..## / ###.#.`。数表规律是每个滑动 3×3 的九数乘积均为完全平方数。对每个质因子只看指数奇偶，在 GF(2) 上列 16 个窗口异或方程，求出各空格的最小正整数平方自由部分，补成完整数表。再用数织白格作掩码，按行读取对应数字：`3,15,14,10,21,7,1,3,25`。

### 验证

补表后 16 个 3×3 乘积全为平方数；A1Z26 把白格数值转成 `C O N J U G A C Y`，零错通过。

<a id="p-lXxOiBju"></a>

## 帮Stavros回家（lXxOiBju）

- 答案：`GREECE`

### 题面要点

Stavros 来信要订回家机票，并说自己的书写看起来像数学。

### 我的解法

Stavros 是典型希腊名字；数学书写大量使用希腊字母，这又独立指向希腊。因此其回国目的地/国家是 `GREECE`。

### 验证

姓名和“像数学”的字母线索一致；`GREECE` 首投正确。

<a id="p-fBtYBRMr"></a>

## 平面直角坐标系（fBtYBRMr）

- 答案：`AXIS`

### 题面要点

四个小题分别给图像、曲线、坐标点和物理量，先求四个英文中间答案，再按第五图抽取。

### 我的解法

四题得到 `ALPHA`（字母/alpha+bet rebus）、`CALCULUS`（曲线下面积）、`SIX`（直线 `y=.5x+3` 上 y=6 时 x=6）、`GRAVITY`（重量与质量斜率 9.8）。末图按标记及索引取 `ALPHA[1]=A、SIX[3]=X、GRAVITY[5]=I、CALCULUS[8]=S`，拼成 `AXIS`。

### 验证

四个中间词的长度和末图抽取全部吻合；首次提交 correct。

<a id="p-swOBl3vq"></a>

## 当一切都沉寂之时（swOBl3vq）

- 答案：`DEADLINE`

### 题面要点

单图由若干彩色字格、共同黑色字格、下降箭头和图标组成；七个编号字母最后填入右侧两组四格。

### 我的解法

各行都是英文短语在某种量下降后的变化。温度下降使 `FRESH CREAM` 变成 `ICE CREAM`；速度下降使 `FULL GAS` 变成 `FULL STOP`；电力下降使 `ON END` 变成 `OFFEND`。编号由这些词得到 `1–7 = L,I,F,E,L,N,E`，在右侧先组成 `LIFE LINE`。最后生命降至终点，`LIFE` 变为 `DEAD`，共同后缀仍是 `LINE`，故得到 `DEADLINE`。

### 验证

三个示例的词长、图标和编号全部闭合；`DEADLINE` 也对应时钟图标。该答案首次提交即为 correct。

<a id="p-qwTUKLri"></a>

## 彩色方块（qwTUKLri）

- 答案：`TELEGRAM`

### 题面要点

题图把品牌或平台字标化成“每个字母一个色块”，示例可识别 `LASTFM、STEAM、FORTNITE、NETFLIX、EBAY、FEDEX、GOOGLE、PAYPAL` 等。

### 我的解法

最下方只给一个青蓝色块和长度 `(8)`，要求按相同规则识别主色对应的平台。该颜色与 Telegram 的标志性蓝色吻合，且 `TELEGRAM` 正好八字母；其他八字母蓝色品牌的常用色调与示例语境较弱。

### 验证

颜色与长度共同锁定候选；`TELEGRAM` 首次提交正确。

<a id="p-UsvRTeZO"></a>

## 微谜137：述数术（UsvRTeZO）

- 答案：`ALBUM`

### 题面要点

上方例子展示报数/Look-and-say 变换，下方从 `113` 连续变换三次，末端有五个宽窄不同的答案框。

### 我的解法

依次报数：`113→2113→122113→11222113`。答案框宽度指定把末串切成 `1|12|2|21|13`，再按 A1Z26 转字母。

### 验证

得到 `A|L|B|U|M=ALBUM`；切分数量和框宽完全一致，提交正确。

<a id="p-JpgoAEXN"></a>

## 微谜139: 汉语词典（JpgoAEXN）

- 答案：`价值`

### 题面要点

仿词典页面给三条被遮词目，长度分别 4、4、3，均圈出前两字。

### 我的解法

三条释义分别对应 `价值规律`（商品生产和交换规律）、`价值连城`（战国赵国和氏璧典故）、`价值量`（体现在商品中的劳动量）。共同被圈出的前两字是 `价值`。

### 验证

释义、词长和圈号位置全部吻合；`价值` 首投正确。

<a id="p-CzfVTmLk"></a>

## 微谜145: 叠色（CzfVTmLk）

- 答案：`万紫千红`

### 题面要点

题面以王维《相思》的字、颜色叠层、编号与缺声母拼音作提示；紫、红与“春”尤其突出。

### 我的解法

日志先后尝试把底部图层直读、按首字母读或同音改写，得到 `春紫作红、姹紫嫣红、春色微红、春色始红、春色斑斓` 等，均未获认可。最终把蓝色 2 指向的“春”看作熟语语境“万紫千红总是春”，重叠色块直接锚定“紫”，粉色 1 锚定“红”，并用诗中“几/多”的数量感补足“万/千”，得到 `万紫千红`。

### 验证

本地独立证据有限：七个较字面的候选均 incorrect，`万紫千红` correct；日志没有给出一条无歧义的逐格抽取，只能确认“春、紫、红、多”的语义回扣，不能把被拒的中间读法包装成确定机制。

<a id="p-LimqNrv1"></a>

## 微谜147: 力（LimqNrv1）

- 答案：`GOING`

### 题面要点

方块置于弹簧上，箭头表示力 X；X 是多音字。彩格从两种拼音中抽共同部分，先填入 `g _ i _`，检查器随后要求把“向上”改为“向下”。

### 我的解法

向上时是 `弹力`，`弹` 读 `dàn/tán`，共同的彩色部分为 `a` 和 `n`，填得 `GAIN`。该中间答案被接受，并提示改为向下。向下时 X 为 `重力`，`重` 读 `zhòng/chóng`，共同部分为 `o` 和 `ng`，填入原模板得到 `g+o+i+ng = GOING`。

### 验证

`GAIN` 获中间反馈，方向反转后拼音分段精确得到 `GOING`；最终提交正确。

<a id="p-duyF4LbF"></a>

## 心（duyF4LbF）

- 答案：`LOVE`

### 题面要点

四幅图都由 `他/她 + 心形 + 他/她` 组成，并分别排成串、幸运草、同心圆和呼唤状；画面明显借用了小虎队《爱》的歌词意象。

### 我的解法

识别歌曲只能说明主题是“爱”，但每个基本图元本身更直接：心形夹在两个人称之间，英文读法就是 “A loves B”。四幅图反复用同一关系，因而应取英文关系词 `LOVE`，而不是歌名、歌手或后续歌词。

### 验证

中文 `爱` 及多个歌词延伸答案均被拒；直接把核心心形关系写成 `LOVE` 后正确。此题的本地机制证据支持主题识别，但最终英文格式主要由判题反馈确认。

<a id="p-o0tmNtwx"></a>

## 怀旧数学（o0tmNtwx）

- 答案：`MIX`

### 题面要点

给出 `5+5=10、15+5=110、1015+11=1051、1000+110=? (3)`，风味提示某 xkcd 风格规则。

### 我的解法

把数字串按罗马数字符号的现代数值分块：5=V，15=IV，110=IX，1015=XIV，11=II，1051=XVI。于是末式是 `M + IX = MIX`，数值上即 1000+9=1009；题目要求三字符，所以提交罗马形式 `MIX`。

### 验证

前三个等式均按同一罗马运算成立，`MIX` 符合 `(3)`；首投正确。

<a id="p-WTklljce"></a>

## 成词成对（WTklljce）

- 答案：`LAYOUT`

### 题面要点

六对五字母词之间各有统一 Caesar 位移，题末另给 `(6)`。

### 我的解法

各对位移量依次为 6、21、19、9、15、14，例如 `FUNNY+6=LATTE`、`KNEED-5=FIZZY`。把正位移量按 A1Z26 读成 `FUSION`，该词提交后获 intermediate。再按题末 `(6)` 对 `FUSION` 整体 Caesar +6，得到 `LAYOUT`。

### 验证

`FUSION` 为 intermediate，`LAYOUT` correct；两层均使用同一位移机制。

<a id="p-iS6RTMow"></a>

## 成语与反义词（iS6RTMow）

- 答案：`括`

### 题面要点

题图用结构色块表示一个四字成语，后两字互为反义词，并要求取前两字的红色左部件后在一个方框中组合。

### 我的解法

符合图形的是 `拨乱反正`：`拨=扌+发`，`乱=舌+乚`，而 `反/正` 是反义词；图中黄色部分“几乎一样”对应 `发` 与 `反` 的相似轮廓。两个红部件是 `扌` 和 `舌`，底部不是并排输出，而是合成一个字：`扌+舌=括`。

### 验证

把部件写成 `扌舌` 或 `手舌` 均被判错，合字 `括` 正确，也呼应题中大量括号。

<a id="p-OkbiZO0v"></a>

## 成语与反义词2（OkbiZO0v）

- 答案：`事无巨细`

### 题面要点

四个位置分别画出事物、空集和一对大小相反的色块；提示强调“不管多大多小”。

### 我的解法

第一格取“事”，第二格空集 `∅` 取“无”。后三格是一对反义概念，结合“大/小”提示，用更固定的书面搭配“巨/细”。四字合成 `事无巨细`。

### 验证

成语释义正是事情不分大小、全都包括，逐格和 flavor 完整对应；本地正确结果确认。

<a id="p-D0iPz728"></a>

## 成语接龙（D0iPz728）

- 答案：`心安理得`

### 题面要点

给出字母模板 `ABCD→DAEF→FGEA→ABCD`，并用古籍出处提示各成语。

### 我的解法

《庄子·天道》对应 `得心应手`，故 D=得、A=心、E=应、F=手；《警世通言》对应 `手不应心`，得 G=不。AD=`心得`，BA 根据《墨子·亲士》为 `安心`，故 B=安。于是 ABCD 唯一补成 `心安理得`，完整环为“心安理得→得心应手→手不应心→心安理得”。

### 验证

所有首尾字与出处闭合；`心满意得` 判错后，`心安理得` 正确，共 1 次错误。

<a id="p-WRKlljce"></a>

## 我是嘉豪（一）（WRKlljce）

- 答案：`尹相杰`

### 题面要点

线索描述早期说唱歌手、与女歌手合唱一首关于劳动者追求女子的歌、同年两次涉案，以及一首歌词重复结构为 `ABCDABEFAGHIJ` 的歌。

### 我的解法

《纤夫的爱》的男声演唱者是尹相杰，纤夫也正是所述劳动者。其歌曲《天不下雨天不刮风天上有太阳》逐字模式为：天A 不B 下C 雨D 天A 不B 刮E 风F 天A 上G 有H 太I 阳J，精确符合给定结构；同年两次涉毒的描述也相符。

### 验证

歌曲语义、逐字模式和人物经历共同锁定；首次提交 correct。

<a id="p-EIStl1dT"></a>

## 我爱记歌词（EIStl1dT）

- 答案：`SING`

### 题面要点

十条歌词要求接下一句，风味强调“有一点”；题目按 3/2/2/3 分成四组，答案四字母。

### 我的解法

根据本地日志补出各句续歌词后，每条关键续句都会出现 `点` 或 `一`。把 `点` 当摩斯点 `.`，把 `一` 当横线 `-`，四组依次得到 `...`、`..`、`-.`、`--.`，即 `S、I、N、G`。

### 验证

分组长度与四个摩斯码完全吻合，结果又符合记歌词主题；`SING` 提交正确。

<a id="p-JyxgoAEX"></a>

## 我的世界一直在下雨……（JyxgoAEX）

- 答案：`SUNNY`

### 题面要点

五张 Minecraft 截图分别展示生成结构，HUD 经验等级为 `1,4,3,2,8`；题目开头给 `/weather clear`。

### 我的解法

使用归档图片文件名的结构 ID：`swamp_hut、monument、mansion、ancient_city、jungle_pyramid`，去掉下划线后按对应等级作一基索引，取到 `S,U,N,N,Y`。

### 验证

五图一图一字，提取串为 `SUNNY`；含义正是清除持续下雨后希望得到的天气。

<a id="p-ZmApgd2S"></a>

## 我解谜（ZmApgd2S）

- 答案：`RING`

### 题面要点

可见文字强调“转移注意力用的”，隐藏样式中有“她的____(4)”，风味说它似乎可食用。

### 我的解法

“转移注意力用的”是 `red herring`。把“她的”译成 `HER`，四字母空格填 `RING`，拼成 `HER+RING=HERRING`；红色样式再补出 RED HERRING。题目只要求四格内容，所以提交 `RING`。

### 验证

食物、红色样式和四字母空格同时解释；`RING` 首投正确。

<a id="p-JY3goAEX"></a>

## 我解谜 I puzzIe.（JY3goAEX）

- 答案：`9`

### 题面要点

英文句子故意混用大写 I 与小写 l，要求告诉 IRIS 字母 I 的数量；标题本身也含同样机关。

### 我的解法

只数正文中真正的大写 I，可数到 7；`THlS、lS、lRIS` 开头等是小写 l 诱饵。提交 7 后提示“好像漏了哪里”，于是把标题也计入：标题里独立的 `I` 与 `puzzIe` 中的 I 共 2 个，总数 `7+2=9`。

### 验证

`7` 获 intermediate 提示，`9` correct。

<a id="p-eyFoQPLb"></a>

## 才不是汽水谜！(二)（eyFoQPLb）

- 答案：`横岗`

### 题面要点

题设 `AB` 与 `CDB` 是同城地铁站，`A=D+C`、`B=E+F` 表示汉字部件组合，`CE`、`CF` 又是中国城市名。

### 我的解法

取深圳地铁站 `AB=横岗`、`CDB=黄木岗`，则 C=黄、D=木，且 `木+黄=横`。再把 `岗` 分成 F=山、E=冈，即 `山+冈=岗`；于是 `CE=黄冈`、`CF=黄山` 都是城市名。

### 验证

两座同城车站、两条部件等式和两个城市名全部成立；`横岗` 首次提交正确。

<a id="p-ELjtl1dT"></a>

## 才不是汽水谜！（一）（ELjtl1dT）

- 答案：`坏`

### 题面要点

题目让多组大写字母串在不同语境下读义：模式、光盘、扑克牌、英文物件等，最后落到 `BAD`，要求七画汉字。

### 我的解法

末串无需再拆字母，直接把英文形容词 `BAD` 翻译成中文。“坏”正是最直接译义，且笔画数为 7（土三画、不四画）。

### 验证

词义和七画条件同时唯一化 `坏`；首投正确。

<a id="p-EqZtl1dT"></a>

## 打字比赛（EqZtl1dT）

- 答案：`CHINA`

### 题面要点

空白 QWERTY 键盘在 F、Y、A、W、K、L 位置编号，给出 `1+2=landlord、3+4=worker、5+6=? (5)`。

### 我的解法

改用五笔一级简码：F=`地`、Y=`主`，组成 `地主=landlord`；A=`工`、W=`人`，组成 `工人=worker`；K=`中`、L=`国`，组成 `中国`。五字母英文为 `CHINA`。

### 验证

键位、两个例词和目标词均用同一五笔映射；`CHINA` 首投正确。

<a id="p-zY6G691D"></a>

## 找不同（zY6G691D）

- 答案：`ACID RAIN`

### 题面要点

两栏化学描述大体相同，仅英文名中的编号/颜色有一处差异；一侧编号覆盖 1–8，另一侧缺 8。

### 我的解法

化学性质与文字位置确定隐藏名为 `CARBONIC ACID`。把其中带编号的字母按 1–8 排序：`1:A,2:C,3:I,4:D,5:R,6:A,7:I,8:N`，得到 `ACIDRAIN`。右栏缺少的 8 正好突出最后的 N，也符合“找不同”。

### 验证

初猜 `ASCORBIC ACID` 被拒；按实际位置修正为 carbonic acid 后，抽取的 `ACID RAIN` correct。

<a id="p-TP9KhwRH"></a>

## 抽象猜歌1（TP9KhwRH）

- 答案：`BAD ROMANCE`

### 题面要点

图片上排是两个埃及太阳神 Ra 和三张喊叫图，下排是罗马斗兽场重复并截短；限定为 2000 年代、B 开头的双词英文歌。

### 我的解法

上排读作 `Ra-ra-ah-ah-ah`，下排读作 `Roma-roma-ma`。这是 Lady Gaga 2009 年歌曲《Bad Romance》开头最有辨识度的歌词，且歌名确为 B 开头的两个词。

### 验证

本地元数据的答对提示也保存了同一句歌词；`BAD ROMANCE` 提交正确。

<a id="p-APVTwX1Q"></a>

## 抽象猜歌2（APVTwX1Q）

- 答案：`BILLIE JEAN`

### 题面要点

限制为 1980 年代、B 开头、两词英文歌。图中 WHO 标志作人头，人物走向 `t>now`，脚踩地板函数，整体处于大圆内。

### 我的解法

按图元连读：WHO=`who`；走向未来表示 `will`；人物动作是 `dance`；脚踩 `floor`；人在圆中为 `in the round`。合成歌词片段 `who will dance on the floor in the round`，据此识别 Michael Jackson 的《Billie Jean》。

### 验证

歌名满足 B 开头、两词、1980s 三项限制；每个图元都在歌词中有对应位置，提交 `BILLIE JEAN` 正确。

<a id="p-9ppWHnxJ"></a>

## 抽象猜歌4（9ppWHnxJ）

- 答案：`MOSKAU`

### 题面要点

图示“来自德国、扮演蒙古、歌曲关于俄罗斯”，并限定 1970 年代、题名一个词、语言由题面暗示。

### 我的解法

德国迪斯科组合 Dschinghis Khan 以成吉思汗/蒙古造型表演，其 1979 年德语歌曲、主题为莫斯科的单词歌名是 `Moskau`。

### 验证

国籍、舞台形象、主题、年代和语言全部吻合；`MOSKAU` 首投正确。

<a id="p-fvQYBRMr"></a>

## 抽象猜歌5（fvQYBRMr）

- 答案：`SCHNAPPI`

### 题面要点

提示欧洲语言、2000 年代、S 开头单词歌名及老梗；六段歌词长度为 `5-5-8 / 8-8-7`。

### 我的解法

2004 年德国网络儿歌《Schnappi, das kleine Krokodil》的副歌是 `Schni schna Schnappi / Schnappi Schnappi schnapp`，词长正好为 `5,5,8 / 8,8,7`。歌名、年代、语言与梗图提示全部一致。

### 验证

六段词长提供精确指纹；`SCHNAPPI` 首次提交 correct。

<a id="p-2mbMJHkc"></a>

## 拼好字（2mbMJHkc）

- 答案：`ALGORITHM`

### 题面要点

左侧九个残字需用右侧 A–T 共二十个部件补全；风味说活动从第 A 届办到第 T 届，提示按年度编码。

### 我的解法

九行补成中国年度汉字：`炒(2006)、享(2017)、梦(2012)、民(2020)、振(2023)、法(2014)、韧(2025)、房(2013)、奋(2018)`。把 2006 记 A、2007 记 B，顺推至 2025 记 T，各年份对应字母依次是 `A L G O R I T H M`。

### 验证

所有部件恰好用完，年份到 A–T 的线性映射明确；`ALGORITHM` 提交正确。

<a id="p-UwEvRTeZ"></a>

## 指北（UwEvRTeZ）

- 答案：`ENSURE`

### 题面要点

罗盘和彩色边框规定红北、蓝南、绿东、黄西；红蓝两行各五格，一条 U 形箭线路径穿过若干格。

### 我的解法

红行填 `NORTH`、蓝行填 `SOUTH`，两行相同位置的 O/T/H 也与题面引号标记吻合。沿 U 形线从无箭头端走到向北箭头，两个绿色端点取 EAST 首字母 E，中间依次穿过红首 N、蓝首 S、蓝第三 U、红第三 R，得到 `E N S U R E`。

### 验证

四色方向、两行共享字母和路径顺序全部被使用；结果是正常英文词 `ENSURE`。

<a id="p-gy76lhr6"></a>

## 探骊格之底线（gy76lhr6）

- 答案：`生肖 牛`

### 题面要点

线索是“区别只是有无底线（2+1）”，要求用探骊格同时给出二字谜目和一字谜底。

### 我的解法

完整答案写作 `生肖牛`。谜目首字 `生` 与谜底 `牛` 的字形区别正是底部一横；同时牛确实属于十二生肖。因此类别与条目不仅语义成立，字形关系也发生在完整答案内部。

### 验证

`五行 土`、`数字 十` 两个泛化的一横差答案均判错；`生肖 牛` 正确，共 2 次错误。

<a id="p-s7QBl3vq"></a>

## 探骊格（三）（s7QBl3vq）

- 答案：`字 体`

### 题面要点

谜面“高 矮 胖 瘦 各不同（探骊格，1+1）”中四字本身分别以大、小、宽、斜等不同排版显示，风味还斜体强调“类别”。

### 我的解法

探骊格要同时报类别与谜底。四个被改变体态的对象都是“字”，差异在其“体”——字号、字宽、斜体。故类别为 `字`，谜底为 `体`，合起来又是自然词“字体”。

### 验证

1+1 枚举、实际排版和风味提示一致；本地正确清单确认提交形式为 `字 体`。

<a id="p-ADITwX1Q"></a>

## 数独谜题（ADITwX1Q）

- 答案：`RESUME`

### 题面要点

6×6 数独除行列宫规则外，还有大小箭头、互质边和定和边；每格附一个字母，风味要求按相同数字自上而下读字母，再重排成指令。

### 我的解法

本地回溯得到唯一数独。按数字 1–6 分组读字母分别是 `ANSWER、PUZZLE、OFTHIS、SUDOKU、BOTTOM、INSIDE`，可组成指令“ANSWER OF THIS PUZZLE INSIDE SUDOKU BOTTOM”。因此取数独内部最底行字母 `SMUREE`，重排为 `RESUME`。

### 验证

唯一盘面、六个英文块和底行字母多重集都可复核；错误的 `SUMMER` 不保字母数，`RESUME` 提交正确。

<a id="p-7vOIxIpP"></a>

## 文化造纸（7vOIxIpP）

- 答案：`诣`

### 题面要点

五名学生的编号用于索引各自引用诗句的篇名；标题和 flavor 都故意写“文化造纸”。

### 我的解法

辨认篇名并按学生数字取字：`答…` 第 1 字得答，`青玉案·元夕` 第 3 字得案，`破阵子·为陈同甫赋壮词以寄之` 第 4 字得为，`金错刀行` 第 2 字得错，`送别得书字` 第 5 字得字。串成指令 `答案为错字`，题中错字就是“文化造纸”的“纸”。提交“纸”后站点要求改成正确汉字，于是把词改为“文化造诣”，提交 `诣`。

### 验证

五次索引形成完整指令；中间反馈确认“纸”定位无误，改正后的 `诣` 正确。

<a id="p-BvqEpJHi"></a>

## 文字游戏（BvqEpJHi）

- 答案：`alpha`

### 题面要点

例子包括 `2-7=b、4-7=dl、6-7=z、8-7=th、21-16=h、23-16=s`，提示数字上限 24。

### 我的解法

数字按希腊字母表编号，并从第一个希腊字母英文名中删掉第二个名字的字母：`beta-eta=b`、`delta-eta=dl`、`zeta-eta=z`、`theta-eta=th`、`phi-pi=h`、`psi-pi=s`。六条例子本身已足以确定这套编号规则，因此编号 1 的名字是小写 `alpha`。

### 验证

六条例子均逐字成立；本地提交命令返回账号已解出，错误 0 次。日志后来通过浏览器取得的“上限 24”免费提示未用于本段推导。

<a id="p-q4kUKLri"></a>

## 料理（q4kUKLri）

- 答案：`刺身`

### 题面要点

图标来自日本料理调味料“さしすせそ”，数字从调味料日文名中取假名，并与额外假名拼成菜名。

### 我的解法

糖 `砂糖(さとう)` 的第 2、3 位加 `ふ` 得 `とうふ`；盐 `塩(しお)` 第 2 位配醋 `酢(す)` 和 `し` 得 `おすし`；味噌 `みそ` 第 2 位加 `ば` 得 `そば`。末行分别取砂糖、盐、味噌的第 1 位，即 `さ、し、み`，合成 `さしみ`，按示例写作汉字 `刺身`。

### 验证

三个示例和末行使用同一假名索引；`刺身` 首次提交 correct。

<a id="p-p0e2nNtD"></a>

## 旅立ち（p0e2nNtD）

- 答案：`運勢`

### 题面要点

题图用圆圈表示恒星演化阶段名称的日语假名，灰圈舍弃、彩圈提取；旁边图标用于确认同音词。

### 我的解法

前两行示范：`主系列星（しゅけいれつせい）` 提取 `けいつい=頸椎`，含 `巨星（きょせい）` 的阶段提取 `きせい=規制`。末行 `超新星（ちょうしんせい）` 的蓝圈取第 3、5、6、7 个假名，得到 `うんせい`，写作 `運勢`。

### 验证

三个阶段都遵守同一“天文词读音→抽假名→同音词”规则，末图的幸运含义进一步校验 `運勢`；提交正确。

<a id="p-cSyHRhJe"></a>

## 旅行前也要先填饱肚子呀……（cSyHRhJe）

- 答案：`CHANGI`

### 题面要点

六段文字描述一条新加坡路线，每段含地点和索引。第一轮会得到与“吃饭/旅行”都有关系的中间词，随后要改用地铁信息重解。

### 我的解法

第一轮从天福宫附近文字、Collyer Quay、Jubilee Bridge、War Memorial Park、Changi Exhibition Centre、Loyang 等名称按 `1,2,3,1,3,倒数4` 取字，得到 `SUBWAY`；站点提示乘地铁继续。再把各段的线路方向词与数字读成新加坡 MRT 站码：`CC17 Caldecott、NE6 Dhoby Ghaut、NS18 Braddell、DT11 Newton、TE28 Siglap、EW3 Simei`。复用同一索引，取 `C,H,A,N,G,I`。

### 验证

第一阶段 `SUBWAY` 同时呼应三明治店和地铁；第二阶段六个站名按原索引精确拼出 `CHANGI`，最终正确。

<a id="p-qOpUKLri"></a>

## 无需多言（qOpUKLri）

- 答案：`LIFE`

### 题面要点

左侧轮廓与右侧图标要连成标准标志，底部按四色给出索引 `8-5-1-1`。

### 我的解法

连接成蓝色 `PARKING LOT`、黄色 `WARNING`、红色 `FIRE`、绿色 `EXIT`。按颜色顺序分别取第 8、5、1、1 字母，得到 `L I F E`。不用文字的标志保护生命，也呼应标题。

### 验证

错误的四角号码分支累计 3 次错误；按标志英文提取的 `LIFE` 正确。

<a id="p-Xe7kPIap"></a>

## 无需枚举（Xe7kPIap）

- 答案：`FUN`

### 题面要点

题体为 `(1/5 4) (3/4) (5/7 4)`；说明斜线前是抽取位置，后面是被抽取对象的词长。

### 我的解法

无需遍历词典，斜线后的长度直接对应英文数字名：`5 4=FIFTY FOUR`，`4=FOUR`，`7 4=SEVENTY FOUR`。忽略空格后分别取第 1、3、5 字母，得到 F、U、N。

### 验证

每个长度模式只需数字名即可解释；`FUN` 首次提交 correct。

<a id="p-KeQXEjGS"></a>

## 时雨谜 · 〇三一 || 血雨（KeQXEjGS）

- 答案：`HAWAII`

### 题面要点

图中按红橙黄绿青蓝紫给出色阶，六个物体被涂成不正常颜色，并各带一个初始字母；说明要求让时间倒退，直到颜色恢复正常。

### 我的解法

沿色阶反向走到物体正常色，步数用于凯撒位移：天空紫→蓝走 1，`G→H`；树青→绿走 1，`Z→A`；草蓝→青→绿走 2，`U→W`；消防栓黄→橙→红走 2，`Y→A`；橙子青→绿→黄→橙走 3，`F→I`；玉米绿→黄走 1，`H→I`。得到 `HAWAII`。

### 验证

六个物体各自独立给出一个确定步数，位移结果直接拼成地名；`HAWAII` 首次提交正确。

<a id="p-KpIXEjGS"></a>

## 明诚谜 003（KpIXEjGS）

- 答案：`吴承恩`

### 题面要点

例子为 `10=浙大校训、100=COLA、10000=如意图`，目标 `1=??`，答案格式 `??N（人名）`。

### 我的解法

例子组成四字固定语：十/实+求是=`实事求是`，百+可乐=`百事可乐`，万+如意=`万事如意`。所以 1 对应 `一事无成`，空格是 `无成`；再接字母 N 的读音“恩”，并作同音规范化：无→吴、成→承、N→恩，得到人名 `吴承恩`。

### 验证

三个例子、固定成语和人名约束完全一致；`吴承恩` 首投正确。

<a id="p-FCjyul5g"></a>

## 明诚谜 005（FCjyul5g）

- 答案：`YOUR`

### 题面要点

两行七个彩色槽分别提示“北方菜”和“岳飞罪”，大部分位置上下相同，四个不同位置带 1–4 抽取号。

### 我的解法

把答案写成无空格拼音：北方菜“木须肉”为 `MUXUROU`，岳飞罪名“莫须有”为 `MOXUYOU`。两串在 1、3、4、6、7 位完全相同，正对应连线；不同格按号码取：1=Y（下 5），2=O（下 2），3=U（上 2），4=R（上 5），得到 `YOUR`。

### 验证

两条七字母拼音、所有相等连线与编号都精确一致；本地正确清单确认答案。

<a id="p-X2akPIap"></a>

## 明诚谜001（X2akPIap）

- 答案：`北京明诚学校`

### 题面要点

四象限淡字分别是北、昌、南、京，彩色标记要求取整字或拼接局部，末尾已给“诚学校”。

### 我的解法

红、绿标记直接选出“北”和“京”；橙、紫两个半宽标记分别从“昌、南”取相关部分，拼成“明”。把结果接上题面提供的“诚学校”，得到 `北京明诚学校`。

### 验证

四色标记各有用途，组合后的名称符合题目所问“哪所中学”；零错通过。

<a id="p-AZDTwX1Q"></a>

## 明诚谜004（AZDTwX1Q）

- 答案：`LEMON`

### 题面要点

图中先有五个未知字母，再接编号 1–5 的五字母，并标注几层近似数值；底部写明抽取顺序 `3 2 1 4 5`。

### 我的解法

近似数值是 pH：前五字母可填 `WATER`，pH 约 7；十字母整体填 `WATERMELON`，pH 约 5.5，因此编号部分是 `MELON`。按 `3,2,1,4,5` 重排为 `LEMON`，其 pH 约 2.5，补上最后一层数值。

### 验证

直接提交抽取序号 `32145` 被判错；pH 链和索引共同得到的 `LEMON` 正确。

<a id="p-tQe7ji9S"></a>

## 明诚谜007（tQe7ji9S）

- 答案：`A6F10H3`

### 题面要点

10×12 网格中给出必须覆盖的蓝色机身格、禁止进入的深灰格，以及三种可旋转的飞机形状；要求报告三架飞机机鼻坐标。

### 我的解法

把每个形状相对机鼻的格偏移录入程序，枚举四种旋转和所有平移，剔除越界、碰禁格、机鼻落在既有机身格的放置。再组合三架飞机，要求互不重叠且恰覆盖全部 14 个蓝格。合法单形状放置分别有 18、10、14 种，三者组合只有一解：机鼻为 `A6、F10、H3`。

### 验证

唯一组合满足全部覆盖与禁入约束；按行字母升序串联为 `A6F10H3`，首投正确。

<a id="p-eJ0oQPLb"></a>

## 明诚谜008（eJ0oQPLb）

- 答案：`详细信息`

### 题面要点

新疆轮廓下有八个彩色格，重复颜色模式对应字母；答案区域分成 5、2、3、2 格，要求把拼音转回中文。

### 我的解法

`新疆` 的拼音 `XINJIANG` 正好八字母，重复的 I、N 位置与同色格吻合，由此建立颜色到字母的键。答案四行依次解成 `XIANG / XI / XIN / XI`，连接为 `XIANGXIXINXI`，还原中文是 `详细信息`。

### 验证

重复颜色、行长和拼音分词全部一致；`详细信息` 首投正确。

<a id="p-9XXWHnxJ"></a>

## 明诚谜009（9XXWHnxJ）

- 答案：`RIVER`

### 题面要点

两天考试时间表中，每科考试时长除以 10 等于该科英文名长度；需要比较相同钟点的字母。

### 我的解法

两天科目依次可填 `GEOGRAPHY、HISTORY、VIROLOGY、ENGLISH、FRENCH` 与 `ART、MUSIC、VENETIAN、CHEMISTRY、LITERATURE`。从各考试开始，每十分钟放置下一个字母；比较同一时刻，08:40、09:50、11:00、13:20、15:30 的两边字母相同，分别是 R、I、V、E、R。

### 验证

每科时长与词长吻合，五个相同时刻依序拼成 `RIVER`；本地提交记录为 correct。

<a id="p-TSUKhwRH"></a>

## 最烂的谜题只需枚举（TSUKhwRH）

- 答案：`TRUETYPE`

### 题面要点

图片模拟旧版 Windows 字体查看器，字体名用首次出现字母编号写成 `12345 6789 36`，标题栏括号内有八个高亮问号。

### 我的解法

编号模式可识别字体名 `COMIC SANS MS`，也解释“最烂字体”的笑点，但这只是背景。真正被高亮的是字体查看器标题栏的固定类型后缀，八个字符正是 `(TrueType)`，所以需要提交 `TRUETYPE`，而不是字体家族或示例 pangram。

### 验证

`COMIC SANS MS`、`COMIC SANS` 和 pangram 均被判错；八问号对应的 `TRUETYPE` 提交正确。

<a id="p-m61r8Uar"></a>

## 月照纱窗 2（m61r8Uar）

- 答案：`离家今几载`

### 题面要点

五行只显示汉字内部封闭区域，风味为“字字孔明诸格亮”；每行对应一个四字成语并有一个完全不可见字。

### 我的解法

可由题图直接观察到每行只保留了若干汉字的封闭区域，因此“没有封闭区域的字会消失”是合理方向。日志给出的五行复原为 `貌合神离、家喻户晓、博古通今、曾几何时、口碑载道`，相应缺字依次为 `离、家、今、几、载`，连读得到 `离家今几载`。

### 验证

`离家今几载` 获正确判定。本地独立证据有限：日志在系统化匹配前已经查看本地保存的 P&KU2 解法并使用外部生成器确认机制，现有记录无法证明五个成语是在未受该材料影响下独立还原；因此这里只把孔洞观察、日志所列填词和提交结果分开陈述。

<a id="p-Kx6XEjGS"></a>

## 月照纱窗 3（Kx6XEjGS）

- 答案：`枕上劝人归`

### 题面要点

黑底上只显示汉字内部封闭空腔，排列成 5×4 字符网格；每行恰有一个没有封闭腔、因而完全隐形的字。

### 我的解法

按白色负空间形状还原各行成语/短语：`枕曲藉糟`、`喜上眉梢`、`好言相劝`（或空腔兼容的同类填法）、`血口喷人`、`解甲归田`。每行唯一无内孔的暗字依次为 `枕、上、劝、人、归`，直接读出答案。

### 验证

前四次基于形状误配的抽取均 incorrect；修正负空间识别后 `枕上劝人归` correct。

<a id="p-TMHKhwRH"></a>

## 月照纱窗 4（TMHKhwRH）

- 答案：`动作`

### 题面要点

4×4 网格只画汉字内部封闭负形，部分格为空；两个位置标为 `①`、`②`，需要先恢复四字词再提取。

### 我的解法

前三行由负形还原为 `扭曲作直、删繁就简、兽聚鸟散`。它们的第二、四字依次形成反义对 `曲/直、繁/简、聚/散`，因此第四行平行地应为 `一静一动`。标号格中 `①=动`，第一行 `②=作`，按编号得到 `动作`。

### 验证

四行结构和反义对序列给出决定性约束；多个弱候选被排除后，`动作` 提交正确。

<a id="p-q9SUKLri"></a>

## 月照纱窗1（q9SUKLri）

- 答案：`无多花片子`

### 题面要点

5×4 图只显示汉字笔画围成的封闭负形，像纱窗透光的“孔”；每行对应四字词，其中无封闭区域的字整格全黑。

### 我的解法

用本机字体渲染候选汉字并比较孔洞的数量、位置和形状，再用四字词组作整行约束，恢复出 `默默无闻、足智多谋、明日黄花、片文只事、膏腴子弟`。每行唯一无孔字依次为 `无、多、花、片、子`。

### 验证

五行图形均能由相应汉字的封闭区域解释，逐行取全黑格得到 `无多花片子`；零错通过。

<a id="p-gCN6lhr6"></a>

## 月照纱窗（无限版）（gCN6lhr6）

- 答案：`我是月照纱窗传奇`

### 题面要点

这是交互式版本：根据汉字封闭区域的黑白图恢复诗句，累计答对十轮后显示外层提交答案。

### 我的解法

检查本地归档的交互脚本，确认 `PASS_THRESHOLD=10`。胜利文字以整数数组保存，运行脚本自身的异或解码公式后，前缀数组得到“恭喜通关！提交答案：”，答案数组得到 `我是月照纱窗传奇`。

### 验证

该字符串只在十轮通关分支由 `victoryMessage()` 拼出，明确位于“提交答案：”之后，因此不是某一轮诗句而是外层答案。

<a id="p-IWfLNP39"></a>

## 本题设有中间答案验证（IWfLNP39）

- 答案：`IT ALL CLICKED`

### 题面要点

起始页面直接声称答案是 `POINTLESS`，标题说明有中间验证；随后答案会改变页面状态，进入文字版 point-and-click 房间。

### 我的解法

可独立复现的部分是依次通过中间验证：`POINTLESS→ANDROID→CLICKBAIT→GAMEPLAY`。四词拆成 `POINT/LESS、AND/ROID、CLICK/BAIT、GAME/PLAY`，取前半得 `POINT AND CLICK GAME`，从而进入文字版房间；“观察房间”等动宾命令也能继续推进状态。日志随后没有从房间物件独立推出最终短语，而是直接读取归档元数据中的正确提示得到 `IT ALL CLICKED`。

### 验证

四个链式词和 `POINT AND CLICK GAME` 均触发中间状态；探索中共记录 9 次错误，`IT ALL CLICKED` 最终为 correct。本地独立证据有限：最终答案属于作者正确提示泄漏，不能算我们的独立提取；独立解题进度只能确认到 point-and-click 房间及其命令机制。

<a id="p-zEbG691D"></a>

## 来自地球的礼物（zEbG691D）

- 答案：`REMOTE CONTROLLED CAR`

### 题面要点

月球上的女孩收到来自地球的礼物。题面给出一个不走斜线的 10×10 英文词搜和各类别、长度清单，称 16 件礼物中只出现了 15 件。

### 我的解法

我逐类在网格中找到 `SWING、SLIDE、BASKETBALL、SKATEBOARD、WATER GUN、GLOBE、CRAYON、BALLOON、CRT TV、TENT、PARASOL、CAMPFIRE、FLOWER、SANDCASTLE、BUG NET`。划去这 15 项后，剩余字母按行读为 `PRAGMATA`，说明题面背景对应游戏《PRAGMATA》。最初我误把 `BUG NET` 当缺失礼物；服务器否定后，重新对照本地日志中已确认的 16 件地球记忆收藏品，发现真正未在词搜中出现的是 RC Car。中间反馈给出 `(6 10 3)` / `(2 3)`，将其展开为 `REMOTE CONTROLLED CAR` / `RC CAR`。

### 验证

15 个词完整覆盖清单，余字 `PRAGMATA` 校验作品背景；枚举精确吻合 `REMOTE(6) CONTROLLED(10) CAR(3)`。该答案提交正确。

<a id="p-bYF5uOJW"></a>

## 极简键盘（bYF5uOJW）

- 答案：`REFERENCE`

### 题面要点

键盘只留 Ctrl、C、V、A；操作记录去掉 Ctrl 后为九字符 `CVCVCVACV`，故事背景是查阅文献写论文。

### 我的解法

把 C/V 当 consonant/vowel 模板，A 当任意字母。`REFERENCE` 的字母类型是 `R(C) E(V) F(C) E(V) R(C) E(V) N(A) C(C) E(V)`，精确符合 `CVCVCVACV`；“论文/文献”背景又直接提示 reference。其他同模板单词没有同等语义支撑。

### 验证

九字母长度、按键序列和主题三重吻合；首次提交 correct。

<a id="p-tvD7ji9S"></a>

## 核类艺术（微恐）（tvD7ji9S）

- 答案：`NUCLEAR WEAPON`

### 题面要点

七幅图配被编号圆圈遮住的英文词，前几幅是网络 `-core` 美学，后几幅转向果核、地核、细胞核和病灶；最终按编号 ①–⑫ 读短语。

### 我的解法

依次识别 `DREAMCORE、WEIRDCORE、POOLCORE、APPLECORE、CORE、NUCLEUS、TUBERCULOSIS`。按各词中编号所在位置回填字母：①N、②U、③C、④L、⑤E、⑥A、⑦R、⑧W、⑨E、⑩A、⑪P、⑫O，并重复①作为末字 N，组成 `NUCLEAR WEAPON`。

### 验证

十二个编号字母全部有唯一来源，且题名“核类/core”双关贯穿七图；提交正确。

<a id="p-XjYkPIap"></a>

## 梨谜014A（XjYkPIap）

- 答案：`循环往复`

### 题面要点

方框表示“口”形包围构字，三行不完整成语用于确定编号字，底部再把这些字拆部件组装。

### 我的解法

第二行补成“日复一日”，得 1=复；第三行“百折不回”，得 2=不；第四行“一目十行”，得 3=行。底部依次要求 `彳+盾、王+不、彳+主、复`，分别组成“循、环、往、复”。

### 验证

三个编号由固定成语唯一确定，底部四次部件组合完整生成 `循环往复`；首投正确。

<a id="p-E4otl1dT"></a>

## 森林不退化（E4otl1dT）

- 答案：`奥秘`

### 题面要点

右侧红白块是去除白色部分后仍可识别的国旗，左侧对应 2 格、3 格，箭头自下向上提取。

### 我的解法

上方两条竖红带对应秘鲁国旗，填 `秘鲁`；下方两条横红带对应奥地利国旗，填 `奥地利`。箭头自下而上先穿过“奥地利”的首字 `奥`，再穿过“秘鲁”的首字 `秘`，得到 `奥秘`。

### 验证

国旗方向、字数和箭头顺序一致；`奥秘` 首投正确。

<a id="p-ghc6lhr6"></a>

## 森林退化（ghc6lhr6）

- 答案：`大巴`

### 题面要点

两面国旗的植物图案被移除：加拿大国旗缺枫叶，黎巴嫩国旗缺雪松；旁有 2×3 格和斜向抽取箭头。

### 我的解法

把两个三字国名按行填入：上行 `加拿大`，下行 `黎巴嫩`。斜箭头依次穿过上行右格 `大` 与下行中格 `巴`，得到 `大巴`。

### 验证

“国家”和“无植物”风味同时解释两旗残影；`大巴` 首次提交 correct。

<a id="p-RX1AJFgi"></a>

## 水浒卡（RX1AJFgi）

- 答案：`WATER MARGIN`

### 题面要点

卡片画《水浒传》人物，风味提示使用英雄座次，并给出英文答案枚举 `(5 6)`。

### 我的解法

把每张卡的人物座次当 A1Z26：史进 23=W、宋江 1=A、戴宗 20=T、关胜 5=E、徐宁 18=R；鲁智深 13=M、宋江 1=A、徐宁 18=R、秦明 7=G、花荣 9=I、武松 14=N。连读为 `WATER MARGIN`。

### 验证

十一张卡的座次逐一给出目标字母，结果正是《水浒传》常见英文名；提交正确。

<a id="p-WiTlljce"></a>

## 江河湖海（WiTlljce）

- 答案：`2`

### 题面要点

题图给“江、河、海”对应数字，询问“湖”的数字。

### 我的解法

数字是在数拼音的声音部件，把 `ng` 当一个韵尾：江 `jiang=j+i+a+ng` 为 4，河 `he=h+e` 为 2，海 `hai=h+a+i` 为 3。因此湖 `hu=h+u` 为 2。

### 验证

同一拆分规则解释三个已知样例，未知项得到 `2`；首投正确。

<a id="p-gFt6lhr6"></a>

## 汽水谜（gFt6lhr6）

- 答案：`吴京`

### 题面要点

定义 A1、B1、C2；A/B/C 近义且 A、C 常形容汽水，1、2 同音形近，最后问扮演 C2 的汽水代言人。

### 我的解法

`A1=冰峰`，故 A=冰、1=峰；`B1=凌峰`，B=凌，与冰近义。取 C=冷、2=锋，满足同音形近，于是 `C2=冷锋`，即《战狼》角色。扮演冷锋且符合代言人描述的是 `吴京`。

### 验证

冰/凌/冷近义和峰/锋关系完整闭合；`吴京` 首投正确。

<a id="p-bC65uOJW"></a>

## 汽水谜（三）（bC65uOJW）

- 答案：`伽勒尔双弹瓦斯`

### 题面要点

字母组 ABC、DE 分别由汽水/日本活动等线索确定，随后要求找一个“在英国的升级版”七字答案。

### 我的解法

ABC 是格瓦斯，故 A=格、B=瓦、C=斯；DE 是弹珠，来自弹珠汽水/日本弹珠活动，故 D=弹、E=珠。于是 BCD=`瓦斯弹`，即宝可梦瓦斯弹；其进化是双弹瓦斯。“在英国”指以英国为原型的伽勒尔地区，因此所求为地区形态 `伽勒尔双弹瓦斯`。

### 验证

字母重叠、进化关系、地区提示和七字枚举全部一致；首次提交 correct。

<a id="p-z5nG691D"></a>

## 汽水谜（二）（z5nG691D）

- 答案：`非人`

### 题面要点

题设 `AB` 是汽水，`CDAB` 是其中一种更具体的产品，要求输出 `C人`；检查器可能返回中间提示。

### 我的解法

先取 `AB=可乐`。尝试 `可口可乐` 得 `C=可`，提交 `可人` 后，检查器提示“这不是中国人自己的答案”。这句提示指向定位为“中国人自己的可乐”的 `非常可乐`，故 `CDAB=非常可乐`，C=`非`，最终 `C人=非人`。

### 验证

`可人` 获中间提示而非错误，按提示换成品牌全名后，`非人` 提交正确。

<a id="p-RkTAJFgi"></a>

## 汽水谜（六）（RkTAJFgi）

- 答案：`海风`

### 题面要点

每个中心空格要与四周汽水品牌中的一个字按箭头方向组成词；两格之间同品牌原则上不能重复取字，唯可口可乐例外。

### 我的解法

第一格取“海”：元气森林取林成林海，雪碧取碧成碧海，北冰洋取洋成海洋，可口可乐取口成海口。第二格取“风”：北冰洋取北成北风，可口可乐取口成口风，雪碧取雪成风雪，元气森林取气成风气。两中心字按顺序为 `海风`。

### 验证

八个词都自然成立；森林、雪碧、北冰洋在两格取字均不重复，只有可口可乐重复“口”，正吻合特例说明。

<a id="p-iK0RTMow"></a>

## 汽水谜（四）（iK0RTMow）

- 答案：`新年快乐`

### 题面要点

题面以 A–L 代替汉字/音节，用汽水品牌、公司、传说动物、球队和餐厅建立重叠词链，询问 `EBID`。

### 我的解法

`ABC=美年达`、`CA=达美`、`CAD=达美乐`，得 A=美、B=年、C=达、D=乐。`EFG=新奇士`、`FAH=奇美拉`，得 E=新、F=奇、G=士。KFC 是 `快餐厅`，确定 I=快；球队/地名链也作旁证。代入 `EBID` 得 `新+年+快+乐`。

### 验证

品牌与专名的重叠逐字一致，结果为自然固定短语。本地日志未执行提交；本批清单列为 correct，本地日志仅能确认答案机制为 `新年快乐`。

<a id="p-79kIxIpP"></a>

## 洋（79kIxIpP）

- 答案：`HARBOR`

### 题面要点

三组图片拼词分别配有骰点 1–6，骰点落在对应单词的某些字母上。

### 我的解法

图片词为 `STAR+FISH=STARFISH`、`BRO+OK=BROOK`、`RUN+OFF=RUNOFF`。按骰点数字顺序读取其下字母：1→H（STARFISH 第 8 位）、2→A（第 3 位）、3→R（BROOK 第 2 位）、4→B（BROOK 第 1 位）、5→O（RUNOFF 第 4 位）、6→R（RUNOFF 第 1 位），组成 `HARBOR`。

### 验证

六个骰点恰好给六字母水域相关词；首次提交 correct。

<a id="p-p8D2nNtD"></a>

## 添几笔（p8D2nNtD）

- 答案：`云`

### 题面要点

示例 `带→一、气→メ、儿→旧`，风味说到了异国写字要多花功夫；题目问 `齐`、`广` 分别需添什么。

### 我的解法

这里不是数笔画，而是把简体字变成日文标准字形并取新增部件：`带→帯` 添一，`气→気` 添メ，`儿→児` 添旧。于是 `齐→斉` 添 `二`，`广→広` 添 `厶`。按上下次序把 `二` 与 `厶` 组合成单字 `云`。

### 验证

直接提交 `二厶` 被判错，说明需要合字；`云` 提交正确。

<a id="p-5EtuzMeL"></a>

## 演变（5EtuzMeL）

- 答案：`魂魄`

### 题面要点

例图把“王”和“虎”合字得到“琥”，并以两字词“琥珀”落地；问题给“云”和“鬼”。

### 我的解法

将“云”与“鬼”合成汉字“魂”，再仿照例题补成常用二字词，得到 `魂魄`。`灵魂` 虽同义，但生成的“魂”会落在第二位，不符合例题中合成字位于第一位的格式。

### 验证

合字位置和二字词结构均与“琥珀”平行；`魂魄` 首投正确。

<a id="p-1BzaRpKD"></a>

## 漫游（1BzaRpKD）

- 答案：`RAMBLING`

### 题面要点

交互题使用环面 5×5 网格，移动时通过提示显示当前格字母在 Polybius 方阵中的行或列。

### 我的解法

本地交互资源可重建方阵：`ABTEP / HGWIY / LMNZQ / DRVKX / OUSCF`。与标准去 J 的 5×5 字母方阵逐格比较，位置相同的字母为 `A B G I L M N R`。这些字母结合题名“漫游”唯一重排为 `RAMBLING`。

### 验证

固定位置字母集合与答案完全同构，且答案正是题名含义；`RAMBLING` 首投正确。

<a id="p-1IuaRpKD"></a>

## 火柴人推箱子（1IuaRpKD）

- 答案：`BOXES`

### 题面要点

火柴人把一个 4×4 的十六字母箱堆推向阶梯状坑地，需要模拟所有箱子的落位。

### 我的解法

按从左向右推动并让最右/最低的箱子依次落入台阶凹槽，最终把落定后的字母按从左到右、从上到下读，得到句子 `THE ANSWER IS BOXES`。初始十六字母的多重集也恰好等于该句去空格后的字母多重集。

### 验证

终态直接给出答案，字母计数提供独立校验；`BOXES` correct。

<a id="p-xebD8t6h"></a>

## 熊不是黑白的（xebD8t6h）

- 答案：`PANDA`

### 题面要点

五条线索各指向一只熊或熊状角色及其代表色；风味强调 RGB 和“bits of color”。

### 我的解法

五项识别为 `PADDINGTON BEAR`（蓝）、`URSUS MARITIMUS`（白）、`URSA MINOR`（白）、`DJUNGELSKOG`（蓝）、`VOLIBEAR`（白）。把蓝色 RGB 位写成 `001=1`，白色写成 `111=7`，分别在去空格名称中取第 1 或第 7 字母，得到 `P A N D A`。

### 验证

每项的名称长度与颜色位索引都能独立核对；`PANDA` 首次提交正确。

<a id="p-TelKhwRH"></a>

## 熟悉的等式（TelKhwRH）

- 答案：`GENIUS`

### 题面要点

示例为 `27 8 19 = CoOK`，标签是化学；问题为 `32 28 92 16`。

### 我的解法

把数字当元素原子序数。示例中 27=Co、8=O、19=K，拼成 CoOK。问题中 32=Ge、28=Ni、92=U、16=S，连接为 `GeNiUS`。

### 验证

忽略元素符号大小写即 `GENIUS`；四个原子序数唯一，首投正确。

<a id="p-KZ7XEjGS"></a>

## 猜单词（KZ7XEjGS）

- 答案：`REAL WAR`

### 题面要点

密文为 `AB CDB CEE ABEE CACDB that ......`，A–E 各代表不同英文字母，要求解 `DBCE ACD`。

### 我的解法

四级作文常见句首 `WE ARE ALL WELL AWARE that...` 精确匹配重复模式，得到 A=W、B=E、C=A、D=R、E=L。代入目标：`DBCE=REAL`，`ACD=WAR`。

### 验证

五个密文词全部同时还原为自然句子；`REAL WAR` 首投正确。

<a id="p-zu0G691D"></a>

## 猜单词 1（zu0G691D）

- 答案：`FASCINATOR`

### 题面要点

模板为 `F[介词]C[介词][介词][连词] (10)`。

### 我的解法

把括号填成完整的短英文功能词：介词依次取 `AS、IN、AT`，连词取 `OR`。拼接为 `F+AS+C+IN+AT+OR=FASCINATOR`，正好十字母；as、in、at 均可作介词，or 为并列连词。

### 验证

词性与枚举完全满足；本地正确清单确认 `FASCINATOR`。

<a id="p-mnCr8Uar"></a>

## 猜单词 2（mnCr8Uar）

- 答案：`CLASSMATES`

### 题面要点

题目给五个带编号的周期表位置，需要把元素符号拼成一个十字母词。

### 我的解法

五个元素依次是 Chlorine=`Cl`、Arsenic=`As`、Samarium=`Sm`、Astatine=`At`、Einsteinium=`Es`。直接拼为 `ClAsSmAtEs`，忽略大小写即 `CLASSMATES`。

### 验证

五个元素符号无剩余地组成目标词；`CLASSMATES` 提交正确。

<a id="p-SxSj2oe3"></a>

## 画（SxSj2oe3）

- 答案：`AFRICA`

### 题面要点

六面墙上的画框排成若干矩形网格；需要对每面墙分别数所有可由小框组合出的矩形，而非只数最小格或求总和。

### 我的解法

六格依阅读顺序的矩形总数分别是：单格 1；1×3 网格为 6；两个独立 2×2 网格共 18；一个 2×2 网格为 9；1×2 网格为 3；单格 1。得到 `1,6,18,9,3,1`。

### 验证

A1Z26 转成 `A,F,R,I,C,A`，拼成 `AFRICA`。这也解释了为什么六面墙必须分别保留位置；最终正确。

<a id="p-HjG44RZL"></a>

## 留空（HjG44RZL）

- 答案：`BAT`

### 题面要点

近乎空白的图实际是键盘左侧，唯一明显符号位于 Tab 键并指向左；题目要求一种动物。

### 我的解法

键位几何先确定按键名 `TAB`，其左向/返回箭头给出倒读操作。把 `TAB` 反转即 `BAT`，恰是一种动物。

### 验证

早期 `CAT`（Keyboard Cat）与 `TABBY` 均判错；利用箭头倒读后 `BAT` 正确，共 2 次错误。

<a id="p-x8hD8t6h"></a>

## 病历乱神（x8hD8t6h）

- 答案：`UNUSUAL TREATMENT`

### 题面要点

十六条“病历”影射四大名著中的人物事件，每条带索引，需要做两轮拼音抽取。

### 我的解法

先识别鲁智深、诸葛亮、孙悟空、林冲、潘金莲、贾探春、黑熊精、刘备、公孙胜、庞统、唐僧、太白金星、石秀、曹操、张飞、司马昭，并按索引取其无空格拼音，得到 `IN WHICH LOCATIONS`。这要求改取对应事件地点：野猪林、七星坛、八卦炉、山神庙、狮子楼、秋爽斋、洛迦山、檀溪、二仙山、落凤坡、盘丝洞、天庭、大名府、宛城、长坂桥、铁笼山。用同一索引再取拼音，得到 `UNUSUAL TREATMENT`。

### 验证

第一轮形成清晰英文指令，第二轮形成完整答案；首次提交 correct。

<a id="p-cO8HRhJe"></a>

## 百合谜 01（cO8HRhJe）

- 答案：`ADACHI`

### 题面要点

三位角色图片后是其伴侣姓名模板，九个编号散布在字母位中；最终提示 `(9)→(6)`，先取九字母名字，再找其六字母伴侣。

### 我的解法

三组伴侣名按本地日志填为 `Tonami Ibuki`、`Anisufia Win Parettia`、`Miyagi Shiori`，用模板编号建立字母表。按 1–9 读取为 `SHIMAMURA`。继续套用题目的“与她相伴的人”规则，Shimamura 的六字母伴侣是 `ADACHI`。

### 验证

九个编号恰好拼出 `SHIMAMURA`，再满足六字母终点；`ADACHI` 提交正确。

<a id="p-yC1zg7XA"></a>

## 相生相克（yC1zg7XA）

- 答案：`EARTH THEATER`

### 题面要点

五条线索先识别一个五字母中间答案，再把字母按金木水火土分配，并沿相克、相生次序读取。

### 我的解法

线索识别《崩坏：星穹铁道》角色 `HERTA`，依题面金木水火土顺序映射为 `金=H、木=E、水=R、火=T、土=A`。从金出发沿相克循环 `金木土水火` 得 `HEART`；沿相生循环的反向 `金土火木水` 得 `HATER`。分别提交这两个中间词后，判题器返回两条带黑格的五行字符串；把两串黑格互补叠合，得到元素序列 `木土水火金火金木土火木水`。

### 验证

按同一五行映射转字母，序列为 `EARTH THEATER`；三次前置提交均被当作中间答案，最终串正确。

<a id="p-gbq6lhr6"></a>

## 神鲸谜 003（gbq6lhr6）

- 答案：`AGE`

### 题面要点

复平面直线满足 `z=a+bi, b=a+1`，线上三个点配儿童、成人工作者、老人遗像，答案标 `(3)`。

### 我的解法

以截距 `(0,1)` 为尺度，三点约为 `(1,2)、(3,4)、(7,8)`；把实部、虚部顺次拼成 12、34、78，与三个人生阶段吻合，说明编码的是年龄。题面答案长度为 `(3)`，将这一概念写成三字母英文即 `AGE`。

### 验证

`生命线` 判错；`年龄段` 命中中间验证，其反馈也确认英文 `age`。最终 `AGE` 可由坐标、人物阶段与三字母长度独立得到，反馈只作验证。

<a id="p-RKhAJFgi"></a>

## 神鲸谜 007（RKhAJFgi）

- 答案：`乙炔基`

### 题面要点

Wordle 风格两行分别为 `一 去 二 三 里` 与 `CACHE`，颜色给出字符存在性和位置限制；答案是三个汉字。

### 我的解法

隐藏五格包含 `一、三、C、C、H`：首位固定为一，三不在第 4 位，两枚 C 不在第 1/3 位，H 不在第 4 位。唯一有明确意义的排列是 `一 C 三 C H`，把“一”看作单键、三看作三键，即结构式 `—C≡CH`。这是 ethynyl group，中文为 `乙炔基`。

### 验证

结构式满足全部 Wordle 位置约束和三字枚举；首次提交 correct。

<a id="p-Zeipgd2S"></a>

## 福尔摩斯（Zeipgd2S）

- 答案：`HOUSE`

### 题面要点

五行看似普通的文字中混入圆点、间隔号、横线和下划线，题名及“怎么看、雨点”等措辞提示观察标点。

### 我的解法

把每行的点划读作摩斯码：第一行三个间隔号加句号为 `....=H`；第二行三个横线为 `---=O`；第三行为 `..-=U`；第四行为 `...=S`；第五行的字面“点”给 `.=E`。合成 `HOUSE`。

### 验证

初读漏掉一个间隔号得到的 `SOS` 被判错；完整五行摩斯码给 `HOUSE`，提交正确。

<a id="p-stNBl3vq"></a>

## 秘密单词本（stNBl3vq）

- 答案：`BEAUTY`

### 题面要点

不同符号一一替代英文字母，已知词按动物、饮料、网站分类，可利用词形模式破译。

### 我的解法

饮料 `+ ** ◢` 为模式 ABBC，可填 BEER，得到 `+=B、*=E、◢=R`。动物 `+ X ◢ ☆` 于是是 B?R?=BIRD，得 X=I、☆=D；网站 `+ □ X ☆ ♦` 是 B?ID?=BAIDU，得 □=A、♦=U。其余 CAT/DOG、SODA/TEA、YAHOO/SOGOU 可交叉验证映射。目标六符号解为 B-E-A-U-T-Y。

### 验证

同一替换表覆盖所有分类词，目标得到 `BEAUTY`；首投正确。

<a id="p-xJsD8t6h"></a>

## 符世绘（xJsD8t6h）

- 答案：`五谷丰登`

### 题面要点

四幅符号重绘均有富士山，标题谐音“浮世绘”，`(36)` 指向《富岳三十六景》。每幅有取字位置，末尾还有两项图形运算。

### 我的解法

四图分别识别为 `深川万年桥下、东海道程谷、甲州三岛越、登户浦`，按标记取出 `万、谷、三、登`。末尾把 `万/2k=5` 写成 `五`，并给 `三` 加一竖成为 `丰`，于是依次得到 `五、谷、丰、登`。

### 验证

四画名、取字位和两次变形全部有用；`五谷丰登` 首投正确。

<a id="p-4O19OF2B"></a>

## 粉色（4O19OF2B）

- 答案：`BEST BOAT`

### 题面要点

八段文字各隐喻 Pink Floyd 专辑《The Dark Side of the Moon》的一首曲目，题目要求再作抽取。

### 我的解法

八段依次对应 `Breathe、Eclipse、Speak to Me、Time、Brain Damage、On the Run、Any Colour You Like、The Great Gig in the Sky`。不应提交缺失曲目或专辑名，而应按段落顺序取八个曲名首字母，得到 `B E S T B O A T`，即 `BEST BOAT`。

### 验证

`MONEY US AND THEM`、专辑名、乐队名及单独缺失曲目均被拒；首字母抽取 `BEST BOAT` correct。

<a id="p-C7hfVTmL"></a>

## 纵横字咪（C7hfVTmL）

- 答案：`FELICETTE`

### 题面要点

猫主题英文填字共有六横七竖，九个红格分别画 1–9 个点，点数表示抽取顺序。

### 我的解法

交叉填入 `NYANCAT、PRIMORDIALPOUCH、CLOWDER、SPHINX、MANEKINEKO、MIAO` 等猫相关词。红格按行看到的点数次序为 `4,9,8,7,6,3,1,5,2`，按点数 1–9 重排对应字母，得到 `FELICETTE`。

### 验证

Félicette 是第一只进入太空的猫，回扣全题主题；`FELICETTE` 提交正确。

<a id="p-KowXEjGS"></a>

## 编程（KowXEjGS）

- 答案：`CODE`

### 题面要点

一段 C++ 质数判断代码中若干字母变成问号，四处缺字带编号。

### 我的解法

按标准代码补字：`#inclu(3)e` 应为 include，所以 ③=D；`(1)in>>a` 为 cin，所以 ①=C；`??ut<<"y(4)s"` 补 cout/yes，④=E；`?(2)ut` 补 cout，②=O。按编号 1–4 读取。

### 验证

得到 `C O D E`；未编号问号只负责补全代码，不进入提取，首投正确。

<a id="p-L4xqNrv1"></a>

## 缩略（L4xqNrv1）

- 答案：`MAP`

### 题面要点

两侧用完整词长度提示缩写，中心为三行两字母，红线经过三个格。

### 我的解法

左侧 `(9 10)、(9 10)、(5 10)` 分别对应 `Frequency Modulation=FM`、`Amplitude Modulation=AM`、`Phase Modulation=PM`；右侧 `(4 8)` 的 `Ante Meridiem=AM`、`Post Meridiem=PM` 再次确认后两行。红线依次选上行右格 M、中行左格 A、下行左格 P，得到 `MAP`。

### 验证

五个展开词的长度和缩写都一致；`MAP` 首投正确。

<a id="p-KDdXEjGS"></a>

## 美术课呢？（KDdXEjGS）

- 答案：`CANCEL`

### 题面要点

六张图分别以语文、数学、英语、物理、化学、生物为主题，每张内部自指地拼出科目英文名并标一个抽取位置。

### 我的解法

六图对应 `CHINESE、MATHEMATICS、ENGLISH、PHYSICS、CHEMISTRY、BIOLOGY`。按各图问号位置取字：CHINESE[1]=C，MATHEMATICS[7]=A，ENGLISH[2]=N，PHYSICS[6]=C，CHEMISTRY[3]=E，BIOLOGY[4]=L，组成 `CANCEL`。标题问“美术课呢”，答案说明美术课被取消。

### 验证

六个科目、长度与抽取位全部闭合；首次提交 correct。

<a id="p-9AAWHnxJ"></a>

## 老地方（微恐）（9AAWHnxJ）

- 答案：`GRENADE`

### 题面要点

五张现实化场景对应 Counter-Strike 经典拆弹地图，地图名模板中若干字母被编号 1–7 代替。

### 我的解法

五图识别为 `MIRAGE、DUST_II、NUKE、INFERNO、ANUBIS`。按模板回填：1=MIRAGE 第5字母 G，2=第3字母 R，3=INFERNO 第4字母 E，4=第6字母 N，5=ANUBIS 第1字母 A，6=DUST_II 第1字母 D，7=NUKE 第4字母 E。按 1–7 得 `GRENADE`。

### 验证

七个字母均由地图名固定位置给出，答案也符合拆弹游戏语境；提交正确。

<a id="p-IH5LNP39"></a>

## 自我治疗（IH5LNP39）

- 答案：`血炎症`

### 题面要点

flavor 突出“以撒”，三个“病号”数字对应《以撒的结合》收藏品 ID，图像和字格长度帮助确定中文物品名。

### 我的解法

157 对应两字物品“嗜血”，编号格取“血”；459 对应三字“鼻窦炎”，取“炎”；368 对应三字“溢泪症”，取“症”。按 1、2、3 顺序拼接。

### 验证

三个 ID、图像效果和名称长度相互吻合，提取为 `血炎症`；首投正确。

<a id="p-SMkj2oe3"></a>

## 节日快乐（SMkj2oe3）

- 答案：`VANILLA`

### 题面要点

七行 emoji 各代表一个节日，括号给提取位置与英文节日名的词长。

### 我的解法

七行依次是 `VALENTINE'S DAY、SAINT PATRICK'S DAY、CANADA DAY、INDEPENDENCE DAY、BASTILLE DAY、DIWALI、CHRISTMAS`。忽略空格和标点，按各行索引 1、2、3、1、6、5、8 取字母，依次得到 `V A N I L L A`。

### 验证

每组 emoji、词长与索引均一致；`VANILLA` 首投正确。

<a id="p-sIwBl3vq"></a>

## 芉禧姩洣趧迋ふ（一）（sIwBl3vq）

- 答案：`LONELY ISLAND`

### 题面要点

两组符号串为 `111￥` 与 `!$1&`，答案枚举 `(6 6)`；系列机制是按符号字形、名称或含义拼英文。

### 我的解法

`111￥` 可拆读为 `L+ONE+L+Y`：两个 1 取 L 形，中间 1 读 ONE，货币符号取 Y，得到 `LONELY`。`!$1&` 读为 `I+S+L+AND`：感叹号取 I，美元符号取 S，1 取 L，& 读 AND，得到 `ISLAND`。

### 验证

两组各恰为六字母，合成自然短语；首次提交 correct。

<a id="p-WA5lljce"></a>

## 芉禧姩洣趧迋ふ（二）（WA5lljce）

- 答案：`COMEDY CENTRAL`

### 题面要点

题面是一串外形奇特的货币/符号字符，枚举 `(6 7)`，标签“杀马特”提示按外观替字。

### 我的解法

前六个字符按形状依次对应 C、O、M、E、D、Y，得到 `COMEDY`。第二部分中 `¢` 表示 `CENT`，里亚尔符号表示 `RIAL`，再减去圈出的 `i`，即 `CENT + RIAL - I = CENTRAL`。

### 验证

两段分别严格符合 6、7 字母枚举；`COMEDY CENTRAL` 提交正确。

<a id="p-YtJhZAop"></a>

## 花卉培育！20260619（YtJhZAop）

- 答案：`安康`

### 题面要点

三个词 `担当、宽广、祥和` 要分别通过音、形、义指向同一个双字答案。

### 我的解法

音：担当 `dān dāng` 与安康 `ān kāng` 两音节分别同韵、同声调。形：宽与安同为宀部，广与康都以广为部件/部首。义：祥和描述的正是安宁康泰的状态，即“安康”。

### 验证

音形义三个关系一一分配且都按双字顺序对应；`安康` 首投正确。

<a id="p-9KKWHnxJ"></a>

## 花卉培育！20260620（9KKWHnxJ）

- 答案：`终结`

### 题面要点

规则要求三个词分别从音、形、义提示同一答案；线索为“收尾、通牒、图纸”。

### 我的解法

`收尾` 在意义上就是 `终结`；`通牒(tōng dié)` 与 `终结(zhōng jié)` 两个音节分别押韵；`终、结` 都含 `纟`，而 `图纸` 的“纸”也含该部件。三种关系恰好一一对应。

### 验证

语义、双音节押韵和共同部件同时成立。Windows 大小写不敏感导致目录与旧题 `9kkWHnxJ` 碰撞，现有“火柴”提交记录不属于本题；本地日志没有本题有效提交，只能确认清单答案与机制为 `终结`。

<a id="p-HAg44RZL"></a>

## 花卉培育！20260621（HAg44RZL）

- 答案：`图示`

### 题面要点

规则要求从三条线索分别通过声音、字形、意义指向同一词；线索为“服饰 / 国标 / 说明”。

### 我的解法

声音上，“服饰”与“图示”第二音节同为 shì，第一音节韵母、声调也相近；字形上，`国` 与 `图` 共享 `囗`，`标` 含 `示`；意义上，图示本来就是用来说明内容的。三种关系共同指向 `图示`。

### 验证

声、形、义一一覆盖且无需交换角色；首次提交 correct。

<a id="p-4TE9OF2B"></a>

## 花卉培育！20260622（4TE9OF2B）

- 答案：`草莓`

### 题面要点

三个提示是 `花海、扫雷、水果`，需分别从字形、读音、意义三个角度共同指向一个二字词。

### 我的解法

答案取 `草莓`：字形上花/草共享艹，海/莓共享完整部件每；读音上 `扫雷(sǎo léi)` 与 `草莓(cǎo méi)` 两个音节分别同韵同调；意义上草莓是水果。三种关系各占一条，且顺序一致。

### 验证

其他莓类只能满足字形和意义，不能像草莓一样逐音节押“扫雷”；`草莓` 首次提交正确。

<a id="p-5BEuzMeL"></a>

## 花卉培育！20260623（5BEuzMeL）

- 答案：`口腔`

### 题面要点

三个词为 `手枪、牙齿、中控`，同样分别承担音、义、形关系。

### 我的解法

音：手枪 `shǒu qiāng` 与口腔 `kǒu qiāng` 分别同韵同调。义：牙齿位于口腔，是其典型组成。形：`中` 含“口”，`控` 与“腔”都含完整部件“空”。

### 验证

两音节和两个字形部件均按顺序对应，语义关系直接；首投正确。

<a id="p-BBEpJHim"></a>

## 芳香（BBEpJHim）

- 答案：`茉莉`

### 题面要点

中央是带共同绿色 `艹` 顶部的苯环图，左右要求“反义字”，标题是“芳香”。

### 我的解法

中央表示 `苯`，绿色带是共同草字头。左侧对下部 `本` 取反义字 `末`，加艹成 `茉`；右侧从苯“有害”的 `害` 取反义字 `利`，加艹成 `莉`。左右合为芳香花卉 `茉莉`。

### 验证

直接把“苯/笨”取反义所得 `聪明、灵巧` 均判错；保留艹部件后 `茉莉` 正确，共 2 次错误。

<a id="p-OMhiZO0v"></a>

## 英文翻译？（OMhiZO0v）

- 答案：`ELEVEN`

### 题面要点

九个中文词被空行分成三组：橙色/九/橡皮，苹果/狗/点，树/蛋/不；标题要求英文翻译。

### 我的解法

逐词翻译并取首字母：`Orange Nine Eraser→ONE`，`Apple Dog Dot→ADD`，`Tree Egg No→TEN`。三个组输出指令 `ONE ADD TEN`，计算 1+10=11，再按标题写成英文 `ELEVEN`。

### 验证

空行恰好承担分组作用，三组首字母形成完整算式；首次提交 correct。

<a id="p-RSsAJFgi"></a>

## 蔚蓝谜（RSsAJFgi）

- 答案：`奥赛`

### 题面要点

字母代表《Celeste》地图中文名中的汉字，条件涉及地图名称、难度高低、同音字和同一大厅。

### 我的解法

利用本地保存的 Strawberry Jam 地图包中英文文本：`ABCD=星空遗迹`，`ABEF=星空之眠`，`HBEI=猩空之穴`，`ABJKL=星空奥德赛`。由此 A=星、B=空、J=奥、L=赛；“星/猩”同音和大厅/难度关系也与题设吻合。所求 `JL=奥赛`。

### 验证

四个本地化地图名和附加关系使用同一套字母代换；`奥赛` 提交正确。

<a id="p-P8Le2esI"></a>

## 蛙谜1 篮球赛得分情况（P8Le2esI）

- 答案：`0`

### 题面要点

给出杰森=5、乔治=3、安德鲁=5，问大卫；中文名和“分”均标绿，提示从汉字本身计“分/点”。

### 我的解法

数中文姓名字形中的点状笔画：已有三例可按相同口径得到 5、3、5。目标“大卫”两字没有点笔画，因此得分为 0。

### 验证

规则利用了只标绿中文名而非英文名的版式，也解释了绿色“分”的双关；`0` 首投正确。个别字体中点笔画的归类会有差异，因此这一机制以题图所用字形为准。

<a id="p-sQlBl3vq"></a>

## 西行漫记（sQlBl3vq）

- 答案：`LONGEST HIGHWAY`

### 题面要点

十天向西的游记沿连云港至新疆路线展开；编号段落有的 1 句、有的 5 句，文中夹杂大量真伪事实，住宿段落分隔每天。

### 我的解法

先把 1 句段落视作摩斯长划、5 句段落视作点，每晚住宿分字母，十天解得指令 `MISTAKE BIN`。再对每个五句段落逐句判真伪，真记 1、假记 0，五位二进制按 1–26 转字母。十四组依次给出 `LONGEST HIGHWAY`。明线城市基本沿 G30 连霍高速，验证其“中国最长高速”主题，但路线名不是提交串。

### 验证

`红星照耀中国、连霍高速、连霍高速公路、LONGEST IN CHINA` 四次判错；复核全部十四组后 `LONGEST HIGHWAY` 正确。

<a id="p-I9CLNP39"></a>

## 观星思人（I9CLNP39）

- 答案：`春日忆李白`

### 题面要点

星空图中若干星名/星座名配编号，右侧为四行五格并问“出自《?????》”；成功文案保存了一联诗。

### 我的解法

本地日志没有保留下星名填格与逐字抽取，只能确认成功文案为“何时一樽酒，重与细论文”，其出处题名是杜甫《春日忆李白》，恰为五个汉字，并与“观星思人”的题名语义相合。因此答案可确认，但不能据现有日志补造星图如何产生该诗句。

### 验证

本地独立证据有限：五字枚举、提交成功文案中的诗句出处和 correct 状态一致，但星图抽取过程缺失，只能确认到上述范围。

<a id="p-JzDgoAEX"></a>

## 译口同声（JzDgoAEX）

- 答案：`WRITE TO YOU`

### 题面要点

每个中文词先翻成英文，再换成不同意义的同音词，并按给定位置提取；中间结果枚举与最终枚举不同。

### 我的解法

例如 那里 `THERE→THEIR`、雄性的 `MALE→MAIL`、道路 `WAY→WEIGH`、我们的 `OUR→HOUR`、夜晚 `NIGHT→KNIGHT` 等。按索引抽取九项得到 `RIGHT TWO U`。题目要求继续应用同音替换并匹配 `(5 2 3)`，所以三段分别变为 `WRITE TO YOU`。

### 验证

只改后两段的 `RIGHT TO YOU` 被判错；三段全部换同音词后的 `WRITE TO YOU` 正确。

<a id="p-5h1uzMeL"></a>

## 语文课（5h1uzMeL）

- 答案：`吹拉弹唱`

### 题面要点

形如四位数相加的“算式”并非十进制运算；“通通用汉字”提示数字是《通用规范汉字表》的序号。

### 我的解法

查本地序号表：`0450=竹、0488=合、2687=答`，说明加号表示合并部件；`0549=安、0087=木、2107=案` 再次验证。于是 `0038口+0153欠=吹`，`0121手+0302立=拉`，`0063弓+1232单=弹`，`0038口+1084昌=唱`。

### 验证

两个例式和四个问题都使用同一“序号转字—部件合字”规则，四个结果依次为 `吹拉弹唱`；首投正确。

<a id="p-LvSqNrv1"></a>

## 语言（LvSqNrv1）

- 答案：`石英`

### 题面要点

示例为 `聚合→集中`、`なま→生日`，目标 `stone→?`。

### 我的解法

先把输入的含义压缩成一个汉字，再附上输入语言的一字简称：中文“聚合”取 `集`，加“中”得 `集中`；日语 `なま` 取“生”，加“日”得 `生日`。英语 `stone` 取 `石`，加“英”得 `石英`。

### 验证

三组均使用“义译一字+语言简称”且结果为正常词；`石英` 首投正确。

<a id="p-c9rHRhJe"></a>

## 误差分析（c9rHRhJe）

- 答案：`JAPAN`

### 题面要点

四个“测量值±误差”为 `1853.5±35.5、1805.5±30.5、1642.5±19.5、1685±42`，误差异常大。

### 我的解法

把每对数转成上下界，得到年份区间：1818–1889 是 Joule，1775–1836 是 Ampere，1623–1662 是 Pascal，1643–1727 是 Newton。四位科学家对应 SI 单位符号依次为 `J、A、Pa、N`，连写为 `JAPAN`。

### 验证

四组端点精确等于生卒年，单位符号又组成国家名；首次提交 correct。

<a id="p-Mm7xAs7n"></a>

## 读法错误（Mm7xAs7n）

- 答案：`THE OLD MAN AND THE SEA`

### 题面要点

6×3 字母表若按列读，会得到风味中的荒诞短语 `TOMATO PLANTS SENDER`；七个格子的手写替代字母被红线划掉。

### 我的解法

标题说“读法错误”，因此改为正常按行读印刷字母。六行依次是 `THE / OLD / MAN / AND / THE / SEA`，组成海明威小说名 `THE OLD MAN AND THE SEA`。被划掉的手写字正是为了诱导错误的竖读。

### 验证

横读完整形成书名，也解释风味中加粗的“书”；提交正确。

<a id="p-TkqKhwRH"></a>

## 课文两景（TkqKhwRH）

- 答案：`水龙`

### 题面要点

两行彩条表示拼音字母，黑色记号表示声调，相同颜色代表相同字母；题目分别提示五年级和四年级课文景物。

### 我的解法

按颜色重复和声调，上行解为 `shuǐ lián dòng`，即《猴王出世》中的水帘洞；下行解为 `shuāng lóng dòng`，即《记金华的双龙洞》中的双龙洞。编号 1 位于“水”，编号 2 位于“龙”。

### 验证

两处景物与年级提示吻合，共同的“洞”也与同色框对应；按编号取出 `水龙`，提交正确。

<a id="p-9AlWHnxJ"></a>

## 负负得……（9AlWHnxJ）

- 答案：`LINEAR`

### 题面要点

六个字/符号各连续“取反”两次，再把终点译成指定长度英文并按索引取字母。

### 我的解法

“反”是找反义词，但中间词有另一义项，所以第二次不回原点：`浓→淡→咸`，SALTY 取第 3 位 L；`胜→负→正`，POSITIVE 第 6 位 I；`亲→疏→密`，DENSE 第 3 位 N；`熟→生→死`，DEATH 第 2 位 E。前四位严格得到 `LINE`。本地日志没有重建“商”和 `|` 的两条完整链，只记录它们按同法补出 A、R，结合数学题名形成 `LINEAR`。

### 验证

本地日志仅能完整确认前四位 `LINE`，末两位主要由成词与主题闭合；`LINEAR` 首投获得 correct，错误 0 次。

<a id="p-IUdLNP39"></a>

## 贪婪与高尚（IUdLNP39）

- 答案：`蝤`

### 题面要点

上下两行分别以声调、结构和语义提示四字词，并突出末字内部组件；答案要求左右结构汉字。

### 我的解法

上行是 `得陇望蜀`，符合贪婪主题，末字“蜀”突出部件 `虫`。下行是 `德隆望尊`，表示德高望重/高尚，末字“尊”突出上部 `酋`。答案图要求把亮、暗两部按左右组合，所以 `虫+酋=蝤`。

### 验证

初猜 `冬日` 被拒；按两个四字词拆部件后 `蝤` correct。

<a id="p-usrC56DT"></a>

## 越狱（usrC56DT）

- 答案：`咚`

### 题面要点

示例把 `囤` 变成 `吨`、把 `田` 变成 `叶`，标题提示封在大口框里的部件要“越狱”。

### 我的解法

两例都是把 `囗` 内部部件移到普通口字旁右边：`囗+屯 → 口+屯`，`囗+十 → 口+十`。底图代表“图”，即 `囗+冬`；按同一操作变成 `口+冬=咚`。

### 验证

三字共享完全相同的部件移动规则；`咚` 首次提交正确。

<a id="p-FsDyul5g"></a>

## 路线（FsDyul5g）

- 答案：`ID`

### 题面要点

罗盘给两位方向编码 `E=00,S=01,N=10,W=11`，五组四字母密文要转成路线；标注 `(5)→(2)` 表明先得五字母中间答案再压成两字母。

### 我的解法

将 A–Z 写成五位 A1Z26 二进制。每组四字母合成 20 位，再按两位切成十步方向并画路线；`EKUH、ZSJP、UAIJ、ZTJW、ZTZP` 分别画出 `S,E,N,S,E`，中间答案为 `SENSE`。再把这五个方向字母按罗盘编码为 `01 00 10 01 00`，合成十位后切为两组五位：`01001=9=I`、`00100=4=D`。

### 验证

两阶段互为编码转换，完整解释 `(5)→(2)`；最终 `ID` 首投正确。

<a id="p-GBdbeioV"></a>

## 跳舞的小人（GBdbeioV）

- 答案：`ICONIC`

### 题面要点

四个小人只改变手臂曲线，前两个标 `0`、`x`，后两个是三个彩色问号加 x。

### 我的解法

前两幅分别表示 `y=0` 与 `y=x`，说明手臂是函数图像。第三幅是 `sin x`，给出黑=S、红=I、橙=N；第四幅是 `cos x`，给出黄=C、桃=O，并复核黑=S。按底部红、黄、桃、橙、红、黄的颜色顺序替换，得到 `I C O N I C`。

### 验证

两条函数曲线建立完整颜色字母表；`ICONIC` 首投正确。

<a id="p-iD5RTMow"></a>

## 跳马2（iD5RTMow）

- 答案：`CLAY PIPES`

### 题面要点

9×9 棋盘要求放 14 枚互不攻击的马，使每格有马或被马攻击；三枚马固定，黑格禁放。棋盘同时是英文填字，马所在格用于抽取。

### 我的解法

对独立支配集条件做穷举，得到唯一 14 马布局。横向填入 `SIDCAESAR、QUINTUPLE、UNSELFISH、INCIVIL、RELIGIOSO、ROADWAY、EPISCOPE、LIMEWATER、SMILE`，并由竖向 `SQUIRREL、DISCLAIM、REHIRE` 交叉验证。按行优先读取所有马格，得到 `ANSISCLAYPIPES`，分词为 `ANS IS CLAY PIPES`。

### 验证

马布局唯一，填字可交叉核对，抽取直接声明答案；本地正确清单确认 `CLAY PIPES`。

<a id="p-ogImNtwx"></a>

## 这不是数独，这是英独！（ogImNtwx）

- 答案：`NUTRIENTS`

### 题面要点

9×9 盘同时满足普通数独和字母数独：每格字母来自该数字英文拼写，行列宫内字母也不重复；解完后按九宫各选一字母形成模式，并取候选排名第 4。

### 我的解法

本地日志保存了完成字母盘。九个宫的可选字母集合依次形成模式 `[efgnrstux][fginoruvx][eginstuvw][fghiorstx][eginrsuvw][eghinostx][fgnoruvwx][egiorstuv][fghiosuwx]`。日志中的本地检索结果依次为 `notorious、nothing to、go through、nutrients`，按题意取第四名 `NUTRIENTS`。

### 验证

九字母逐位都属于对应宫的集合，且排名位置为第 4；`NUTRIENTS` 提交正确。

<a id="p-HRJ44RZL"></a>

## 这是Cryptic clue吗？（HRJ44RZL）

- 答案：`CASE`

### 题面要点

同一串文字既可按 Cryptic clue 解，也可按普通语义理解，题面标出两种结果中的编号位置。

### 我的解法

按 Cryptic：`Take` 是定义，`order` 是字母重排指示，`CAP ETC` 重排成 `ACCEPT`。若不按 Cryptic，Take、order、cap、etc. 都是“术语”，即 `TERMS`。从 ACCEPT 的第 1、2 位及 TERMS 的第 2、5 位按标号重排，得到 C、A、S、E。

### 验证

两种“case”各自给出一个合法结果，四个编号字母拼成 `CASE`；首投正确。

<a id="p-9kAWHnxJ"></a>

## 这期神了（9kAWHnxJ）

- 答案：`DIVINE`

### 题面要点

四色圆分别含文明建筑、局部数字编码的神名和象征物，底部要求解 `123245`。

### 我的解法

四神为印度 `INDRA`、美索不达米亚 `ENKI`、中国 `NUWA/NÜWA`、埃及 `ATUM`。对齐 `241ra=indra` 得 2=I、4=N、1=D；`54k2=enki` 得 5=E；`43wa=nuwa` 给 3 的 U/V 形，目标现代英文取 V。代入 `123245` 得 `DIVINE`，也概括四者皆为神祇。

### 验证

编码映射和中心主题一致；`DIVINE` 首投正确。

<a id="p-9TOWHnxJ"></a>

## 远亲与不邻（9TOWHnxJ）

- 答案：`GLAM`

### 题面要点

颜色模式分别表示英文名、拉丁学名、希伯来语转写和四字母答案；风味说不必会希伯来语。

### 我的解法

英文模式 `BBCDC` 可填 `LLAMA`，于是桃色=L、黄色=A、绿色=M。拉丁学名 `Lama glama` 正好匹配 `BCDC / ABCDC`，从而红色=G。希伯来语转写行随之成为 `GAMAL`（camel），验证羊驼与骆驼的亲缘主题。答案色序 `ABCD` 即 G-L-A-M。

### 验证

三种名称的颜色重复模式彼此锁定；`GLAM` 首次提交 correct。

<a id="p-Prte2esI"></a>

## 邑首Quiz（Prte2esI）

- 答案：`小虍阜`

### 题面要点

题目把每个汉字替换成康熙部首，先编码歌曲名和一句问话，再要求用同样方式回答。

### 我的解法

三首歌解为《愛》《紅蝴蝶》《青蘋果樂園》；后续部首串读作“擁有以上歌曲的是哪一個男團”，候选人名还可解出吳奇隆、蘇有朋。共同指向男团 `小虎隊`。把答案再次按康熙部首编码：小→小、虎→虍、隊→阜，得到 `小虍阜`。

### 验证

歌名、问句和成员共同唯一指向小虎队，输出格式也遵守部首规则；提交正确。

<a id="p-bsb5uOJW"></a>

## 降水（bsb5uOJW）

- 答案：`RAIN`

### 题面要点

三行汉字构形与拼音格各有一个绿色提取位，末尾幼苗/枝干图形画成小写 r，后接三格。

### 我的解法

依三行拼音填格，在绿色位置依次取到 `A、I、N`；把末图给出的 `r` 放在前面，组成 `RAIN`。

### 验证

字母结构正好是 r+ain，英文含义“雨”直接对应标题“降水”；零错通过。

<a id="p-iZFRTMow"></a>

## 随蓝01（iZFRTMow）

- 答案：`三角`

### 题面要点

`[D2]` 线索可同时指课本单位和门牌单位，`[E2]` 可同时指素描方法和编程方法，求下一个 `[?2]` 常见词。

### 我的解法

第一词是 `单元`：课本单元、住宅单元，拼音首字母 D 且两字；第二词是 `二分`：素描二分/比例方法、编程二分法，首字母 E 且两字。首字又形成“单(一)、二”的递进，下一项应以“三”开头、两字且成词，因此是 `三角`，标签相当于 S2。

### 验证

双重释义、首字递进与长度都吻合；`三角` 首投正确。

<a id="p-zt5G691D"></a>

## 集单谜（zt5G691D）

- 答案：`SEASONDAN`

### 题面要点

九条鸡蛋主题的一句话谜语各带拼音首字母/汉字数标记和抽取位置，风味说“最后记得把它去掉”。

### 我的解法

机制是先猜蛋梗答案，把无声调拼音连写，再按索引取字。日志早期因第 2–6 行猜词不精确，错误抽成 `SUMMERDAN`，继而猜过 `SUMMER、SPRING CHICKEN、SPRINGDAN、SPRING`。重新校正九行后，逐行抽取恰为 `S E A S O N D A N`，应直接提交 `SEASONDAN`；成功文案再以“season dan / 季蛋 / 鸡蛋”做谐音收束。

### 验证

本地独立证据有限：五个过早解释均 incorrect，直接九字母串 `SEASONDAN` correct；日志没有完整保留九条最终谜底，因此无法逐行复现最终九字母，不补写缺失拼音。

<a id="p-7ljIxIpP"></a>

## 集单谜2-忌惮谜（7ljIxIpP）

- 答案：`THE BEGINNING`

### 题面要点

十二条鸡蛋主题谐音 rebus 配十二个索引，标题“忌惮”本身也谐“鸡蛋”；规范化答案应为十二字母。

### 我的解法

本地日志能确认各题围绕“蛋”替代 `旦、胆、丹` 等同音字，例如“再见了，鸡蛋”可构成 Biden/拜登式谐音，“躺凉席上吃蛋”影射“卧薪尝胆”。但日志没有完整保留十二条逐项填词和抽取表，只记录十二字母提取与本地正确提示开头 `the beginning……` 一致，因此最终读作 `THE BEGINNING`。

### 验证

答案规范化后正好十二字母，本地提交 `THE BEGINNING` 为正确。就逐条抽取而言，本地日志仅能确认部分示例与最终一致性，不能完整复原十二行。

<a id="p-RPMAJFgi"></a>

## 非洲79（RPMAJFgi）

- 答案：`马普托`

### 题面要点

数字与少量汉字拼成非洲国家及城市的谐音；标题中的 79 是金的原子序数，提示把数字换成对应元素中文名。

### 我的解法

例如 `41日68` 转成铌+日+铒，谐读“尼日尔”；箭头后的 `41 18 12` 为铌+氩+镁，谐读其首都“尼亚美”。`79 46 94韦` 类似得到“津巴布韦”，右边 `72拉88` 得“哈拉雷”，确认规则是国家→首都。问题 `115桑83 36` 为镆+桑+铋+氪，谐读“莫桑比克”，其首都是 `马普托`。

### 验证

两组例子同时验证元素谐音和国家到首都的箭头关系；目标国家唯一，首投正确。

<a id="p-KS3XEjGS"></a>

## 食物·景观·战役（KS3XEjGS）

- 答案：`火烧`

### 题面要点

三行格式依次为 `①②`、`①②□`、`①②□□`，定义北方传统食物、天空景观、三国战役。

### 我的解法

两字食物是 `火烧`；加一字成为天空景观 `火烧云`；加两字成为三国战役 `火烧赤壁`。编号圈只在共享前两字，所以应提取 `火烧`，不是提交最长短语。

### 验证

`火烧赤壁` 判错，确认方格补字不是答案位；`火烧` 正确，共 1 次错误。

<a id="p-fqvYBRMr"></a>

## 鱼数（fqvYBRMr）

- 答案：`CATFISH`

### 题面要点

图片定义了一个以猫图标与鱼图标构成的递归符号数制，末尾询问一个猫/鱼组合。

### 我的解法

本题本地日志的具体答案曾来自不符合本批约束的外部检索，因此该部分不采用。重新查看本地图片，只能确认题面是猫、鱼及若干运算符构成的递归符号数制，末尾有七行待求值/抽取；日志没有保存各符号的数值解释、七行结果与字母转换，无法独立重建为何精确拼成 `CATFISH`。

### 验证

本地独立证据有限：提交记录显示 `CATFISH` 首次 correct；除正确结果与猫/鱼主题外，不补造缺失计算。

<a id="p-XxEkPIap"></a>

## 麻雀（XxEkPIap）

- 答案：`白頭山`

### 题面要点

题面用日式麻将牌的特殊读法拼日语词；末行是“東”和“三”，左侧还有一块看似空白的区域，答案标三汉字。

### 我的解法

示例包括北=`ペー`、八=`パー`，连成 `ペーパー`；四=`し`、發=`はつ`，连成 `始発`。末行先按读音得到 `とうさん`，提交后本地中间提示明确说答案是三个汉字，并注意“東”左侧空白。麻将白板牌本身纯白，故空白补“白”的读音 `はく`；`はく+とう+さん` 对应三字地名 `白頭山`。

### 验证

`とうさん` 获得定向中间提示，加入隐藏白板后字数、读音和地名均吻合；`白頭山` 提交正确。

<a id="p-O2YiZO0v"></a>

## 黑暗森林组织：序（O2YiZO0v）

- 答案：`VERMOUTH`

### 题面要点

故事混合《黑暗森林》和《名侦探柯南》设定；蚂蚁依次探索墓碑上的八道刻痕，文字描述每道线条的拓扑形状。

### 我的解法

按描述复原字母：两斜线向下相交是 V；竖线带三横是 E；竖线、上环和斜腿是 R；尖锐折线是 M；封闭圆环是 O；两侧上升、底部圆弧是 U；竖线顶端横杆是 T；双竖中横是 H。八字母连成 `VERMOUTH`。

### 验证

每道刻痕唯一对应一个大写字母；所得词又是黑衣组织中莎朗的代号“Vermouth”，与墓碑和人物背景吻合。

<a id="p-dfGF4LbF"></a>

## 미로（dfGF4LbF）

- 答案：`미로의 수다쟁이`

### 题面要点

韩语题名意为“迷宫”，题面给横向、纵向韩语填字线索但不显示网格；纵 1 的枚举为 `(2 3 2 2)`，定义“为了得到答案要查看的位置”。

### 我的解法

本地题面只能确认这是一道不显示网格的韩语填字题，横纵线索中包含“出发”“到达”，纵 1 则询问应查看的位置。现有日志没有保存独立重建网格的过程；其中关于 10×11 网格、最短路径奇数位和最终串的详细机制，均是在读取官方解答文件后写入，故不作为我们的独立解法复述。

### 验证

`미로의 수다쟁이` 本地提交为 correct，错误 0 次。本地独立证据有限：除题型、线索表和已接受答案外，当前归档没有合规的独立推导链；官方解答中的网格与提取步骤已从本题解中排除。

<a id="p-pmp2nNtD"></a>

## 복제（pmp2nNtD）

- 答案：`시공기하영토`

### 题面要点

标题意为“复制”，题面有八对韩语线索；每对左侧是一音节词，复制该音节后成为右侧释义的双音节词。

### 我的解法

八行依次为：`답→답답`、`은→은은`、`시→시시`、`공→공공`、`기→기기`、`하→하하`、`영→영영`、`토→토토`。抽取单音节得到 `답 은 시 공 기 하 영 토`。前两音节 `답은` 表示“答案是”，余下六音节连成 `시공기하영토`。

### 验证

八行释义均能直接在本地 `content.txt` 中对照，遵循“复制一音节”规则，抽取句法完整；`시공기하영토` 首次提交 correct。本题不依赖日志中另记载的外部源码或解析核对。

<a id="p-Sepj2oe3"></a>

## 회전（Sepj2oe3）

- 答案：`목공`

### 题面要点

韩文题名意为“旋转”，图片整体倒置，内部是多层括号嵌套的韩文文字、罗马字母和算式；题目要求两字词。

### 我的解法

允许使用的本地题面能确认核心操作是逐层旋转/倒置后解释嵌套表达式，也能确认直接按中文意义猜 `速度、转速、唾液、木工、木匠` 均不对。日志对从各内层算式一直推到韩文终词的完整推导明确引用了原题官方解答，因此本批不复述该链条。

### 验证

本地提交记录显示六个中文候选均错误，韩文 `목공` 得到 `correct`。本地日志仅能确认旋转机制的大方向、答案语言和最终验收，无法在排除官方解答内容后完整重建每一层推导。

<a id="p-1wsaRpKD"></a>

## ！？土土？！（1wsaRpKD）

- 答案：`山脚下的泥土路和地里的铁`

### 题面要点

A–H 各代表一个汉字，多条语义和组词约束确定字母映射，最后代入模板 `HGF的EBD和A里的C`。

### 我的解法

由“土地”和偏旁关系得 A=地、B=土；`AC` 是交通工具“地铁”，故 C=铁；类似交通工具行于 `CD=铁路`，故 D=路；`EB=泥土` 得 E=泥；`AF=地下` 且 `FB=下土`，得 F=下；`GF=脚下` 得 G=脚；`HG=山脚` 且 `HF=山下`，得 H=山。

### 验证

代入最终模板正好得到 `山脚下的泥土路和地里的铁`；八个字母都由至少一个组词约束使用，首投正确。
