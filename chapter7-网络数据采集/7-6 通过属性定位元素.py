
from lxml import etree

html = """
<div>
    <ul>
        <li><p class="test1">这是第1个li</p></li>
        <li  class="test4"><p class="test2">这是第2个li</p></li>
        <li  class="test4"><p class="test3">这是第3个li</p></li>
    </ul>
    这是div的内容
</div>
"""
html_obj = etree.HTML(html)
p_element = html_obj.xpath("//div/ul/li/p[@class='test1']")
print(p_element)

