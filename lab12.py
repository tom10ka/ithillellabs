import requests

url = 'https://script.googleusercontent.com/macros/echo?user_content_key=g--wIIvZzzhjImsmdqn5WXq82Dg-X-_XEf0KSp4PX_NjyrtFEMl8zI5kclide4eS6nlI30vVUM8bxAyMP8Y2c1Hikm9EUYd2m5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnJJSz-0qgNnrjX_lsmjyF66AquHjXmDhbua3x6VUlwrMS4HaXlKRjvWwrQxiYFxAdff-H-FPGOuEUWsSDVQYINaFCpdjScVu7A&lib=MePDWmZU7aIdRiHQVCmZnzjUevPycBIIq'

response = requests.get(url)
inner_data = response.json()
clean_data = inner_data['data']
whole_price = 0
product_price = 0
product_quantity = 0
whole_price_no_gluten = 0
for product in clean_data:
    product_price = float(product.get('price', 0))
    product_quantity = float(product.get('quantity', 0))
    whole_product_price = product_price * product_quantity
    whole_price += whole_product_price
    product_gluten = product.get('is_gluten')
    if product_gluten is False:
        whole_price_no_gluten += whole_product_price
print(f'General price of all goods {whole_price}')
print(f'General price of all non-gluten goods {whole_price_no_gluten}')