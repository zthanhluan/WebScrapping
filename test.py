from bs4 import BeautifulSoup
import re

# Your HTML input
html = '''
<span class="sc-jsMahE sc-kFuwaP jSUKcK fdKTiB" data-testid="duration">2h 5ph</span>, 
<span class="a067f-box a067f-fill-inherit a067f-text-inherit a067f-items-end a067f-flex a067f-flex-col" data-element-name="flight-price-breakdown">
<div class="a067f-box a067f-fill-inherit a067f-text-inherit a067f-items-end a067f-flex a067f-flex-col">
<div class="a067f-box a067f-fill-inherit a067f-text-inherit a067f-items-baseline a067f-inline-flex a067f-flex-row a067f-mb-xs" dir="ltr">
<span class="sc-csCMJt bvCKbC">Giá gốc: 2.505.630 ₫</span>
<span aria-hidden="true" class="sc-jsMahE sc-kFuwaP bEtAca frpCWd" data-testid="crossout-price">2.505.630 ₫</span></div>
<div class="a067f-box a067f-fill-inherit a067f-text-inherit a067f-items-baseline a067f-inline-flex a067f-flex-row a067f-mb-xs" dir="ltr">
<span class="sc-jsMahE sc-kFuwaP bEtAca cyWjYO">2.404.544</span>
<span class="sc-jsMahE sc-kFuwaP eYeVVH bpqEor">₫</span></div></div></span>, 
<span class="sc-csCMJt bvCKbC">Giá gốc: 2.505.630 ₫</span>, 
<span aria-hidden="true" class="sc-jsMahE sc-kFuwaP bEtAca frpCWd" data-testid="crossout-price">2.505.630 ₫</span>, 
<span class="sc-jsMahE sc-kFuwaP bEtAca cyWjYO">2.404.544</span>, 
<span class="sc-jsMahE sc-kFuwaP eYeVVH bpqEor">₫</span>, 
<span class="sc-jsMahE sc-kFuwaP bEtAca iWvotD sc-ktEKTO gwsfLE" label="Chi tiết">Chi tiết<svg aria-hidden="true" class="sc-eDDNvR sc-jTrPJq csIrST cIttmB" opacity="1" role="img"><use href="#9711fb1d"></use></svg></span>, 
<span class="a067f-box a067f-fill-inherit a067f-text-inherit">• </span>, 
<span class="a067f-box a067f-fill-inherit a067f-text-inherit">• </span>, 
<span class="sc-jsMahE sc-kFuwaP bEtAca jkQDVs">Chọn</span>, 
<span><svg aria-hidden="true" fill="none" role="img" viewbox="0 0 95 6" xmlns="http://www.w3.org/2000/svg">
<path cliprule="evenodd" d="M0 5C0 4.44772 0.498412 4 1.11323 4H82C82 4 82 4.44772 82 5C82 5.55228 82 6 82 6H1.11323C0.498412 6 0 5.55228 0 5Z" fill="#B1B9CB" fillrule="evenodd"></path>
<path d="M82 4.85714L82.0001 0L94.2767 4.66835C94.323 4.68595 94.3712 4.69952 94.4189 4.71269C95.3459 4.96838 95.1124 6 94.0829 6H82.0001L82 4.85714Z" fill="#B1B9CB"></path>
</svg></span>
'''

# Parse the HTML
soup = BeautifulSoup(html, "html.parser")

# Find all span tags
all_span = soup.find_all("span")

# Regular expression to find prices
price_pattern = r"(\d{1,3}(?:\.\d{3})+)"

# Extract and filter prices from span tags
matches = []
for span in all_span:
    if span.string:  # Check if the span contains text
        match = re.search(price_pattern, span.string)
        if match:
            matches.append(match.group(1))

# Print all extracted prices
print("Extracted prices:", matches)

# Access the first price element
if matches:
    price_element = matches[0]
    print("First extracted price:", price_element)