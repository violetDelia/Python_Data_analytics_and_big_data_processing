
from lxml import etree

html = """
<div>
    <ul>
        <li><p class="test1">这是第1个li</p></li>
        <li class="test4"><p class="test2">这是第2个li</p></li>
        <li class="test4"><p class="test3">这是第3个li</p></li>
    </ul>
    这是div的内容
</div>
"""
html_obj = etree.HTML(html)


print("获取当前层级：")
cur_content = html_obj.xpath("//div/text()")
for i in cur_content:
    print("获取到的内容：", i)

print("-------------------------------------")
print("获取当前与所有子级：")
all_content = html_obj.xpath("string(//div)")
print("获取到的元素：", all_content)


