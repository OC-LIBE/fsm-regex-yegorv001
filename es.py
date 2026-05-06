import re

txt = product_description = """
<div class="long-description">
    <p><strong>Amazing</strong> and&amp; creative  sample description of  a \
    product&trade; with <em>5-star***** reviews!!!</em></p>
</div>
"""

def func(txt):

    pattern1 = r'<\W\w+>'
    pattern2 = r'<\w+>'
    pattern3 = r'<div \w+\W+\w+\W+\w+\W>'
    pattern4 = r'\w+&\w+'
    x1 = re.sub(pattern1, "", txt)
    x2 = re.sub(pattern2, "", x1)
    x3 = re.sub(pattern3, "", x2)
    x4 = re.sub(pattern4, "", x3)
    return x4

print(func(txt))