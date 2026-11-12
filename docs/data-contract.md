# 安全裁剪抽象域

AST字面量携字段类型，op为and/or(args非空)、not(arg)、eq/ne/lt/le/gt/ge(field,value)、in(field,values)、is_null/is_not_null(field)。不支持列对列比较。null字面量比较和IN的null项按SQL三值；IN空表总FALSE，NOT按三值，NaN与任意值eq为FALSE、ne为TRUE，排序比较为FALSE；IS NULL只识别null，NaN不是null。正负零相等。timestamp按UTC微秒整数，long按有符号64位，double特殊值用{"float":"nan"}表示。

value_count是该列所有行含null/NaN个数，须等record_count，null_count+nan_count<=value_count。bounds针对非null非NaN。缺列metrics表示未知，不能推成全null。string exact界按UTF8字节序；prefix界声明lower_prefix_hex和upper_prefix_hex、字节长度k，含义是所有值前min(k,len(value))字节落在闭区间，两端可截到多字节字符中间，不能强制解UTF8。除声明的prefix约束之外不假定upper是完整最大值，允许保守丢弃这条界。

partition变换day以UTC微秒除86400000000取数学floor；bucket编码沿资料约定SHA256类型前缀。文件spec独立。解释器为独立逐行语义，统计规划不使用reference_rows生成决策。keep可以误保留，drop不允许漏任何TRUE。
