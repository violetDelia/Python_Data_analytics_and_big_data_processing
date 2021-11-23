
from lxml import etree

html = """
<div>
    <ul>
        <li><p class="test1">这是第1个li</p></li>
        <li  class="test3"><p class="test2">这是第2个li</p></li>
        <li  class="test4"><p class="test3">这是第3个li</p></li>
    </ul>
    这是div的内容
</div>
"""
html_obj = etree.HTML(html)
li_list = html_obj.xpath("//div/ul/*[@class='test4']")
for i in li_list:
    print("获取到的元素：", i)
li_list_attr = html_obj.xpath("//div/ul/*[@class]")
for i in li_list_attr:
    print("class属性值：", i.attrib["class"])

	
	