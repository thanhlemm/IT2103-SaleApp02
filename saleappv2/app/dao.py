def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    }, {
        'id' : 2,
        'name': 'Tablet'
    }]

def load_products(kw):
    products = [{
        'id': 1,
        'name': 'iPad Pro 2022',
        'price': 24000000,
        'image' :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU'
    }, {
        'id': 2,
        'name': 'iPhone 15',
        'price': 20000000,
        'image' :'https://nld.mediacdn.vn/291774122806476800/2023/9/13/apple-iphone-15-pro-lineup-color-lineup-geo-230912bigjpglarge2x-16945655616201637318914.jpg'
    },{
        'id': 3,
        'name': 'iPad Pro 2022',
        'price': 24000000,
        'image' :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU'
    }, {
        'id': 4,
        'name': 'iPad Pro 2022',
        'price': 24000000,
        'image' :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU'
    }, {
        'id': 4,
        'name': 'iPad Pro 2022',
        'price': 24000000,
        'image' :'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSh3NyvBAdWsidoZ1r_iSn9mtUbPI7aqysds3RcScZ9OMADWwfWfMJIBNfVs5MuLxoTTQM&usqp=CAU'
    }]

    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]
    return products